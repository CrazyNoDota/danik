from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'sk-WRJBKQkTAYIk4gSJRAy971h2EteV_YX8XZe_K3PL6iT3BlbkFJPnUlwGUaoEnHj_HWmEMh3rsgUA_-xqnugZWiI3KHgA'  # Replace 'your-api-key-here' with your actual API key

kazakh = False

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
    
    # Build messages list based on the 'kazakh' variable
    if kazakh:
        system_message = {"role": "system", "content": "You are an assistant that communicates in Kazakh language."}
    else:
        system_message = {"role": "system", "content": "You are an assistant that communicates in English language."}
    
    # Use the new ChatCompletion method with updated API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            system_message,
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        n=1,
        temperature=0.9,
    )
   
    text = response['choices'][0]['message']['content'].strip()
    return render_template("generated_text.html", text=text)


@app.route('/update_bool', methods=['POST'])
def update_bool():
    global kazakh
    kazakh = not kazakh
    if kazakh == False:
        return 'Language set to English. Please return.'
    else:
        return 'Language changed to Kazakh. Please return.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
