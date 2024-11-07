import styles from "../styles/Home.module.css"; // Importa os estilos CSS

function ListaDeUsuarios() {
  return (
    <main className={styles.main}>
      <h1 className={styles.aula}>Lista de Usuários</h1>
      <ul className={styles.aula}></ul>
    </main>
  );
}

export default ListaDeUsuarios;
