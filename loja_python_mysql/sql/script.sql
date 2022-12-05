CREATE DATABASE pmysql;

USE pmysql;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    estoque INT NOT NULL
);
