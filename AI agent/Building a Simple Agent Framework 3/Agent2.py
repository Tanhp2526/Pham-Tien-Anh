import os
import sys
from litellm import completion
from typing import List, Dict, Optional
from dataclasses import dataclass
#Define the Goals
@dataclass(frozen=True)
class Goal:
    prioritty: int
    name: str
    description: str

goals = [
    Goal(
        prioritty=1,
        name="Khám phá tài liệu",
        description="Khám phá tài liệu cso trong thư mục hiện tại bằng cách liệt kê và đọc chúng." #Explore files in the current directory by listing and reading them.
    ),
    Goal(
        prioritty=2,
        name="Terminate",
        description="Kết thúc phiên khi yêu cầu được hoàn thành, kèm theo bản tóm tắt hữu ích." #Terminate the session when the tasks are complete with a helpful summary.
    )
]

#Create Actions Using the Framework
class Action:
    def __init__(self,
                 name: str,
                 function: callable,
                 description: str,
                 parameters: Dict,
                 terminate: bool = False):
        self.name = name
        self.function = function
        self.description = description
        self.terminate = terminate
        self.parameters = parameters

    def execute(self, **args):
        return self.function(**args)#trả về hàm action dựa trên tham số đầu vào
class ActionRegistry:
    def __init__(self):
        self.actions = {}
    
    def resgister(self, action: Action):
        self.actions[action.name] = action

    def get_action(self, name:str) -> Optional[Action]:
        return self.actions.get(name)
    
    def get_actions(self) -> List[Action]:
        return list(self.actions.values())

def list_file() -> List[str]:
    """Liệt kê tất cả file có trong thư mục hiện tại"""
    return os.listdir(".")

def read_file(file_name: str) -> str:
    """Đọc nội dung của 1 file"""
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileExistsError:
        return f"Error: {file_name} not found."
    except Exception as e:
        return f"Error: {str(e)}"
    
def terminate(message: str) -> str:
    """Kết thúc vòng lặp agent và cung cấp 1 bản tóm tắt"""
    return message

"""tạo và đăng ký action"""
action_registry = ActionRegistry()

action_registry.resgister(Action(
    name="list_files",
    function=list_file,
    description="Trả về danh sách các tài liệu có trong thư mục hiện tại.", #Return a list of files in the directory.
    parameters= {},
    terminate=False
))

action_registry.resgister(Action(
    name="read_file",
    function=read_file,
    description="Đọc nội dung của tài liệu được chỉ định trong thư mục.", #Read the content of a specified file in the directory.
    parameters={
        "type":"object",
        "properties":{
            "file_name":{
                "type":"string"
            }
        },
        "required":["file_name"]
    },
    terminate=False
))

action_registry.resgister(Action(
    name="terminate",
    function=terminate,
    description="Kết thúc cuộc hội thoại. In ra tin nhắn cung cấp cho người dùng.",#Terminate the conversation. Prints the provided message for the user.
    parameters={
        "type":"object",
        "properties":{
            "message": {"type": "string"},
        },
        "required": ["message"]
    },
    terminate= True
))

class Memory:
    def __init__(self):
        self.items = []
    
    def add_memory(self, memory: dict):
        return self.items.append(memory)
    
    def get_memories(self, limit: int = None):
        return self.items[:limit]
    
#Create and Run the Agent
"""Create the Agent"""
flie_explorer_agent = Agent(
    goals= goals,
    agent_language= agent_language,
    action_registry= action_registry,
    generate_response = generate_response,
    environment = environment
)
"""Run the agent"""
user_input = input("What would you like to do? ")
final_memory = flie_explorer_agent.run(user_input, max_iterations = 10)

# Print the final conversation if desired
for item in final_memory.get_memories():
    print(f"\n{item['type'].upper()}: {item['content']}")