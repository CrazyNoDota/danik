from flask import Flask, render_template, request
import openai

# Initialize the Flask app
app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

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
        
        response = self.client.Completion.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        
        response_content = response.choices[0].message.content
        self.context.append(
            {"role": "assistant", "content": response_content}
        )
        return response_content

# Initialize the chatbot instance
chatbot = Chatbot(openai)

# Define home page route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/files.html")
def serve_files_html():
    return render_template('files.html')

# Define route for generating text using Chatbot
@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]
    
    # Use the chatbot to generate a response
    text = chatbot.chat(prompt)
    
    return render_template("generated_text.html", text=text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
