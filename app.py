from flask import Flask, render_template, request
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API credentials from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define system message (optional)
system_message = "You are a helpful assistant."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/files.html")
def serve_files_html():
    return render_template('files.html')

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]

    try:
        # Correct API call using the new OpenAI library interface
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo" if you're using the 3.5 model
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.9
        )

        # Extract the generated text from the response
        text = response['choices'][0]['message']['content'].strip()

    except Exception as e:
        # Handle any errors that occur during the API call
        text = f"An error occurred: {str(e)}"

    return render_template("generated_text.html", text=text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
