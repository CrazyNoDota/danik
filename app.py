from flask import Flask, render_template, request
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API credentials from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define system message (optional)
system_message = {"role": "system", "content": "You are a helpful assistant."}

# Define home page route
@app.route("/")
def home():
    return render_template("index.html")

# Route to serve files.html
@app.route("/files.html")
def serve_files_html():
    return render_template('files.html')

# Route to generate text based on user input
@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]

    try:
        # Correct API call for the chat model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.9
        )

        # Accessing the response correctly
        text = response['choices'][0]['message']['content'].strip()

    except Exception as e:
        # Handle any API or response parsing errors
        text = f"An error occurred: {str(e)}"

    return render_template("generated_text.html", text=text)

# Main entry point for the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
