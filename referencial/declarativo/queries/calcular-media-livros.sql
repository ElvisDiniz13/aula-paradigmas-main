SELECT generos.nome AS genero, AVG(livros.preco) AS preco_medio
FROM livros
JOIN generos ON livros.genero_id = generos.genero_id
GROUP BY generos.nome;