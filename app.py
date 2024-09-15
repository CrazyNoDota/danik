from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key='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')
import os

app = Flask(__name__)

# Set up OpenAI API credentials
  # Replace 'your-api-key-here' with your actual API key

# Define system message (optional)
system_message = {"role": "system", "content": "You are a helpful assistant."}

# Define home page route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/files.html")
def serve_files_html():
    return render_template('files.html')

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]

    # Correct API call with the system message
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        system_message,  # You can modify this message or remove it if not needed
        {"role": "user", "content": prompt}
    ],
    max_tokens=1024,
    temperature=0.9)

    # Accessing the response in the new structure
    text = response.choices[0].message.content.strip()
    return render_template("generated_text.html", text=text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
