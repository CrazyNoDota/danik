from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'  # Replace 'your-api-key-here' with your actual API key

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
