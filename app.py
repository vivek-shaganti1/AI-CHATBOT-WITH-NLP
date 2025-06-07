from flask import Flask, render_template, request, jsonify
import cohere

app = Flask(__name__)
co = cohere.Client('n0ftzqxavMn0ANrdzrvQZU5mqulwzjS00BZ8zCqx')  # Your Cohere API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': 'Please say something!'}), 400

    prompt = f"Human: {user_message}\nAI:"
    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0
    )
    bot_reply = response.generations[0].text.strip()
    return jsonify({'response': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
