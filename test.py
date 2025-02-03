

def call_llm(prompt,model='llama3:latest'):
    import requests
    try:
        url = "https://gpt.sslwireless.com/api/chat/completions"
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        headers = {
            "Authorization": "Bearer sk-5c54250e72264f1982442da3fb5523fb",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload,headers=headers)
        if response.status_code == 200:

            return response.json()['choices'][0]['message']['content']
        else:
            print(f"Custom LLM Error: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Error in CustomLLM: {e}")
        return None

# Use this tiny function to leverage our local LLM in any Python script without any hassle.

print(call_llm("Hi"))
print(call_llm("what is ai"))
print(call_llm("give me a python code"))



