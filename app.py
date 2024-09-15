from flask import Flask, render_template, request
import openai

import time

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

kazakh = False

# Define home page route
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
    
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.9,
    )
   
    text = response.choices[0].text.strip()
    return render_template("generated_text.html", text=text)

@app.route('/update_bool', methods=['POST'])
def update_bool():
    global kazakh
    kazakh = not kazakh
    if kazakh == False:
        return 'language set to english plase return'
    else:
        return 'The language changed to kazakh please return'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
