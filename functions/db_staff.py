from flask_mysqldb import MySQL, MySQLdb


def get_staff(mysql):

    sql = '''
        SELECT 
            sta_id,  -- Seleciona o ID único do membro da equipe
            sta_name,  -- Seleciona o nome do membro da equipe
            sta_email,  -- Seleciona o email do membro da equipe
            sta_birth,  -- Seleciona a data de nascimento do membro da equipe
            sta_image,  -- Seleciona a URL da imagem do membro da equipe
            sta_description,  -- Seleciona a descrição do membro da equipe
            sta_type,  -- Seleciona o tipo do membro (admin, moderator, author)
            
            -- Usando CASE para definir a prioridade do tipo de membro
            CASE 
                WHEN sta_type = 'admin' THEN 1  -- Prioridade 1 para 'admin'
                WHEN sta_type = 'moderator' THEN 2  -- Prioridade 2 para 'moderator'
                WHEN sta_type = 'author' THEN 3  -- Prioridade 3 para 'author'
                ELSE 4  -- Qualquer outro tipo terá prioridade 4
            END AS type_priority  -- Define o resultado do CASE como a coluna 'type_priority'
    
        FROM staff  -- Seleciona os dados da tabela 'staff'
        WHERE sta_status = 'on'  -- Filtra para incluir apenas membros ativos (status 'on')
        ORDER BY type_priority;  -- Ordena os resultados pela prioridade do tipo (do mais alto para o mais baixo)
        '''
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    staff = cur.fetchall()
    cur.close()

    return staff