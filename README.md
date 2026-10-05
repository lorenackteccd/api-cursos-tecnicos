# API de Cursos Técnicos

## 1. Objetivo

Este projeto simula o backend de um portal da Secretaria de Educação destinado a fornecer informações sobre cursos técnicos disponíveis no estado.

A aplicação disponibiliza uma API Web que retorna dados de cursos em formato JSON. Os dados são mockados, ou seja, estão armazenados diretamente no código e não dependem de um banco de dados.

## 2. Desenvolvimento de Sistemas e SDLC

### Metodologia escolhida: Ágil

Para este projeto, foi escolhida a metodologia Ágil. A abordagem Ágil é adequada porque permite desenvolver o sistema de forma incremental, realizando entregas em etapas e possibilitando ajustes conforme novas necessidades aparecem.

No cenário apresentado, a Secretaria de Educação pode posteriormente solicitar novas funcionalidades, como consulta de instituições, vagas ou matrículas. O desenvolvimento incremental facilita a evolução do sistema sem exigir que todo o projeto seja planejado e concluído de uma única vez.

## 3. Arquitetura de Serviços

### Arquitetura escolhida: Microsserviço

A solução foi planejada como um microsserviço responsável pelo fornecimento dos dados dos cursos técnicos.

A escolha considera a possibilidade de crescimento do sistema. No futuro, outros serviços independentes poderiam ser criados, por exemplo, um serviço de matrículas, um serviço de alunos ou um serviço de instituições. Dessa forma, cada serviço poderia possuir uma responsabilidade específica e evoluir de maneira independente.

Para o exercício, entretanto, foi implementado apenas o serviço de cursos, mantendo a solução simples e adequada ao objetivo da atividade.

## 4. Definição da API

A API utiliza o padrão HTTP e possui dois endpoints principais:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/cursos` | Retorna a lista de todos os cursos |
| GET | `/cursos/{id}` | Retorna os dados de um curso específico pelo ID |

### Exemplo

Para consultar todos os cursos:

`GET http://127.0.0.1:5000/cursos`

Para consultar o curso de ID 1:

`GET http://127.0.0.1:5000/cursos/1`

Caso o ID informado não exista, a API retorna o código HTTP `404` e uma mensagem informando que o curso não foi encontrado.

## 5. Tecnologias utilizadas

- Python 3
- Flask
- API REST
- JSON
- Git
- GitHub

## 6. Estrutura do projeto

```text
api-cursos-tecnicos/
├── app.py
├── README.md
└── requirements.txt
```

## 7. Como instalar

### Pré-requisito

Ter o Python 3 instalado no computador.

Verifique no terminal:

```bash
python --version
```

ou, no Windows:

```bash
py --version
```

### Instalação do Flask

No terminal, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

Se necessário, no Windows:

```bash
py -m pip install -r requirements.txt
```

## 8. Como executar

No terminal, dentro da pasta do projeto:

```bash
python app.py
```

No Windows, se necessário:

```bash
py app.py
```

A aplicação será iniciada em:

`http://127.0.0.1:5000`

## 9. Como testar

### Listar todos os cursos

Abra no navegador:

`http://127.0.0.1:5000/cursos`

A API deverá retornar uma lista em formato JSON.

### Consultar um curso específico

Abra:

`http://127.0.0.1:5000/cursos/1`

A API deverá retornar os dados do curso de ID 1.

### Testar um ID inexistente

Abra:

`http://127.0.0.1:5000/cursos/999`

A API deverá retornar erro `404` informando que o curso não foi encontrado.

## 10. Dados mockados

Os dados utilizados na aplicação são fictícios e foram inseridos diretamente no arquivo `app.py`, conforme solicitado na atividade. Não foi utilizado banco de dados.

## 11. Versionamento

Versionado com Git e disponibilizado em um repositório público ou compartilhado no GitHub.

Histórico de commits:

1. `Commit inicial: cria estrutura do projeto`
2. `Docs: adiciona planejamento da arquitetura`
3. `Feature: adiciona endpoint de listagem de cursos`
4. `Feature: adiciona consulta de curso por ID`
5. `Docs: finaliza documentação de execução da API`
