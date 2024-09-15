from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    
    # Updated API call to the new chat_completions method
    response = openai.chat_completions.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" depending on your access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,
        n=1,
        temperature=0.9,
    )
    
    # Extracting the response text
    text = response.choices[0].message['content'].strip()
    return render_template("generated_text.html", text=text)

@app.route('/update_bool', methods=['POST'])
def update_bool():
    global kazakh
    kazakh = not kazakh
    if kazakh == False:
        return 'Language set to English. Please return.'
    else:
        return 'The language changed to Kazakh. Please return.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
