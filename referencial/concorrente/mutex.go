package main

import (
    "fmt"    // Importa o pacote fmt para formatação de entrada e saída
    "sync"   // Importa o pacote sync para usar WaitGroup e Mutex
)

// Estrutura Contador que contém um valor inteiro e um mutex para controle de acesso
type Contador struct {
    valor int          // O valor que será incrementado
    mutex sync.Mutex  // Mutex para garantir acesso exclusivo ao valor
}

// Método Incrementar que incrementa o valor de Contador de forma segura
func (c *Contador) Incrementar() {
    c.mutex.Lock()   // Bloqueia o mutex para garantir que apenas uma goroutine pode acessar o valor
    c.valor++        // Incrementa o valor do contador
    c.mutex.Unlock() // Desbloqueia o mutex após a operação
}

func main() {
    contador := Contador{} // Cria uma nova instância de Contador
    var wg sync.WaitGroup   // Declara um WaitGroup para gerenciar a sincronização das goroutines

    // Inicia 1000 goroutines para incrementar o contador
    for i := 0; i < 1000; i++ {
        wg.Add(1) // Adiciona um contador ao WaitGroup
        go func() {
            defer wg.Done() // Marca a goroutine como concluída quando ela termina
            contador.Incrementar() // Chama o método Incrementar para incrementar o contador
        }()
    }

    wg.Wait() // Aguarda até que todas as goroutines tenham terminado
    fmt.Println("Valor final do contador:", contador.valor) // Imprime o valor final do contador
}
