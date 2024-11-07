-- Criação da tabela de autores
CREATE TABLE autores (
    autor_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50),
    data_nascimento DATE
);

-- Criação da tabela de gêneros
CREATE TABLE generos (
    genero_id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

-- Criação da tabela de livros
CREATE TABLE livros (
    livro_id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    ano_publicacao INTEGER,
    autor_id INT,
    genero_id INT,
    preco NUMERIC(10, 2),
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id),
    FOREIGN KEY (genero_id) REFERENCES generos(genero_id)
);

-- Inserção de dados na tabela de autores
INSERT INTO autores (nome, nacionalidade, data_nascimento) VALUES
('Gabriel Garcia Marquez', 'Colombiana', '1927-03-06'),
('Jane Austen', 'Britânica', '1775-12-16'),
('George Orwell', 'Britânica', '1903-06-25'),
('Machado de Assis', 'Brasileira', '1839-06-21');

-- Inserção de dados na tabela de gêneros
INSERT INTO generos (nome) VALUES
('Romance'),
('Ficção Científica'),
('Fantasia'),
('História'),
('Suspense');

-- Inserção de dados na tabela de livros
INSERT INTO livros (titulo, ano_publicacao, autor_id, genero_id, preco) VALUES
('Cem Anos de Solidão', 1967, 1, 1, 39.90),
('Orgulho e Preconceito', 1813, 2, 1, 29.90),
('1984', 1949, 3, 2, 19.90),
('Dom Casmurro', 1899, 4, 1, 34.90),
('Fahrenheit 451', 1953, 3, 2, 24.90);