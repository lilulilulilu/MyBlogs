# https://api.dify.ai/v1
# api key: app-GS0kHP7xcM0af7RbdTebfSP2

import requests

dify_app_url = "https://api.dify.ai/v1/chat-messages"
dify_api_key = "app-Gxxx"

def chat(query: str) -> str:
    headers = {
        "Authorization": f"Bearer {dify_api_key}"
    }
    data = {
        "inputs": {},
        "conversation_id": "",
        "response_mode": "blocking",
        "query": query,
        "user": "abc-123"
    }
    response = requests.post(dify_app_url, headers=headers, json=data)
    print(f'response:{response.json()}')
    return response.json()['answer']

if __name__ == "__main__":
    query = "WPP是什么?"
    answer = chat(query)
    print(f'answer:{answer}')
    