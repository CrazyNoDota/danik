from flask import Flask, render_template, request
import openai
import os
#oasidfoasidj
app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

# Define home page route
@app.route("/")
def home():
    return render_template("index.html")

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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

