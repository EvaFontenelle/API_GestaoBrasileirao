from flask import Flask, jsonify
from conectar.funcaoConectar import conectar

from endpoints.SerieA import SerieA_bp
from endpoints.SerieB import SerieB_bp
from endpoints.SerieC import SerieC_bp
from endpoints.SerieD import SerieD_bp

app = Flask(__name__)
app.register_blueprint(SerieA_bp)
app.register_blueprint(SerieB_bp)
app.register_blueprint(SerieC_bp)
app.register_blueprint(SerieD_bp)

@app.route('/')
def raiz():
    return jsonify({"status": "API principal Flask funcionando!"})

if __name__ == "__main__":
    app.run(debug=True)