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
    input = data["input"]
    key = data["key"]
    m = data["method"]

    if data["input"] == "" or data["key"] == "":
        return jsonify({"error": "please enter a valid text/key"}), 400

    method = CIPHERS[m]

    try:
        if mode == "encrypt":
            return jsonify({"result": method.encrypt(input, key)})
        elif mode == "decrypt":
            return jsonify({"result": method.decrypt(input, key)})
         
    except ValueError:
        return jsonify({"error": "invalid key for cipher"}), 400

    
if __name__ == "__main__":
    app.run()
