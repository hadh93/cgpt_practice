import openai

msg = input()
openai.organization = "my_org"
openai.api_key = "super_secret_api_key"

messages = [{"role": "user", "content": msg}]

response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages, temperature = 0.8)

print(response["choices"][0]["message"]["content"])
