import openai

class ChatApp:
    def __init__(self):
        openai.organization = "my_org"
        openai.api_key = "super_secret_api_key"
        self.messages = [
            {
                "role":"system",
                "content":"너는 끝말잇기 게임 상대 역을 맡은 채팅 봇이야."
            }
        ]

    def chat(self, msg):
        try:
            self.messages.append(
            {"role":"user", "content" : msg}
            )
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo", 
                messages = self.messages,
                temperature = 0.8)
            response_msg = response["choices"][0]["message"]["content"]
            print(response_msg)
            self.messages.append(
                {"role":"assistant", "content":response_msg}
                )
        except openai.error.RateLimitError:
            print("너무 자주 답변을 입력했습니다. 조금만 기다렸다가 다시 입력해주세요.")
        

if __name__ == "__main__":
    chat_app = ChatApp()
    end_phrases =["그만", "그만 할래", "Bye", "Quit", "Exit", "bye", "quit", "exit"]
    while True:
        msg = input()
        if msg in end_phrases:
            print("끝말잇기 게임을 종료합니다.")
            break
        chat_app.chat(msg)