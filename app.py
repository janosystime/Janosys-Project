from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grafico/<nome>')
def grafico(nome):
    return render_template(f'iframes/{nome}.html')

if __name__ == '__main__':
    # Executa localmente com livereload apenas se estiver em desenvolvimento
    if os.environ.get('FLASK_ENV') == 'development':
        from livereload import Server
        server = Server(app.wsgi_app)
        server.watch('templates/*.*')
        server.watch('static/*.*')
        server.serve(host='0.0.0.0', port=5000, debug=True)
    else:
        # Modo produção padrão (para Vercel)
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
