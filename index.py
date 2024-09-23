from flask import Flask, render_template
# Importação do Flask: Aqui estamos importando a classe Flask do pacote Flask, que é um microframework para construção de aplicações web em Python.

app = Flask(__name__)
# Inicialização da aplicação: Criamos uma instância da classe Flask. O argumento __name__ ajuda o Flask a determinar o caminho da aplicação e a localizar recursos como templates e arquivos estáticos.

# @ -> anotation

# Definição de rota: O decorador @app.route('/') define uma rota para a URL raiz (/). A função home() será chamada quando alguém acessar essa URL.

#Rotaa para a ágina inicial
@app.route('/')
def home():
    # Passa parâmetros para o template
    # "CSS" e "JS" são opcionais
    page = {
        'title': 'Página Inical',
        "css":"home.css",
        "js": "home.js",
        "content": "Hello World! (com Flask)",
        "img": {
            "url": "https://picsum.photos/id/1/200/300",
            "alt": "Imagem Aleatória",
        }        
    }    
    return render_template("home.html", page=page)

@app.route('/contacts')
def contacts():
    page = {
        'title': 'Faça contatos',
        "css":"home.css",
        "img": {
            "url": "https://picsum.photos/id/1/200/300",
            "alt": "Imagem Aleatória",
        } 
                
    }
    return render_template("contacts.html",page=page)


# Verificação de execução: Este bloco garante que o código dentro dele só será executado se o script for executado diretamente, e não se for importado como um módulo em outro script.
if __name__ == '__main__':
    app.run(debug=True)  # Execução da aplicação: Aqui, chamamos o método run() da instância app para iniciar o servidor web. O parâmetro debug=True ativa o modo de depuração, o que significa que a aplicação será recarregada automaticamente quando alterações forem feitas no código, e erros serão exibidos de forma mais detalhada.
