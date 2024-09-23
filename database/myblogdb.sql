-- --------------------------- --
-- Banco de dados "myblogdb" --
-- --------------------------- --

-- Apaga o banco de dados caso ele já exista
-- PERIGO! Não faça isso em modo de produção
DROP DATABASE IF EXISTS myblogdb;

-- Cria o banco de dados
-- !!!!!!!!!!!!!!!!!!!!!! ATENÇÃO !!!!!!!!!!!!!!!!!!!
-- Remova este comando após a publicação da versão de produção
CREATE DATABASE myblogdb 
    CHARACTER SET utf8mb4  -- Usando o conjunto de caracteres UTF-8
    COLLATE utf8mb4_general_ci; -- Buscas em UTF-8 e case insensitive

-- Seleciona o banco de dados para os próximos comandos
USE myblogdb;

-- Cria a tabela "staff" para armazenar informações dos usuários do blog
CREATE TABLE staff(
    sta_id INT PRIMARY KEY AUTO_INCREMENT, -- ID único do staff
    sta_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação do registro
    sta_name VARCHAR(127) NOT NULL, -- Nome do staff
    sta_email VARCHAR(255) NOT NULL, -- Email do staff
    sta_password VARCHAR(63) NOT NULL, -- Senha do staff
    sta_birth DATE NOT NULL, -- Data de nascimento
    sta_description VARCHAR(255), -- Descrição do staff
    sta_type ENUM('moderator', 'author', 'admin') DEFAULT 'moderator', -- Tipo de usuário
    sta_status ENUM('on', 'off', 'del') DEFAULT 'on' -- Status do usuário
);

-- Cria a tabela "article" para armazenar os artigos do blog
CREATE TABLE article(
    art_id INT PRIMARY KEY AUTO_INCREMENT, -- ID único do artigo
    art_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação do artigo
    art_title VARCHAR(127) NOT NULL, -- Título do artigo
    art_resume VARCHAR(255) NOT NULL, -- Resumo do artigo
    art_thumbnail VARCHAR(255) NOT NULL, -- Thumbnail do artigo
    art_content TEXT NOT NULL, -- Conteúdo do artigo
    art_view INT DEFAULT 0, -- Contador de visualizações
    art_author INT, -- ID do autor (referência para staff)
    art_status ENUM('on', 'off', 'del') DEFAULT 'on', -- Status do artigo
    FOREIGN KEY (art_author) REFERENCES staff (sta_id) -- Chave estrangeira para staff
);

-- Cria a tabela "comment" para armazenar os comentários nos artigos
CREATE TABLE comment(
    com_id INT PRIMARY KEY AUTO_INCREMENT, -- ID único do comentário
    com_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação do comentário
    com_article INT, -- ID do artigo (referência para article)
    com_author_name VARCHAR(127) NOT NULL, -- Nome do autor do comentário
    com_author_email VARCHAR(127) NOT NULL, -- Email do autor do comentário
    com_comment TEXT NOT NULL, -- Conteúdo do comentário
    com_status ENUM('on', 'off', 'del') DEFAULT 'on', -- Status do comentário
    FOREIGN KEY(com_article) REFERENCES article(art_id) -- Chave estrangeira para article
);

-- Cria a tabela "contact" para armazenar mensagens de contato
CREATE TABLE contact(
    id INT PRIMARY KEY AUTO_INCREMENT, -- ID único da mensagem
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação da mensagem
    name VARCHAR(127) NOT NULL, -- Nome do remetente
    email VARCHAR(127) NOT NULL, -- Email do remetente
    subject VARCHAR(255) NOT NULL, -- Assunto da mensagem
    message TEXT NOT NULL, -- Conteúdo da mensagem
    status ENUM('received', 'readed', 'responded', 'deleted') -- Status da mensagem
);

-- ------------------------------------------- --
-- Popula(colocar) as tabelas com alguns dados --
-- ------------------------------------------- --


