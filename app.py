from flask import Flask, render_template, request, jsonify
from query_engine import ask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "").strip()
    if not question:
        return jsonify({"error": "Empty message"}), 400
    try:
        answer = ask(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Open http://localhost:8000")
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))