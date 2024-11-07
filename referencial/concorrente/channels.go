package main

import (
    "fmt"
    "time"
)

func enviarMensagem(canal chan string, mensagem string, delay time.Duration) {
    time.Sleep(delay) // Espera antes de enviar a mensagem
    canal <- mensagem  // Envia a mensagem para o canal
}

func main() {
    canal1 := make(chan string)
    canal2 := make(chan string)

    // Inicia duas goroutines para enviar mensagens
    go enviarMensagem(canal1, "Mensagem de canal 1", 2*time.Second)
    go enviarMensagem(canal2, "Mensagem de canal 2", 1*time.Second)

    // Usando select para receber mensagens de ambos os canais
    for i := 0; i < 2; i++ {
        select {
        case msg1 := <-canal1:
            fmt.Println("Recebido:", msg1)
        case msg2 := <-canal2:
            fmt.Println("Recebido:", msg2)
        }
    }
}
