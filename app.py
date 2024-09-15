from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'  # Replace 'your-api-key-here' with your actual API key



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
    
    # Correct API call with updated structure
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            system_message,
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.9,
    )
   
    # Accessing the response in the new structure
    text = response['choices'][0]['message']['content'].strip()
    return render_template("generated_text.html", text=text)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
