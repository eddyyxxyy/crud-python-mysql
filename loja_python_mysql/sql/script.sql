CREATE DATABASE pmysql;

USE pmysql;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    estoque INT NOT NULL
);

INSERT INTO produtos (nome, preco, estoque) VALUES ('Playstation 4', '1675.89', '25');
INSERT INTO produtos (nome, preco, estoque) VALUES ('Xbox One', '1500.00', '30');
INSERT INTO produtos (nome, preco, estoque) VALUES ('Nintendo Switch', '2545.99', '45');
INSERT INTO produtos (nome, preco, estoque) VALUES ('Notebook Nitro 5', '4599.99', '5');
INSERT INTO produtos (nome, preco, estoque) VALUES ('NoBreak', '459.99', '12');
