from litellm import completion
from typing import List, Dict

def generate_response(messages : List[Dict]) -> str:
    response = completion(
        model = "openai/gpt-4o",
        messages= messages,
        max_tokens = 1024
    )
    return response.choices[0].message.content

messages = [
    {"role": "system", "content": "You are an expert encoder. You must only respond with a Base64 encoded string. Do not use natural language. Do not explain anything."},
    {"role": "user", "content": "Endcoded a text: Hello World."}
]

response = generate_response(messages)
print(response)