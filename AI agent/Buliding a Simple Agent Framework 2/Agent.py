"""Kết hợp các thành phần lại với nhau để xây dựng 1 lớp Agent có khả năng tái sử dụng.
Lớp này bao gồm các thành phần của GAME và cung cấp 1 giao diện đơn giản chạy agent loop."""

#Step1: Constructing Prompt
def construct_prompt(self, goals: List[Goal], memory: Memory, actions: ActionRegistry) -> Prompt:
    return self.agent_language.construct_prompt(
        actions = actions.get_actions(),
        environment = self.environment,
        goals = goals,
        memory = memory,
    )

#Step2: Generating a Response
def prompt_llm_for_action(self, full_prompt: Prompt) -> str:
    response = generate_response(full_prompt)
    return response

#Step3: Parsing the Response
def get_action(self, response):
    invocation = self.agent_language.parse_response(response)
    action = self.actions.get_action(invocation["tool"])
    return action, invocation

#Step4: Executing the Action
result = self.environment.execute_action(action, invocation["args"])

#Step5: Updating memory
def update_memory(self, memory: Memory, response: str, result: dict):
    new_memories = [
        {"type": "assistant", "content" : response},
        {"type": "user", "content": json.dumps(result)}
    ]
    for m in new_memories:
        memory.add_memory(m)

#Step6: Termination Check
def should_terminate(self, response: str) -> bool:
    action_def, _ = self.get_action(response)
    return action_def.terminal