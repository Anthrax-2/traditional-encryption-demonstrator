from flask import Flask, render_template, request, jsonify
from ciphers import CIPHERS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", ciphers=CIPHERS)


@app.route("/api/process", methods=["POST"])
def process():
    
    data = request.get_json()

    mode = data["mode"]
    text = data["text"]
    key = data["key"]
    m = data["method"]

    if m in CIPHERS:
        method = CIPHERS[m]
    else:
        return jsonify({"error": "invalid value for method"}), 400


    try:
        if mode == "encrypt":
            return jsonify({"result": method.encrypt(text, key)})
        elif mode == "decrypt":
            return jsonify({"result": method.decrypt(text, key)})
        else:
            return jsonify({"error": "invalid value for mode"}), 400  
    except ValueError:
        return jsonify({"error": "invalid key for cipher"}), 400

    
if __name__ == "__main__":
    app.run()
