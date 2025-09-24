# custom client with custom model loader

from types import SimpleNamespace
from ollama import Client

from autogen.oai.openai_utils import config_list_from_json

# must import these from autogen with pip install autogen.
from autogen.agentchat import AssistantAgent, UserProxyAgent


from helper.tool import extract_thinking_and_response

class CustomModelClient:
    def __init__(self, config, **kwargs):
        print(f"CustomModelClient config: {config}")
        self.model_name = config["model"] if "model" in config else "deepseek-r1:7b"
        self.client = Client()


    def create(self, params):
        if params.get("stream", False) and "messages" in params:
            raise NotImplementedError("Local models do not support streaming.")
        else:
            num_of_responses = params.get("n", 1)

            # can create my own data response class
            # here using SimpleNamespace for simplicity
            # as long as it adheres to the ClientResponseProtocol

            response = SimpleNamespace()
            messages = params["messages"]

            response.choices = []
            response.model = self.model_name

            for _ in range(num_of_responses):
                choice = SimpleNamespace()
                ollama_response = self.client.chat(model=self.model_name, messages=messages) 
                answer = ollama_response['message']['content']
                choice.message = SimpleNamespace()
                choice.message.content = answer
                choice.message.function_call = None
                response.choices.append(choice)

            return response

    def message_retrieval(self, response):
        """Retrieve the messages from the response."""
        choices = response.choices
        return [choice.message.content for choice in choices]

    def cost(self, response) -> float:
        """Calculate the cost of the response."""
        response.cost = 0
        return 0

    @staticmethod
    def get_usage(response):
        # returns a dict of prompt_tokens, completion_tokens, total_tokens, cost, model
        # if usage needs to be tracked, else None
        return {}


 
def main():
    config = {
        "model": "deepseek-r1:7b",
        "model_client_cls": "CustomModelClient"
    }
    config_list_custom = [config]

    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list_custom})
    user_proxy = UserProxyAgent(
        "user_proxy",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,
        },
    )

    assistant.register_model_client(model_client_cls=CustomModelClient)
    
    # initiate_chat 返回 ChatResult 对象，包含对话历史
    # 设置 silent=True 和 max_turns=1 避免交互式输入
    result = user_proxy.initiate_chat(
        assistant,
        clear_history=True,
        message="Write python code to print hello world",
        silent=True,
        max_turns=1
    )
    
    
    # 从对话历史中获取最后一条消息的内容
    if result.chat_history:
        # 获取最后一条消息（通常是助手的回复）
        last_message = result.chat_history[-1]
        answer = last_message.get('content', '')
        print("助手回复:")
        print(answer)
        thinking_text, actual_response = extract_thinking_and_response(answer)
        print("思考过程:")
        print(thinking_text)
        print("AI 回答:")
        print(actual_response)
    else:
        print("没有收到回复")


if __name__ == "__main__":
    main()


