from flask import Flask, render_template
# Importação do Flask: Aqui estamos importando a classe Flask do pacote Flask, que é um microframework para construção de aplicações web em Python.

# Constantes do site
SITE ={
    "NAME" : "MyBlog",
    "OWNER" : "Meu Blog",
    "LOGO": "/static/img/icone.png",
}

app = Flask(__name__)
# Inicialização da aplicação: Criamos uma instância da classe Flask. O argumento __name__ ajuda o Flask a determinar o caminho da aplicação e a localizar recursos como templates e arquivos estáticos.

# @ -> anotation

# Definição de rota: O decorador @app.route('/') define uma rota para a URL raiz (/). A função home() será chamada quando alguém acessar essa URL.

# Rota para a página inicial → raiz
@app.route('/')
def home():
    # Passa parâmetros para o template
    # "CSS" e "JS" são opcionais
    toPage = {
        "site": SITE,
        'title': 'Página Inical ',   # Título da página → <title></title>
        "css": "home.css",          # Folhas de estilo desta página (opcional)
        "js": "home.js",            # JavaScript desta página (opcional)

        # Outras chaves usadas pela página

    }
    # Renderiza template passando a variável local `toPage`
    # para o template como `page`.
    return render_template("home.html", page=toPage)

# Rota para a página dec contatos → /contacts
@app.route('/contacts')
def contacts():
    page = {
        "site": SITE,
        "title": "Faça contatos",        
        "css": "home.css",
    }
    return render_template("contacts.html", page=page)


# Rota para a página de sobre (quem somos) → /about
@app.route('/about')
def about():
    page = {
        "site": SITE,
        "title": "Sobre",       
        "css": "about.css"
    }
    return render_template("about.html", page=page)


# Verificação de execução: Este bloco garante que o código dentro dele só será executado se o script for executado diretamente, e não se for importado como um módulo em outro script.
if __name__ == '__main__':
    app.run(debug=True)  # Execução da aplicação: Aqui, chamamos o método run() da instância app para iniciar o servidor web. O parâmetro debug=True ativa o modo de depuração, o que significa que a aplicação será recarregada automaticamente quando alterações forem feitas no código, e erros serão exibidos de forma mais detalhada.
