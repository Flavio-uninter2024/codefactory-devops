from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "projeto": "CodeFactory DevOps",
        "mensagem": "Aplicação funcionando!",
        "status": "online"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/info")
def info():
    return jsonify({
        "aplicacao": "CodeFactory DevOps",
        "versao": "1.0",
        "ambiente": "desenvolvimento"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)