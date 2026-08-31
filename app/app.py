from flask import Flask, jsonify

app = Flask(_name_)


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
        "ambiente": "producao"
    })


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
