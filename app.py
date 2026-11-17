from flask import Flask, jsonify, request, send_file

app = Flask(__name__, static_folder="static")

FAQ = {
    "membership fee": {
        "answer": "Membership fees depend on the member type. Standard adult memberships are $25 per month, while student and family plans are discounted.",
        "source": "Membership FAQ — 'Standard adult memberships are $25 per month, while student and family plans are discounted.'"
    },
    "membership fees": {
        "answer": "Membership fees depend on the member type. Standard adult memberships are $25 per month, while student and family plans are discounted.",
        "source": "Membership FAQ — 'Standard adult memberships are $25 per month, while student and family plans are discounted.'"
    },
    "fees": {
        "answer": "Membership fees depend on the member type. Standard adult memberships are $25 per month, while student and family plans are discounted.",
        "source": "Membership FAQ — 'Standard adult memberships are $25 per month, while student and family plans are discounted.'"
    },
    "benefits": {
        "answer": "Members receive access to events, member-only resources, and priority registration for workshops and classes.",
        "source": "Membership FAQ — 'Members receive access to events, member-only resources, and priority registration for workshops and classes.'"
    },
    "renew": {
        "answer": "Memberships renew automatically each month unless you cancel at least 7 days before the renewal date.",
        "source": "Membership FAQ — 'Memberships renew automatically each month unless you cancel at least 7 days before the renewal date.'"
    }
}


@app.route("/")
def index():
    return send_file("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Please enter a question before submitting."}), 400

    normalized = question.lower()
    for keyword, response in FAQ.items():
        if keyword in normalized:
            return jsonify(response)

    return jsonify({"error": "I couldn't find an answer to that question in the membership FAQ."}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
