import wave, struct, os
from openai import OpenAI
from flask import Flask, render_template, request
client = OpenAI(api_key="sk-TDpzrP8LTYBD5AOVOQtS_BAc_2ipjjOGhHkjJUQsfDT3BlbkFJUbJODhBEsI269PlgbBbu4n3nh7tHPXQDcmGx_TzbAA")

app = Flask(__name__)
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
                return(f'USER: {message["content"]}')
            elif message["role"] == "assistant":
                return(f'BOT: {message["content"]}')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/files.html")
def serve_files_html():
    return render_template('files.html')
# Define route for generating text
@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]
    chatbot = Chatbot(client)
    return render_template("generated_text.html", text=chatbot.chat(prompt))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)


