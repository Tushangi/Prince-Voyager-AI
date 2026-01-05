from flask import Flask, request, jsonify, send_from_directory
from intents import intents
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

FRONTEND_DIR = "Frontend"


# ===================== TEXT NORMALIZATION =====================
def normalize_text(text):
    text = text.lower()
    text = text.replace("_", " ")
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ===================== INTENT MATCHING =====================
def get_response(user_msg):
    user_msg = normalize_text(user_msg)

    # -------------------------------------------------
    # 1️⃣ EXACT MATCH (TOP PRIORITY – FIXES "book cab")
    # -------------------------------------------------
    for key, intent in intents.items():
        if key == "fallback":
            continue

        for pattern in intent["patterns"]:
            if normalize_text(pattern) == user_msg:
                return intent["response"]

    # -------------------------------------------------
    # 2️⃣ WORD-LEVEL MATCHING
    # -------------------------------------------------
    user_words = set(user_msg.split())
    best_match = None
    best_ratio = 0

    for key, intent in intents.items():
        if key == "fallback":
            continue

        for pattern in intent["patterns"]:
            pattern_words = set(normalize_text(pattern).split())
            if not pattern_words:
                continue

            common = user_words & pattern_words
            ratio = len(common) / len(pattern_words)

            if ratio > best_ratio:
                best_ratio = ratio
                best_match = intent["response"]

    # -------------------------------------------------
    # 3️⃣ CONFIDENCE CHECK
    # -------------------------------------------------
    if best_match and best_ratio >= 0.5:
        return best_match

    # -------------------------------------------------
    # 4️⃣ FALLBACK RESPONSE
    # -------------------------------------------------
    return intents["fallback"]["response"]


# ===================== ROUTES =====================
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message found"}), 400

    response = get_response(data["message"])
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
