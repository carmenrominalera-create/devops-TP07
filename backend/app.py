from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "TP07 funcionando"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/db")
def db():
    return jsonify({
        "database": "connected"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
