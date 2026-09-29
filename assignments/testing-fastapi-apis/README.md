# 📘 Assignment: Testando APIs FastAPI com pytest

## 🎯 Objective

Escreva testes automatizados para uma API de livros feita com FastAPI, usando `pytest` e o cliente de testes do framework. Você verificará respostas HTTP, conteúdo JSON, validação e isolamento entre testes.

## 📝 Tasks

### 🛠️ Verifique as rotas de consulta

#### Descrição

Instale as dependências e execute a suíte inicial. Em seguida, amplie os testes das rotas de consulta para verificar tanto respostas de sucesso quanto recursos inexistentes.

A partir da raiz do repositório, instale as dependências e execute os testes:

```bash
python -m pip install fastapi pytest httpx httpx2
python -m pytest -v assignments/testing-fastapi-apis/test_api.py
```

#### Requisitos

A suíte deve:

- Confirmar que `GET /books` responde com código `200` e uma lista em JSON.
- Confirmar que `GET /books/{book_id}` retorna os dados do livro existente.
- Confirmar que a consulta de um identificador inexistente responde com código `404`.

### 🛠️ Teste a criação e a atualização de livros

#### Descrição

Adicione testes para as rotas que recebem dados no corpo da requisição. Verifique o código de resposta e os campos retornados, além dos casos de entrada inválida e livro inexistente.

#### Requisitos

A suíte deve:

- Confirmar que `POST /books` cria um livro, responde com código `201` e retorna um identificador.
- Confirmar que `PUT /books/{book_id}` atualiza os campos do livro e responde com código `200`.
- Confirmar que corpos inválidos são rejeitados com código `422`.
- Confirmar que a atualização de um identificador inexistente responde com código `404`.

Exemplo de corpo JSON válido:

```json
{
  "title": "O Jardim Secreto",
  "author": "Frances Hodgson Burnett",
  "year": 1911
}
```

### 🛠️ Teste a remoção e o isolamento dos casos

#### Descrição

Complete a cobertura testando a remoção e execute a suíte inteira mais de uma vez. Cada teste deve começar com os dados iniciais, sem depender da ordem de execução ou dos efeitos de outro teste.

#### Requisitos

A suíte deve:

- Confirmar que `DELETE /books/{book_id}` remove o livro e responde com código `204`.
- Confirmar que remover um identificador inexistente responde com código `404`.
- Restaurar a coleção inicial antes de cada teste usando a fixture fornecida.
- Passar ao executar `python -m pytest -v assignments/testing-fastapi-apis/test_api.py`.
