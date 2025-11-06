from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grafico/<nome>')
def grafico(nome):
    return render_template(f'iframes/{nome}.html')

# Exporte o app como "handler" para a Vercel
def handler(event, context):
    return app(event, context)
