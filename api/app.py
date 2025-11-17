from flask import Flask, render_template
import os

# Corrige caminhos caso o arquivo esteja dentro de /api
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(BASE_DIR, "../templates")
STATIC = os.path.join(BASE_DIR, "../static")

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grafico/<nome>')
def grafico(nome):
    return render_template(f'iframes/{nome}.html')

# Só roda localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
