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
            max_tokens=50,
            temperature=0.9
        )

        # Accessing the response correctly
        text = response['choices'][0]['message']['content'].strip()

    except Exception as e:
        # Handle any API or response parsing errors
        text = f"An error occurred: {str(e)}"

    return render_template("generated_text.html", text=text)