-- Tabela "staff"
INSERT INTO staff(
    sta_name,         -- Nome do usuário
    sta_email,        -- Email do usuário
    sta_password,     -- Senha (armazenada como hash)
    sta_birth,        -- Data de nascimento
    sta_description,  -- Descrição do usuário
    sta_type          -- Tipo de usuário (admin, author, moderator)
) VALUES (
    'Cinval dos Santos',           -- Nome do primeiro usuário
    'cincin@email.com',            -- Email do primeiro usuário
    SHA1('a1b2c3'),                -- Senha do primeiro usuário (hash)
    '2002-06-15',                  -- Data de nascimento do primeiro usuário
    'De tudo mais um pouco',       -- Descrição do primeiro usuário
    'admin'                        -- Tipo do primeiro usuário
), (
    'Ana Carolina Ribeiro',         -- Nome do segundo usuário
    'anari@email.com',             -- Email do segundo usuário
    SHA1('qwert9513'),             -- Senha do segundo usuário (hash)
    '1990-01-25',                  -- Data de nascimento do segundo usuário
    'Professora, leitora, curiosa e exploradora', -- Descrição do segundo usuário
    'author'                       -- Tipo do segundo usuário
), (
    'Lucas Almeida',                -- Nome do terceiro usuário
    'lucas.almeida@email.com',     -- Email do terceiro usuário
    SHA1('password123'),           -- Senha do terceiro usuário (hash)
    '1985-03-10',                  -- Data de nascimento do terceiro usuário
    'Aventureiro e amante da natureza', -- Descrição do terceiro usuário
    'moderator'                    -- Tipo do terceiro usuário
), (
    'Mariana Ferreira',             -- Nome da quarta usuário
    'mariana.ferreira@email.com',   -- Email da quarta usuário
    SHA1('mariana456'),            -- Senha da quarta usuário (hash)
    '1995-07-20',                  -- Data de nascimento da quarta usuário
    'Escritora e viajante',        -- Descrição da quarta usuário
    'author'                       -- Tipo da quarta usuário
), (
    'Roberto Silva',                -- Nome do quinto usuário
    'roberto.silva@email.com',     -- Email do quinto usuário
    SHA1('roberto789'),            -- Senha do quinto usuário (hash)
    '1978-11-05',                  -- Data de nascimento do quinto usuário
    'Entusiasta da tecnologia e inovação', -- Descrição do quinto usuário
    'admin'                        -- Tipo do quinto usuário
), (
    'Juliana Costa',                -- Nome da sexta usuário
    'juliana.costa@email.com',     -- Email da sexta usuário
    SHA1('juliana321'),            -- Senha da sexta usuário (hash)
    '1992-02-15',                  -- Data de nascimento da sexta usuário
    'Designer e criadora de conteúdo', -- Descrição da sexta usuário
    'author'                       -- Tipo da sexta usuário
);

