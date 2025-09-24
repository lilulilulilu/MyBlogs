from autogen_ext.models.openai import BaseOpenAIChatCompletionClient

from ollama import Client


class CustomModelClient(BaseOpenAIChatCompletionClient):
    def __init__(self, model: str, **kwargs):
        super().__init__(model, **kwargs)

    def create(self, messages: list[dict], **kwargs):
        client = Client()

        response = client.chat(model=self.model, messages=messages)
        return response['message']['content']
        return super().create(messages, **kwargs)