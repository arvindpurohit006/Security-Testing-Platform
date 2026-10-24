import requests
import json 

def send_prompt(targetdata, prompt):
    url = targetdata["api_endpoint"]
    model = targetdata["model_name"]

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }
    response = requests.post(url, json=payload)
    data = response.json()
    print(data)
    llm_response = data["message"]["content"]
    # llm_response=data["answer"]["value"]
    return llm_response