-- Tabela "article"
INSERT INTO article(
    art_title,          -- Título do artigo
    art_resume,         -- Resumo do artigo
    art_thumbnail,      -- URL da imagem thumbnail do artigo
    art_content,        -- Conteúdo completo do artigo
    art_author          -- ID do autor (referência para staff)
) VALUES (
    'Primeiro Artigo',
    'Lorem, ipsum dolor sit amet consectetur adipisicing elit',
    'https://picsum.photos/id/1/200/300',
    '<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima iure ratione molestiae modi soluta aperiam dicta
    repudiandae esse maxime dolor at possimus quidem fugiat, velit nam asperiores? Soluta, obcaecati pariatur.</p>
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Possimus animi commodi praesentium perspiciatis sit totam,
    ullam aliquam voluptatum veniam nostrum facere sapiente nesciunt repellat eligendi labore deserunt eos officiis
    dolor.</p>
    <img src="https://picsum.photos/id/1/200/300" alt="Imagem Aleatória">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic dolores ut incidunt minus vel debitis quod asperiores
    maxime, aut corrupti doloremque saepe quasi vitae perspiciatis temporibus soluta earum dolore voluptate?</p>
    <h4>Lista de links</h4>
    <ul>
        <li><a href="https://www.google.com.br/" target="_blank">Google</a></li>
        <li><a href="https://openai.com/chatgpt/" target="_blank">Chat GPT</a></li>
    </ul>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis explicabo porro libero magni ipsam eligendi, optio
        nisi fuga iusto maiores sit rem tempora amet perferendis repudiandae at quae id molestiae!</p>',
    '2'
),
-- Inserções pelo chatGPT
(
    'Segundo Artigo',  -- Título do segundo artigo
    'Explorando a natureza e suas belezas',  -- Resumo
    'https://picsum.photos/id/2/200/300',  -- Thumbnail do artigo
    '<p>A natureza é um dos maiores presentes que temos. Neste artigo, exploramos suas maravilhas e o que podemos fazer para preservá-las.</p>',  -- Conteúdo
    '1'  -- Autor: Cinval dos Santos
), (
    'Terceiro Artigo',  -- Título do terceiro artigo
    'Tecnologia e Inovação',  -- Resumo
    'https://picsum.photos/id/3/200/300',  -- Thumbnail do artigo
    '<p>A tecnologia está mudando rapidamente a forma como vivemos. Vamos discutir algumas inovações que estão moldando nosso futuro.</p>',  -- Conteúdo
    '5'  -- Autor: Roberto Silva
), (
    'Quarto Artigo',  -- Título do quarto artigo
    'Dicas de leitura',  -- Resumo
    'https://picsum.photos/id/4/200/300',  -- Thumbnail do artigo
    '<p>Se você é um amante de livros, confira nossas dicas de leitura que vão ampliar seus horizontes e enriquecer seu conhecimento.</p>',  -- Conteúdo
    '2'  -- Autor: Ana Carolina Ribeiro
), (
    'Quinto Artigo',  -- Título do quinto artigo
    'Cozinhando com amor',  -- Resumo
    'https://picsum.photos/id/5/200/300',  -- Thumbnail do artigo
    '<p>Cozinhar é uma arte. Neste artigo, falamos sobre receitas que trazem o amor e a tradição para a mesa.</p>',  -- Conteúdo
    '6'  -- Autor: Juliana Costa
), (
    'Sexto Artigo',  -- Título do sexto artigo
    'Viajando pelo mundo',  -- Resumo
    'https://picsum.photos/id/6/200/300',  -- Thumbnail do artigo
    '<p>Viajar é uma forma de aprender sobre diferentes culturas. Aqui estão algumas dicas para sua próxima aventura.</p>',  -- Conteúdo
    '4'  -- Autor: Mariana Ferreira
), (
    'Sétimo Artigo',  -- Título do sétimo artigo
    'A importância do autocuidado',  -- Resumo
    'https://picsum.photos/id/7/200/300',  -- Thumbnail do artigo
    '<p>O autocuidado é fundamental para a nossa saúde mental. Vamos explorar práticas que podem ajudar.</p>',  -- Conteúdo
    '3'  -- Autor: Lucas Almeida
), (
    'Oitavo Artigo',  -- Título do oitavo artigo
    'O futuro da educação',  -- Resumo
    'https://picsum.photos/id/8/200/300',  -- Thumbnail do artigo
    '<p>A educação está em constante evolução. Neste artigo, discutimos o que o futuro nos reserva nesse aspecto.</p>',  -- Conteúdo
    '2'  -- Autor: Ana Carolina Ribeiro
), (
    'Nono Artigo',  -- Título do nono artigo
    'Sustentabilidade no dia a dia',  -- Resumo
    'https://picsum.photos/id/9/200/300',  -- Thumbnail do artigo
    '<p>Viver de forma sustentável é uma responsabilidade de todos. Veja como pequenas mudanças podem fazer a diferença.</p>',  -- Conteúdo
    '5'  -- Autor: Roberto Silva
), (
    'Décimo Artigo',  -- Título do décimo artigo
    'Criatividade e inovação',  -- Resumo
    'https://picsum.photos/id/10/200/300',  -- Thumbnail do artigo
    '<p>Ser criativo é essencial em todos os aspectos da vida. Vamos explorar como a criatividade pode impulsionar a inovação.</p>',  -- Conteúdo
    '6'  -- Autor: Juliana Costa
), (
    'Décimo Primeiro Artigo',  -- Título do décimo primeiro artigo
    'Cuidado com a saúde mental',  -- Resumo
    'https://picsum.photos/id/11/200/300',  -- Thumbnail do artigo
    '<p>A saúde mental é tão importante quanto a saúde física. Aqui estão algumas dicas para cuidar do seu bem-estar emocional.</p>',  -- Conteúdo
    '3'  -- Autor: Lucas Almeida
);


