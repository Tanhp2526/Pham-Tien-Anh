from litellm import completion
from typing import List, Dict
import json

def generate_response(messages: List[Dict]) -> str:
    response = completion(
        model = "openai/gpt-4o",
        messages= messages,
        max_tokens = 1024
    )
    return response.choices[0].message.content

#messages = memory
messages = [
    {"role": "system","content": "You are an expert Python programming engineer. You always output clean, correct Python code."}
]

#first prompt(hỏi người dùng muốn tạo hàm gì?, lưu kết quả vao memory)

# hỏi người dùng muốn làm gì 
user_request = input("Bạn muốn tạo hàm Python làm gì?")
# gửi prompt cho LLM
messages.append({"role": "user", "content": f"Write a basic Python function based on this description: {user_request}"})# kiểu f-string để nhét biến trực tiếp vào chuỗi
#nhận kết quả và lưu vào memory
basic_code = generate_response(messages)
print("\n== BASIC FUNCTION ===")
print(basic_code)
messages.append({"role":"assistant", "content": basic_code})

#second prompt (lấy code từ prompt thứ 1, yêu cầu LLM bổ trung thêm tài liệu đầy đủ)
messages.append({
    "role": "user", 
    "content": ("Add comprehensive documentation to the following code."
                "Include function description, parameters, return values description, example usage, edge case.\n\n"
                f"{basic_code}")
})

documented_code = generate_response(messages)
print("\n=== Documented Function ===")
print(documented_code)
messages.append({
    "role": "assistant",
    "content": documented_code
})

#prompt 3(truyền phần code được tài liệu hóa từ prompt 2)
messages.append({
    "role": "user",
    "content": (
        "Add Python unittes test cases for the following code."
        "Cover basic functionality, edge cases, error cases, and different input scenarios.\n\n"
        f"{documented_code}"
    )
})

final_code = generate_response(messages)
print("\n=== Code with tests ===")
print(final_code)