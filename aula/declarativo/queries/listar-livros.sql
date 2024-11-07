SELECT livros.titulo, autores.nome AS autor, generos.nome AS genero, livros.ano_publicacao, livros.preco
FROM livros
JOIN autores ON livros.autor_id = autores.autor_id
JOIN generos ON livros.genero_id = generos.genero_id;
