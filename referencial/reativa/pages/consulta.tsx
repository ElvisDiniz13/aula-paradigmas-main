import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import { useState, useEffect } from "react";

function ListaDeUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [carregando, setCarregando] = useState(true);

  // Reagir ao montar o componente: buscar dados da API
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        setUsuarios(data); // Atualiza o estado com os dados recebidos
        setCarregando(false); // Finaliza o estado de carregamento
      });
  }, []); // [] significa que o efeito roda apenas ao montar o componente

  if (carregando) {
    return <p>Carregando...</p>;
  }

  return (
    <main className={styles.main}>
      <h1 className={styles.aula}>Lista de Usuários</h1>
      <ul className={styles.aula}>
        {usuarios.map((usuario) => (
          <li key={usuario.id}>{usuario.name}</li>
        ))}
      </ul>
    </main>
  );
}

export default ListaDeUsuarios;
