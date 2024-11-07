import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import { useState, useEffect } from "react";

function ContadorComMensagem() {
  const [contador, setContador] = useState(0);

  // Efeito colateral: exibe uma mensagem no console quando o contador muda
  useEffect(() => {
    console.log(`O contador mudou para: ${contador}`);
  }, [contador]); // Reage apenas a mudanças no contador

  const incrementar = () => {
    setContador(contador + 1);
  };

  return (
    <main className={styles.main}>
      <p className={styles.aula}>Você clicou {contador} vezes</p>
      <button onClick={incrementar}>Incrementar</button>
    </main>
  );
}

export default ContadorComMensagem;
