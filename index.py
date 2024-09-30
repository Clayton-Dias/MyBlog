# Importação do Flask: Aqui estamos importando a classe Flask do pacote Flask, que é um microframework para construção de aplicações web em Python.
from flask import Flask, render_template
from flask_mysqldb import MySQL, MySQLdb

# Constantes do site
SITE = {
    "NAME": "MyBlog",
    "OWNER": "Meu Blog",
    "LOGO": "/static/img/icone.png",   
}


# Inicialização da aplicação: Criamos uma instância da classe Flask. O argumento __name__ ajuda o Flask a determinar o caminho da aplicação e a localizar recursos como templates e arquivos estáticos.
app = Flask(__name__)

# Configurações de acesso ao MySQL
'''
app.config['MYSQL_HOST'] = 'localhost'  # Servidor do MySQL
app.config['MYSQL_USER'] = 'root'       # Usuário do MySQL
app.config['MYSQL_PASSWORD'] = ''       # Senha do MySQL
app.config['MYSQL_DB'] = 'myblogdb'     # Nome da base de dados
'''
app.config.update(
    MYSQL_HOST='localhost',       # Servidor do MySQL
    MYSQL_USER='root',            # Usuário do MySQL
    MYSQL_PASSWORD='',            # Senha do MySQL
    MYSQL_DB='myblogdb'           # Nome da base de dados
)

# Variável de conexão com o MySQL
mysql = MySQL(app)


# @ -> anotation
# Definição de rota: O decorador @app.route('/') define uma rota para a URL raiz (/). A função home() será chamada quando alguém acessar essa URL.

# Rota para a página inicial → raiz
@app.route('/')
def home():

    # Consulta SQL
    sql = '''
        -- Seleciona os campos art_id, art_title, art_resume e art_thumbnail da tabela article
        SELECT art_id, art_title, art_resume, art_thumbnail

        -- Define a tabela de onde os dados serão extraídos
        FROM article

        -- Filtra os resultados para incluir apenas artigos que estão "on" (ativos) e cuja data é anterior ou igual à data atual
        WHERE art_status = 'on'  -- Verifica se o status do artigo é 'on'
        AND art_date <= NOW()    -- Compara a data do artigo com a data e hora atuais

        -- Ordena os resultados pela data do artigo em ordem decrescente (do mais recente para o mais antigo)
        ORDER BY art_date DESC;
    '''

    # Executa a query e obtém os dados na forma de DICT
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    articles = cur.fetchall()
    cur.close()

    # Somente para debug
    # Funciona somente quando a route para a raiz for acionada
    # print('\n\n\n', articles, '\n\n\n')

    # Passa parâmetros para o template
    # "CSS" e "JS" são opcionais
    toPage = {
        "site": SITE,
        'title': 'Página Inical ',   # Título da página → <title></title>
        "css": "home.css",          # Folhas de estilo desta página (opcional)
        "js": "home.js",            # JavaScript desta página (opcional)

        # Outras chaves usadas pela página
        'articles': articles
    }
    # Renderiza template passando a variável local `toPage`
    # para o template como `page`.
    return render_template("home.html", page=toPage)


@app.route('/view/<artid>')
def view(artid):

    if not artid.isdigit():
        return page_not_found(404)

    sql = '''
        SELECT art_id, art_date, art_title, art_content,

        -- Obtém a data em PT_BR pelo pseudo-campo 'art_datebr'
        DATE_FORMAT(art_date, '%%d/%%m/%%Y às %%H:%%i') AS art_datebr,
        sta_id, sta_name, sta_image, sta_description,

        -- Calcula a idade para 'sta_age' considerando ano, mês e dia de nascimento
        TIMESTAMPDIFF(YEAR, sta_birth, CURDATE()) - 
        (DATE_FORMAT(CURDATE(), '%%m%%d') < DATE_FORMAT(sta_birth, '%%m%%d')) AS sta_age
        
        FROM article 

        -- Realiza um INNER JOIN entre a tabela article e a tabela staff
        INNER JOIN staff ON art_author = sta_id
        WHERE art_id = %s  -- Filtra para obter apenas o artigo com ID específico
            AND art_status = 'on'  -- Considera apenas artigos que estão ativos
            AND art_date <= NOW();  -- Inclui apenas artigos cuja data é menor ou igual à data atual

    '''
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (artid,))
    article = cur.fetchone()

    # Para debug
    # print('\n\n\n', article, '\n\n\n')

    if article is None:
        return page_not_found(404)
    
    sql = 'UPDATE article SET art_view = art_view +1  WHERE art_id = %s'
    cur.execute(sql, (artid,))
    mysql.connection.commit()


    toPage={
        'site' : SITE,
        'title': article["art_title"],
        'css':'view.css',
        'article': article
    }

    cur.close()
    return render_template("view.html", page=toPage)


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


@app.errorhandler(404)
def page_not_found(e):
    toPage = {
        'title': 'Erro 404',
        'site': SITE,
        'css': '404.css'
    }
    return render_template('404.html', page=toPage), 404


# Verificação de execução: Este bloco garante que o código dentro dele só será executado se o script for executado diretamente, e não se for importado como um módulo em outro script.
if __name__ == '__main__':
    app.run(debug=True)  # Execução da aplicação: Aqui, chamamos o método run() da instância app para iniciar o servidor web. O parâmetro debug=True ativa o modo de depuração, o que significa que a aplicação será recarregada automaticamente quando alterações forem feitas no código, e erros serão exibidos de forma mais detalhada.
