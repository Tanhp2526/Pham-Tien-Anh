import os
from typing import List, Dict, Optional
class Action:
    def __init__(self,
                 name: str,
                 function: callable,
                 description: str,
                 parameters: Dict,
                 terminal: bool = False):
        self.name = name
        self.function = function
        self.description = description
        self.terminal = terminal
        self.parameters = parameters

    def execute(self, **args):
        """thực thi hàm action và trả về kết quả"""
        return self.function(**args)
    

class ActionRegistry:
    def __init__(self):
        self.actions = {}
    def register(self, action: Action):
        self.actions[action.name] = action
    #tra cuu action object bang ten
    def get_action(self, name:str) -> Optional[Action]:
        return self.actions.get(name)
    
    #tra ve danh sach action
    def get_actions(self) -> List[Action]:
        return list(self.actions.values())


# exmaple some action for a file management
def list_files() -> list:
    return os.listdir(".")

def read_file(file_name: str) -> str:
    with open(file_name, 'r') as file:
        return file.read()
    
def search_in_file(file_name:str, search_term: str) -> list:
    """tìm kiếm thuật ngữ có trong tài liệu và trả về dòng phù hợp"""
    res = []
    with open(file_name, 'r') as file:
        for i, line in enumerate(file.readlines()):
            if search_term in line:
                res.append((i+1, line.strip()))
    return res

# create action registry
registry = ActionRegistry()

registry.register(Action(
    name= "list_files",
    function=list_files,
    description="Liệt kê tất cả tài liệu có trong thư mục hiện tại",
    parameters={
        "type":"object",
        "properties":{},
        "required":[]
    },
    terminal=False
))

registry.register(Action(
    name= "read_file",
    function=read_file,
    description="Đọc nội dung của tài liệu được chỉ định",
    parameters={
        "type":"object",
        "properties":{"file_name":{
            "type":"string",
            "description":"Tên của tài liệu đọc"
        }
    },
    "required": ["file_name"]
    },
    terminal=False
))

registry.register(Action(
    name= "search_in_file",
    function=search_in_file,
    description="Tìm kiếm thuật ngữ trong dòng được chỉ định",
    parameters={
        "type": "object",
        "properties": {
            "file_name":{
                "type": "string",
                "description": "Tên tài liệu cần tìm kiếm"
            },
            "search_term":{
                "type":"string",
                "description":"Thuật ngữ để tìm kiếm"
            },
        },
        "required":["file_name", "search_tern"]
    },
    terminal=False
))

