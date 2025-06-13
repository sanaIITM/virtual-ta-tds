import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Virtual TA is live! Use POST /api/ to ask questions."

@app.route("/api/", methods=["POST"])
def answer_question():
    data = request.get_json()
    question = data.get("question", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful TA for the Tools in Data Science course (TDS Jan 2025). Answer student questions using course materials and previous discussions."
                },
                {"role": "user", "content": question}
            ]
        )

        return jsonify({
            "answer": response["choices"][0]["message"]["content"].strip(),
            "links": []
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

