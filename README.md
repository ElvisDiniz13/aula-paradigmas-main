# Paradigmas de Desenvolvimento de Software

Este repositório contém dois ambientes distintos para a execução dos serviços com `Docker Compose`. A estrutura é organizada em duas pastas:

- **aula/**: Ambiente que será utilizado durante a aula.
- **referencial/**: Ambiente de apoio que contém todos os códigos finalizados como referência.

## Estrutura do Projeto

```bash
.
├── aula/
│   ├── concorrente/
│   │   └── docker-compose.yaml
│   ├── declarativo/
│   │   └── docker-compose.yaml
│   ├── funcional/
│   │   └── docker-compose.yaml
│   ├── imperativo/
│   │   └── docker-compose.yaml
│   ├── logico/
│   │   └── docker-compose.yaml
│   ├── orientado-objeto/
│   │   └── docker-compose.yaml
│   ├── reativa/
│   │   └── docker-compose.yaml
├── referencial/
│   ├── concorrente/
│   │   └── docker-compose.yaml
│   ├── declarativo/
│   │   └── docker-compose.yaml
│   ├── funcional/
│   │   └── docker-compose.yaml
│   ├── imperativo/
│   │   └── docker-compose.yaml
│   ├── logico/
│   │   └── docker-compose.yaml
│   ├── orientado-objeto/
│   │   └── docker-compose.yaml
│   ├── reativa/
│   │   └── docker-compose.yaml
└── README.md
```

## Como subir os ambientes

### Ambiente da Aula

Para iniciar o ambiente que será utilizado durante a aula, siga os passos abaixo:

1. Navegue até a pasta aula:

```bash
cd aula
```

2. Acesse a pasta de algum paradigma. Por exemplo, _funcional_:

```bash
cd funcional
```

3. Execute o comando para subir os containers:

```bash
docker-compose up -d
```

4. Após o término da aula, para parar e remover os containers, execute:

```bash
docker-compose down
```

### Ambiente da Referencial

O ambiente referencial contém todos os códigos finalizados para consulta e testes. Para iniciar o ambiente referencial:

1. Navegue até a pasta referencial:

```bash
cd referencial
```

2. Acesse a pasta de algum paradigma. Por exemplo, _funcional_:

```bash
cd funcional
```

3. Execute o comando para subir os containers:

```bash
docker-compose up -d
```

4. Quando terminar de consultar o material, você pode parar e remover os containers com:

```bash
docker-compose down
```

### Observações

- Certifique-se de ter o Docker instalado na sua máquina antes de rodar os comandos.
- Para mais informações sobre o Docker, consulte os tutoriais disponibilizados para a aula.
- Sinta-se à vontade para consultar o ambiente referencial sempre que tiver dúvidas durante a aula.
