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
    -- Usando o conjunto de caracteres UTF-8
    CHARACTER SET utf8mb4 
    -- Buscas em UTF-8 e case insensitive
    COLLATE utf8mb4_general_ci;

-- Seleciona o banco de dados para os próximos comandos
USE myblogdb;

-- Cria a tabela "staff"
CREATE TABLE staff(
    sta_id INT PRIMARY KEY AUTO_INCREMENT,
    sta_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sta_name VARCHAR(127) NOT NULL,
    sta_email VARCHAR(255) NOT NULL,
    sta_password VARCHAR(63) NOT NULL,
    sta_birth DATE NOT NULL,
    sta_description VARCHAR(255),
    sta_type ENUM('moderator', 'author', 'admin') DEFAULT 'moderator',
    sta_status ENUM('on', 'off', 'del') DEFAULT 'on'
);

