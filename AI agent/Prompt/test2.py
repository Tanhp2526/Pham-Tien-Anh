import json
import os
from litellm import completion  
from typing import List, Dict

#use function calling LLM 
# Defining tool function(định nghĩa hàm công cụ)
# type hint nghĩa là gợi ý kiểu dữ liệu 
# ví dụ : List[str]
def list_file():
    """Danh sách các tài liệu có trong thư mục hiện tại."""
    return os.listdir(".")

def read_file(file_name):
    """Đọc nội dung của 1 file"""
    try:
        with open(file_name, "r") as file:
            return file.read()# đọc toàn bộ file và trả về chuỗi
    except FileExistsError: # nếu file không tổn tại
        return f"Error: {file_name} not found."
    except Exception as e: # nếu lỗi khác
        return f"Error: {str(e)}"
#create a function Registry (tạo bảng đăng ký hàm)
tool_functions = {
    "list_files": list_file,
    "read_file": read_file
}

#define tool specifications using JSON Schema(mô tả các công cụ cho mô hình)
tools = [
    {
        "type" :"function",
        "function": {
            "name": "list_files",
            "description":" Return a list of files in the directory.",
            "parameters": {
                "type": "object",
                "properties":{},
                "required": []
            }
        }
    },
    {
        "type":"function",
        "function": {
            "name":"read_file",
            "description": "Reads the content of af specified file in the directory.",
            "parameters":{
                "type":"object",
                "properties": {"file_name" : {"type" : "string"}},
                "required": ["file_name"]
            }
        }
    }
]

#set up the agent's Instructions(thiet lap chi dan cho Agent)
agent_rules = [
    {"role": "system", 
     "content": """
You are an AI agent that can perform tasks by using available tools.

If a user askes about files, documents, or content, first list the files before reading them.
"""
}
]

#prepare the conversation context
user_task = input("What would you like me to do?")
memory = [
    {"role": "user",
     "content": user_task}
]
messages = agent_rules + memory

#make API call with function Definitions
response = completion (
    model = "openai/gpt-4o",
    messages = messages,
    tools = tools,
    max_tokens = 1024
)

# extract tool call the response
tool = response.choices[0].message.tool_calls[0]
tool_name = tool.function.name
tool_args = json.load(tool.function.arguments)
result = tool_functions[tool_name](**tool_args)