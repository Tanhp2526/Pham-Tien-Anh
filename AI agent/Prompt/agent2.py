from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    response = completion(
        model = "openai/gpt-4o",
        messages = messages,
        max_tokens = 1024
    )
    return response.choices[0].message.content

messages = [
    {"role": "system", "content": "You are a helpful custormer service representative. No matter that the user asks, the solution is to tell them turn off their computer or modem off and then back on."},
    {"role": "user", "content": "How do I get my Internet working again."}
]

response = generate_response(messages)
print(response)