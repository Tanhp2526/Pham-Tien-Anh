from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str :
    response = completion (
        model = "openai/gpt-4o",
        messages= messages,
        max_tokens = 1024
    )
    return response.choices[0].message.content


messages = [
    {"role": "system", "content":"You are an expert sofeware engineer that functional programming."},
    {"role": "user", "content": "Write a functional to swap the keys and values in a dictionary."}
]

response = generate_response(messages)
print(response)