-- Tabela "comment"
INSERT INTO comment(
    com_article,
    com_author_name,
    com_author_email,
    com_comment
) VALUES (
    '2',  -- ID do artigo ao qual o comentário se refere
    'Rivaldinho Almeida',  -- Nome do autor do comentário
    'rivaldinho_al@email.com',  -- Email do autor do comentário
    'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis explicabo porro libero magni ipsam eligendi, optio nisi fuga iusto maiores sit rem tempora amet perferendis repudiandae at quae id molestiae!'  -- Conteúdo do comentário
), 
    -- Inserções pelo chatGPT
(
    '1',  -- ID do artigo ao qual o comentário se refere
    'Maria Clara',  -- Nome do autor do comentário
    'mariaclara@email.com',  -- Email do autor do comentário
    'Adorei o artigo! Muito informativo e bem escrito.'  -- Conteúdo do comentário
), (
    '3',  -- ID do artigo ao qual o comentário se refere
    'João Pedro',  -- Nome do autor do comentário
    'joaopedro@email.com',  -- Email do autor do comentário
    'Ótimas dicas de tecnologia! Mal posso esperar para ver as inovações futuras.'  -- Conteúdo do comentário
), (
    '4',  -- ID do artigo ao qual o comentário se refere
    'Ana Beatriz',  -- Nome do autor do comentário
    'anabeatriz@email.com',  -- Email do autor do comentário
    'Essas dicas de leitura são incríveis! Vou começar a ler os livros sugeridos.'  -- Conteúdo do comentário
), (
    '5',  -- ID do artigo ao qual o comentário se refere
    'Carlos Silva',  -- Nome do autor do comentário
    'carlossilva@email.com',  -- Email do autor do comentário
    'Amei a receita! Com certeza vou experimentar no próximo jantar.'  -- Conteúdo do comentário
), (
    '6',  -- ID do artigo ao qual o comentário se refere
    'Fernanda Souza',  -- Nome do autor do comentário
    'fernandasouza@email.com',  -- Email do autor do comentário
    'Viajar é tudo de bom! Obrigada pelas dicas valiosas.'  -- Conteúdo do comentário
), (
    '7',  -- ID do artigo ao qual o comentário se refere
    'Eduardo Lima',  -- Nome do autor do comentário
    'eduardolima@email.com',  -- Email do autor do comentário
    'O autocuidado é fundamental! Muito importante falar sobre isso.'  -- Conteúdo do comentário
);

