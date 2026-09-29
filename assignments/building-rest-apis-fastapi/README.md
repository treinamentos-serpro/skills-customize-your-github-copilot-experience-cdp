# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos, códigos de resposta e operações CRUD.

## 📝 Tasks

### 🛠️ Consulte a coleção de livros

#### Descrição

Use o código inicial para executar a aplicação e implemente a consulta de um livro pelo identificador. A rota de listagem já está pronta para que você possa explorar a estrutura da API.

Para instalar as dependências e iniciar o servidor a partir da raiz do repositório:

```bash
python -m pip install fastapi uvicorn
python assignments/building-rest-apis-fastapi/starter-code.py
```

Acesse `http://127.0.0.1:8000/docs` para testar as rotas pela documentação interativa.

#### Requisitos

O programa concluído deve:

- Listar todos os livros em `GET /books`.
- Retornar um livro em `GET /books/{book_id}` quando o identificador existir.
- Responder com o código HTTP `404` quando o livro solicitado não existir.

### 🛠️ Cadastre e atualize livros

#### Descrição

Implemente as rotas para adicionar um livro à coleção e atualizar um livro existente. Use o modelo de entrada para validar os dados recebidos no corpo da requisição.

#### Requisitos

O programa concluído deve:

- Criar livros em `POST /books` e responder com o código HTTP `201`.
- Gerar um identificador para cada livro criado, sem exigir que o cliente o envie.
- Atualizar título, autor e ano de publicação em `PUT /books/{book_id}`.
- Responder com `404` ao tentar atualizar um livro inexistente.

Exemplo de corpo para criação ou atualização:

```json
{
  "title": "O Jardim Secreto",
  "author": "Frances Hodgson Burnett",
  "year": 1911
}
```

### 🛠️ Remova livros e verifique as respostas

#### Descrição

Implemente a remoção de livros e teste os caminhos de sucesso e de erro pela documentação interativa da API.

#### Requisitos

O programa concluído deve:

- Remover um livro em `DELETE /books/{book_id}`.
- Responder com o código HTTP `204` quando a remoção for concluída.
- Responder com `404` quando o identificador não corresponder a um livro.
- Manter os dados em memória; eles podem voltar ao estado inicial quando o servidor for reiniciado.
