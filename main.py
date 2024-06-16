import os

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def index():
    theme_color = request.cookies.get('theme', 'light') 
    post_items = [(x, "Nome do Criador", "Titulo do post", "Conteudo do meu post é esse.") for x in range(0, 5)]
    return render_template('index.html', post_items=post_items, theme_color=theme_color)

@app.route('/set_theme/<theme>')
def set_theme(theme):
    # Defina um cookie para armazenar a preferência de tema do usuário
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('theme', theme)
    return resp

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