/*** Otimizado e comentado pelo chat GPT 

-- --------------------------- 
-- Banco de dados "myblogdb" 
-- --------------------------- 

-- Apaga o banco de dados caso ele já exista
-- PERIGO! Não faça isso em modo de produção
DROP DATABASE IF EXISTS myblogdb;

-- Cria o banco de dados
-- !!!!!!!!!!!!!!!!!!!!!! ATENÇÃO !!!!!!!!!!!!!!!!!!!
-- Remova este comando após a publicação da versão de produção
CREATE DATABASE myblogdb 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_general_ci;

-- Seleciona o banco de dados para os próximos comandos
USE myblogdb;

-- Criação da tabela "staff" para armazenar informações dos usuários do blog
CREATE TABLE staff (
    sta_id INT PRIMARY KEY AUTO_INCREMENT, -- ID único do staff
    sta_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação do registro
    sta_name VARCHAR(127) NOT NULL, -- Nome do staff
    sta_email VARCHAR(255) NOT NULL UNIQUE, -- Email do staff (único)
    sta_password VARCHAR(63) NOT NULL, -- Senha do staff (armazenada como hash)
    sta_birth DATE NOT NULL, -- Data de nascimento
    sta_description VARCHAR(255), -- Descrição do staff
    sta_type ENUM('moderator', 'author', 'admin') DEFAULT 'moderator', -- Tipo de usuário
    sta_status ENUM('on', 'off', 'del') DEFAULT 'on' -- Status do usuário
);

-- Criação da tabela "article" para armazenar os artigos do blog
CREATE TABLE article (
    art_id INT PRIMARY KEY AUTO_INCREMENT, -- ID único do artigo
    art_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação do artigo
    art_title VARCHAR(127) NOT NULL, -- Título do artigo
    art_resume VARCHAR(255) NOT NULL, -- Resumo do artigo
    art_thumbnail VARCHAR(255) NOT NULL, -- Thumbnail do artigo
    art_content TEXT NOT NULL, -- Conteúdo do artigo
    art_view INT DEFAULT 0, -- Contador de visualizações
    art_author INT, -- ID do autor (referência para staff)
    art_status ENUM('on', 'off', 'del') DEFAULT 'on', -- Status do artigo
    FOREIGN KEY (art_author) REFERENCES staff (sta_id) -- Chave estrangeira para staff
);

-- Criação da tabela "comment" para armazenar os comentários nos artigos
CREATE TABLE comment (
    com_id INT PRIMARY KEY AUTO_INCREMENT, -- ID único do comentário
    com_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação do comentário
    com_article INT, -- ID do artigo (referência para article)
    com_author_name VARCHAR(127) NOT NULL, -- Nome do autor do comentário
    com_author_email VARCHAR(127) NOT NULL, -- Email do autor do comentário
    com_comment TEXT NOT NULL, -- Conteúdo do comentário
    com_status ENUM('on', 'off', 'del') DEFAULT 'on', -- Status do comentário
    FOREIGN KEY(com_article) REFERENCES article(art_id) -- Chave estrangeira para article
);

-- Criação da tabela "contact" para armazenar mensagens de contato
CREATE TABLE contact (
    id INT PRIMARY KEY AUTO_INCREMENT, -- ID único da mensagem
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data de criação da mensagem
    name VARCHAR(127) NOT NULL, -- Nome do remetente
    email VARCHAR(127) NOT NULL, -- Email do remetente
    subject VARCHAR(255) NOT NULL, -- Assunto da mensagem
    message TEXT NOT NULL, -- Conteúdo da mensagem
    status ENUM('received', 'readed', 'responded', 'deleted') DEFAULT 'received' -- Status da mensagem
);

-- ------------------------------------------- 
-- Popula(colocar) as tabelas com alguns dados 
-- ------------------------------------------- 

-- Tabela "staff"
INSERT INTO staff (sta_name, sta_email, sta_password, sta_birth, sta_description, sta_type) VALUES 
    ('Cinval dos Santos', 'cincin@email.com', SHA1('a1b2c3'), '2002-06-15', 'De tudo mais um pouco', 'admin'),
    ('Ana Carolina Ribeiro', 'anari@email.com', SHA1('qwert9513'), '1990-01-25', 'Professora, leitora, curiosa e exploradora', 'author'),
    ('Lucas Almeida', 'lucas.almeida@email.com', SHA1('password123'), '1985-03-10', 'Aventureiro e amante da natureza', 'moderator'),
    ('Mariana Ferreira', 'mariana.ferreira@email.com', SHA1('mariana456'), '1995-07-20', 'Escritora e viajante', 'author'),
    ('Roberto Silva', 'roberto.silva@email.com', SHA1('roberto789'), '1978-11-05', 'Entusiasta da tecnologia e inovação', 'admin'),
    ('Juliana Costa', 'juliana.costa@email.com', SHA1('juliana321'), '1992-02-15', 'Designer e criadora de conteúdo', 'author');

-- Tabela "article"
INSERT INTO article (art_title, art_resume, art_thumbnail, art_content, art_author) VALUES 
    ('Primeiro Artigo', 'Lorem, ipsum dolor sit amet consectetur adipisicing elit', 'https://picsum.photos/id/1/200/300',
     '<p>Lorem ipsum dolor sit amet consectetur adipisicing elit...</p>', 2), -- Simplificado para brevidade
    ('Segundo Artigo', 'Explorando a natureza e suas belezas', 'https://picsum.photos/id/2/200/300',
     '<p>A natureza é um dos maiores presentes que temos...</p>', 1),
    ('Terceiro Artigo', 'Tecnologia e Inovação', 'https://picsum.photos/id/3/200/300',
     '<p>A tecnologia está mudando rapidamente a forma como vivemos...</p>', 5),
    ('Quarto Artigo', 'Dicas de leitura', 'https://picsum.photos/id/4/200/300',
     '<p>Se você é um amante de livros, confira nossas dicas...</p>', 2),
    ('Quinto Artigo', 'Cozinhando com amor', 'https://picsum.photos/id/5/200/300',
     '<p>Cozinhar é uma arte...</p>', 6),
    ('Sexto Artigo', 'Viajando pelo mundo', 'https://picsum.photos/id/6/200/300',
     '<p>Viajar é uma forma de aprender sobre diferentes culturas...</p>', 4),
    ('Sétimo Artigo', 'A importância do autocuidado', 'https://picsum.photos/id/7/200/300',
     '<p>O autocuidado é fundamental para a nossa saúde mental...</p>', 3),
    ('Oitavo Artigo', 'O futuro da educação', 'https://picsum.photos/id/8/200/300',
     '<p>A educação está em constante evolução...</p>', 2),
    ('Nono Artigo', 'Sustentabilidade no dia a dia', 'https://picsum.photos/id/9/200/300',
     '<p>Viver de forma sustentável é uma responsabilidade de todos...</p>', 5),
    ('Décimo Artigo', 'Criatividade e inovação', 'https://picsum.photos/id/10/200/300',
     '<p>Ser criativo é essencial em todos os aspectos da vida...</p>', 6),
    ('Décimo Primeiro Artigo', 'Cuidado com a saúde mental', 'https://picsum.photos/id/11/200/300',
     '<p>A saúde mental é tão importante quanto a saúde física...</p>', 3);

-- Tabela "comment"
INSERT INTO comment (com_article, com_author_name, com_author_email, com_comment) VALUES 
    (2, 'Rivaldinho Almeida', 'rivaldinho_al@email.com', 'Lorem ipsum dolor sit amet...'),
    (1, 'Maria Clara', 'mariaclara@email.com', 'Adorei o artigo! Muito informativo e bem escrito.'),
    (3, 'João Pedro', 'joaopedro@email.com', 'Ótimas dicas de tecnologia! Mal posso esperar para ver as inovações futuras.'),
    (4, 'Ana Beatriz', 'anabeatriz@email.com', 'Essas dicas de leitura são incríveis!'),
    (5, 'Carlos Silva', 'carlossilva@email.com', 'Amei a receita! Com certeza vou experimentar.'),
    (6, 'Fernanda Souza', 'fernandasouza@email.com', 'Viajar é tudo de bom! Obrigada pelas dicas.'),
    (7, 'Eduardo Lima', 'eduardolima@email.com', 'O autocuidado é fundamental! Muito importante falar sobre isso.');



***/
