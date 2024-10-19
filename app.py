import wave
import struct
import os
from openai import OpenAI
from flask import Flask, render_template, request
from openai import Image


# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

class Chatbot:
    def __init__(self, client):
        self.client = client
        self.context = [
            {
                "role": "system",
                "content": "Answer like an intelligent proffessor, answer from science perspective"
            }
        ]

    def chat(self, message):
        self.context.append({"role": "user", "content": message})
        
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=self.context
        )
        
        response_content = response.choices[0].message.content
        self.context.append({"role": "assistant", "content": response_content})
        return response_content  # Return the assistant's response

    def print_chat(self):
        # Return the last assistant message
        for message in reversed(self.context):
            if message["role"] == "assistant":
                return f'BOT: {message["content"]}'
        return ''

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
    generated_text = chatbot.chat(prompt)
    return render_template("generated_text.html", text=generated_text)

@app.route("/generate_image", methods=["POST"])
def generate_image():
    prompt = request.form["prompt"]
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
   
    return render_template("image.html", image_url=image_url)
    



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
