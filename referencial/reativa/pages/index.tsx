import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import React from "react"; // Importa React

export default function Home() {
  // JSX que renderiza a interface da página
  return (
    <main className={styles.main}>
      <h1 className={styles.title}>
        MBA em Engenharia de Software | MBA USP/Esalq{" "}
      </h1>
      <h2 className={styles.aula}>Paradigma Reativo</h2>
    </main>
  );
}
