from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "E-Book DevOps System API running"
    })

@app.route("/books")
def books():
    sample_books = [
        {"id":1,"title":"DevOps Handbook","author":"Gene Kim"},
        {"id":2,"title":"Python Crash Course","author":"Eric Matthes"}
    ]

    return jsonify(sample_books)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
