# Importação do Flask: Aqui estamos importando a classe Flask do pacote Flask, que é um microframework para construção de aplicações web em Python.
from flask import Flask, redirect, render_template, request, url_for
#from flask_mail import Mail, Message
from flask_mysqldb import MySQL, MySQLdb

from dotenv import load_dotenv  # Importa a função load_dotenv da biblioteca dotenv
import os  # Importa o módulo os, que fornece uma maneira de interagir com o sistema operacional


# Importar as funções do banco de dados, tabela article
from functions.db_articles import *

# Importar as funções do banco de dados, tabela comment
from functions.db_comments import *

from functions.db_contacts import *


load_dotenv()

# Constantes do site
SITE = {
    "NAME": "MyBlog",
    "OWNER": "Meu Blog",
    "LOGO": "/static/img/icone.png",   
}

#Lista de redes sociais
SOCIAL = (
    {
        'name': 'Facebook',
        'link': 'https://facebook.com',
        'icon': '<i class="fa-brands fa-square-facebook fa-fw"></i>'
    },
    {
        'name': 'Linkedin',
        'link': 'https://linkedin.com/',
        'icon': '<i class="fa-brands fa-linkedin fa-fw"></i>'
    },
    {
        'name': 'Youtube',
        'link': 'https://youtube.com/',
        'icon': '<i class="fa-brands fa-square-youtube fa-fw"></i>'
    }, {
        'name': 'GitHub',
        'link': 'https://github.com/',
        'icon': '<i class="fa-brands fa-square-github fa-fw"></i>'
    },
)

# Inicialização da aplicação: Criamos uma instância da classe Flask. O argumento __name__ ajuda o Flask a determinar o caminho da aplicação e a localizar recursos como templates e arquivos estáticos.
app = Flask(__name__)




# Configurações de acesso ao MySQL
app.config.update(
    MYSQL_HOST=os.getenv('MYSQL_HOST'),         # Servidor do MySQL
    MYSQL_USER=os.getenv('MYSQL_USER'),         # Usuário do MySQL
    MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD'), # Senha do MySQL
    MYSQL_DB=os.getenv('MYSQL_DB')              # Nome da base de dados
)

# Variável de conexão com o MySQL
mysql = MySQL(app)

'''
# Configurações do servidor de e-mail
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'luferatinho@outlook.com'
app.config['MAIL_PASSWORD'] = 'Senha123456'

# Objeto de envio de e-mails
mail = Mail(app)
'''

# @ -> anotation
# Definição de rota: O decorador @app.route('/') define uma rota para a URL raiz (/). A função home() será chamada quando alguém acessar essa URL.

# Rota para a página inicial → raiz
@app.route('/')
def home():

    # Obtém todos os artigos
    articles = get_all(mysql)

    # Obtém artigos mais comentados
    commenteds = most_commented(mysql)

    # Obtém artigos mais vistos(visualizados)
    views = most_view(mysql)

    # Somente para debug
    # Funciona somente quando a route para a raiz for acionada
    # print('\n\n\n', articles, '\n\n\n')

    # Parâmetros a serem passados para o template
    # "CSS" e "JS" são opcionais
    toPage = {
        "site": SITE,
        'title': 'Página Inical ',   # Título da página → <title></title>
        "css": "home.css",          # Folhas de estilo desta página (opcional)
        "js": "home.js",            # JavaScript desta página (opcional)

        # Outras chaves usadas pela página
        'articles': articles,
        
        'commenteds': commenteds,

        'views': views
    }
    # Renderiza template passando a variável local `toPage`
    # para o template como `page`.
    return render_template("home.html", page=toPage)


# Rota para visualizar um artigo específico
@app.route('/view/<artid>')
def view(artid):

    # Se o ID(artid) do artigo não é um número, direcionar para 404
    if not artid.isdigit():
        return page_not_found(404)
    
    # Obtém o artigo pelo ID
    article = get_one(mysql, artid) 


    # Para debug
    # print('\n\n\n', article, '\n\n\n')

    # Se o artigo não existe ou está disponível, direcionar para 404
    if article is None:
        return page_not_found(404)
    
    # Atualiza as visualizações do artigo
    update_views(mysql, artid)


    # Traduz o "type" do author
    '''
    if article['sta_type'] == 'admin':
        article['sta_pt_type'] = 'Administrador(a)'
    elif article['sta_type'] == 'author':
        article['sta_pt_type'] = "Autor(a)"
    else:
        article['sta_pt-type'] = "Moderador(a)" 
    '''    
    # Tradução do tipo de autor
    type_translation = {
        'admin': 'Administrador(a)',
        'author': 'Autor(a)',
        'moderator': 'Moderador(a)'
    }
    article['sta_pt_type'] = type_translation.get(article['sta_type'], 'Desconhecido')
    
    # Obtém mais artigos do autor
    articles = get_plus(mysql, article['sta_id'], article['art_id'], 4)

    
    # Obtém somente o primeiro nome do autor
    article['sta_first'] = article['sta_name'].split()[0]


    # Obtém todos os comentários do artigo atual
    comments = get_comments(mysql, article['art_id'])

    # Para debug
    #print('\n\n\n', comments, '\n\n\n')


    # Total de comentários
    total_comments = len(comments)

    toPage={
        'site' : SITE,
        'title': article["art_title"],
        'css':'view.css',
        'js':'view.js',
        'article': article,
        'articles': articles,
        'total_comments': total_comments,
        'comments': comments
    }

    return render_template("view.html", page=toPage)



