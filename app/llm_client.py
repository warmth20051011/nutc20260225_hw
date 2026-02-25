# 接 LiteLLM
import requests
from app.config import LITELLM_URL

def call_llm(messages):
    payload = {
        "model": "company-llm",   
        "messages": messages,
        "temperature": 0.2
    }

    try:
        response = requests.post(LITELLM_URL, json=payload, timeout=60)
        response.raise_for_status()  # 如果 400/500 就會丟到 except
        data = response.json()
        # 避免 KeyError
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        print("💥 LLM API HTTPError:", e)
        print("Response content:", response.text)
        return f"LLM API 錯誤: {response.text}"
    except Exception as e:
        print("💥 LLM API 其他錯誤:", e)
        return f"LLM API 其他錯誤: {str(e)}"
