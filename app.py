import wave, struct, os
from openai import OpenAI
client = OpenAI(api_key="sk-TDpzrP8LTYBD5AOVOQtS_BAc_2ipjjOGhHkjJUQsfDT3BlbkFJUbJODhBEsI269PlgbBbu4n3nh7tHPXQDcmGx_TzbAA")
class Chatbot:
    def __init__(self, client):
        self.client = client
        self.context = [
            {"role": "system", "content": "You are a witty assistant, always answering with a joke."}
        ]

    def chat(self, message):
        self.context.append(
            {"role": "user", "content": message}
        )
        
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=self.context
        )
        
        response_content = response.choices[0].message.content
        self.context.append(
            {"role": "assistant", "content": response_content}
        )
        self.print_chat()

    def print_chat(self):
        for message in self.context:
            if message["role"] == "user":
                print(f'USER: {message["content"]}')
            elif message["role"] == "assistant":
                print(f'BOT: {message["content"]}')


chatbot = Chatbot(client)
chatbot.chat("Hello. Who are you?")