@app.route('/comment', methods=['POST'])
def comment():

    # Obtém dados do formulario
    form = request.form

    # Se o form está vazio
    if form['name'] != None and form['name'] != '' and form['email'] != None and form['email'] != '':
    
        # Salva o comentário no banco de dados
        save_comment(mysql, form)
    
    return redirect(f"{url_for('view', artid=form['artid'])}#comments")


# Rota para a página dec contatos → /contacts
@app.route('/contacts', methods = ['GET', 'POST'])
def contacts():

    # Formulário enviado com sucesso
    success = False

    # Primeiro nome do remetente
    first_name = ''

    # Se o formulário foi enviado...
    if request.method == 'POST':
        # Obtém dados do formulario
        form = dict(request.form)
        
        # Salva os dados no banco de dados 
        success = save_contact(mysql, form)

        # Otém o primeiro nome do remetente
        first_name = form['name'].split()[0]

        '''
        # Envia e-mail para o admin
        msg = Message(
            subject=form['subject'],
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body= f'Foi enviado um contato para JocaBlog:\n\n{form['message']}'
        )
        mail.send(msg)
        '''

    page = {
        "site": SITE,
        "title": "Faça contatos",
        "css": "contacts.css",
        "js":'contacts.js',
        "success": success,
        "first_name": first_name,
        'social': SOCIAL
    }

    return render_template("contacts.html", page=page) # Renderiza a página de contatos
 
# Rota para o perfil do usuário
@app.route('/profile')
def profile():
    toPage = {
        'site': SITE,
        'title': 'Pefil do usuário',
        'css': 'profile.css',
        'js': 'profile.js'
    }

    return render_template('profile.html', page=toPage) # Renderiza a página de perfil


# Rota para a página de sobre (quem somos) → /about
@app.route('/about')
def about():
    page = {
        "site": SITE,
        "title": "Sobre",
        "css": "about.css"       
    }
    return render_template("about.html", page=page) # Renderiza a página sobre
 
# Manipulador de erro 404
@app.errorhandler(404)
def page_not_found(e):
    toPage = {
        'title': 'Erro 404',
        'site': SITE,
        'css': '404.css'
    }
    return render_template('404.html', page=toPage), 404 # Renderiza a página 404


# Manipulador de erro 405
@app.errorhandler(405)
def page_not_found(e):
    toPage = {
        'title': 'Erro 405',
        'site': SITE,
        'css': '405.css'
    }
    #return render_template('405.html', page=toPage), 405
    return 'Errou'


# Define a rota para a busca de artigos
@app.route('/search')  
def search():
    # Obtém o parâmetro de consulta 'q' da URL
    query = request.args.get('q')

    # Chama a função article_search para buscar os artigos que correspondem à consulta
    articles = article_search(mysql, query)

    # Calcula o total de artigos encontrados
    total = len(articles)

    # Obtém os 5 artigos mais recentes
    recents = get_all(mysql, 5)
    
    # Cria um dicionário com os dados da página
    page = {
        'title': 'Pesquisa',  # Título da página
        'site': SITE,        # Nome do site
        'css': 'home.css',   # Arquivo CSS para estilização
        'articles': articles, # Lista de artigos encontrados
        'total': total,      # Total de artigos encontrados
        'query': query,      # Consulta realizada
        'recents': recents   # Artigos mais recentes
    }

    # Renderiza o template 'search.html' com os dados da página
    return render_template('search.html', page=page)


# Define a rota para a política de privacidade
@app.route("/policies")  
def policies():
    # Cria um dicionário com os dados da página
    page = {
        "site": SITE,                # Nome do site
        "title": "Política de Privacidade",  # Título da página
        "css": "policies.css",       # Arquivo CSS para estilização
    }
    
    # Renderiza o template 'policies.html' com os dados da página
    return render_template("policies.html", page=page)


# Verificação de execução: Este bloco garante que o código dentro dele só será executado se o script for executado diretamente, e não se for importado como um módulo em outro script.
if __name__ == '__main__':
    app.run(debug=True)  # Execução da aplicação: Aqui, chamamos o método run() da instância app para iniciar o servidor web. O parâmetro debug=True ativa o modo de depuração, o que significa que a aplicação será recarregada automaticamente quando alterações forem feitas no código, e erros serão exibidos de forma mais detalhada.
