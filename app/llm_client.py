# 接 LiteLLM
import requests
from app.config import LITELLM_URL

def call_llm(messages):
    response = requests.post(
        LITELLM_URL,
        json={
            "model": "company-llm",
            "messages": messages,
            "temperature": 0.2
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
