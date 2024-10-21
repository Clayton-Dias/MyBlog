from flask_mysqldb import MySQL, MySQLdb


def get_all(mysql, limit=0):  # Obtem todos os artigos na página inicial

    if limit == 0:
        subsql = ''
    else:
        subsql = f'LIMIT {limit}'

    # Consulta SQL
    sql = f'''
        -- Seleciona os campos art_id, art_title, art_resume e art_thumbnail da tabela article
        SELECT art_id, art_title, art_resume, art_thumbnail

        -- Define a tabela de onde os dados serão extraídos
        FROM article

        -- Filtra os resultados para incluir apenas artigos que estão "on" (ativos) e cuja data é anterior ou igual à data atual
        WHERE art_status = 'on'  -- Verifica se o status do artigo é 'on'
        AND art_date <= NOW()    -- Compara a data do artigo com a data e hora atuais

        -- Ordena os resultados pela data do artigo em ordem decrescente (do mais recente para o mais antigo)
        ORDER BY art_date DESC
         {subsql};
    '''

    # Executa a query e obtém os dados na forma de DICT
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    articles = cur.fetchall()
    cur.close()

    return articles


# Obtém um artigo pelo ID (artid)
def get_one(mysql, artid):

    sql = '''  
         SELECT

        -- Campo do artigo
        art_id, art_date, art_title, art_content,

        -- Obtém a data em PT_BR pelo pseudo-campo 'art_datebr'
        DATE_FORMAT(art_date, '%%d/%%m/%%Y às %%H:%%i') AS art_datebr,
        
        -- Campo do autor
        sta_id, sta_name, sta_image, sta_description, sta_type,

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
    cur.close()

    return article


def update_views(mysql, artid):  # Atualiza as visualizações do artigo

    sql = 'UPDATE article SET art_view = art_view +1  WHERE art_id = %s'
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (artid,))
    mysql.connection.commit()
    cur.close()

    return True


# Obtém mais artigos relacionados ao autor
def get_plus(mysql, staid, artid, limit):

    sql = '''
        -- Obter até 4 artigos(id, title, thumbnail) aleatórios do autor, com exceção do atual

        -- Obtém (id, title, thumbnail)
        SELECT art_id, art_title, art_thumbnail
        -- da tabela
        FROM article
        -- Do autor = ID, onde o status é 'on' , data de publicação é a presente ou anterior e não pode ser o artigo atualmente vizualiado
        WHERE art_author = %s AND art_status ='on' AND art_date <= NOW() AND art_id != %s
        -- Em ordem aleatória e limitado a 4 artigos
        ORDER BY RAND() LIMIT %s;
    '''

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (staid, artid, limit,))
    articles = cur.fetchall()
    cur.close()

    return articles



def article_search(mysql, query, limit=0):

    if limit == 0:
        subsql = ''
    else:
        subsql = f'LIMIT {limit}'
    
    sql = f'''
        SELECT art_id, art_title, art_resume, art_thumbnail
        FROM article 
        WHERE (
            art_title LIKE %s
            OR art_resume LIKE %s
            or art_content LIKE %s
        )
            AND art_status = 'on' 
            AND art_date <= NOW()
        ORDER BY art_date DESC
        {subsql};
        '''
    
    like_term = f'%{query}%'
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (like_term, like_term, like_term, ))
    articles = cur.fetchall()
    cur.close()

    return articles


def most_commented(mysql, limit=4):
    
    sql = '''
         -- Seleciona os campos e a contagem de comentários
        SELECT 
            a.art_id, 
            a.art_title,
            a.art_thumbnail,
            COUNT(c.com_id) AS comment_count
        FROM 
            article a
        
        -- Faz um LEFT JOIN com a tabela comment, contando apenas os comentários cujo com_status é 'on'    
        LEFT JOIN 
            comment c ON a.art_id = c.com_article AND c.com_status = 'on'
        
        -- Filtra os artigos para incluir apenas aqueles cujo art_status é 'on' e art_date é menor ou igual a NOW()
        WHERE 
            a.art_status = 'on' 
            AND a.art_date <= NOW()
       
        -- Agrupa os resultados por art_id, art_title    
        GROUP BY 
            a.art_id, a.art_title
        
        -- Filtra os grupos para incluir apenas aqueles com contagem de comentários maior que zero
        HAVING 
            comment_count > 0
        
        -- Ordena os resultados pela contagem de comentários em ordem decrescente
        ORDER BY 
            comment_count DESC
        
         -- Limita os resultados a # registros
        LIMIT %s;
    '''

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (limit,))
    most_comments = cur.fetchall()
    cur.close()

    return most_comments


def most_view(mysql, limit=4):
    
    sql ='''
        SELECT art_id, art_title, art_thumbnail

        FROM article

        WHERE art_status = 'on' AND art_date <= NOW()

        ORDER BY art_view DESC

        LIMIT %s;

    '''


    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (limit,))
    most_view = cur.fetchall()
    cur.close()

    return most_view