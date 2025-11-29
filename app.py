from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/grafico/<nome>')
def grafico(nome):
    return render_template(f'iframes/{nome}.html')

if __name__ == '__main__':
    app.run(debug=True)