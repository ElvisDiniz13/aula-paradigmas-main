package main

import (
    "fmt"
    "time"
)

// Função que simula um trabalho que leva algum tempo
func trabalho(nome string) {
    fmt.Println(nome, "iniciou")
    time.Sleep(2 * time.Second) // Simula um trabalho que leva 2 segundos
    fmt.Println(nome, "finalizou")
}

func main() {
    // Inicia duas goroutines
    go trabalho("Goroutine 1")
    go trabalho("Goroutine 2")

    // Aguarda um tempo para as goroutines terminarem
    time.Sleep(3 * time.Second) // Espera um pouco mais do que o trabalho das goroutines
    fmt.Println("Todos os trabalhos concluídos.")
}
