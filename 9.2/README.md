# Exercício 9.2 - API FastAPI

API RESTful implementada com FastAPI e servida com o servidor ASGI Uvicorn.

## Itens do exercício

- **a)** Implementar uma API RESTful com FastAPI
- **b)** Servir a API utilizando Uvicorn
- **c)** Testar os endpoints e métodos via Postman

## Como rodar

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

A API sobe em `http://localhost:8000`

> No Windows, caso a porta 8000 esteja bloqueada por permissões, use `--port 8001`.

A documentação automática (Swagger UI) fica disponível em `http://localhost:8000/docs`

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Hello World |
| GET | `/items` | Lista todos os itens |
| GET | `/items/{id}` | Busca item por ID |
| POST | `/items` | Cria novo item |
| PUT | `/items/{id}` | Atualiza item |
| DELETE | `/items/{id}` | Remove item |

## Exemplos de uso

```bash
# Hello World
curl http://localhost:8000/

# Listar itens
curl http://localhost:8000/items

# Criar item
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Novo Item", "description": "Descrição"}'

# Atualizar item
curl -X PUT http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Item Atualizado", "description": "Nova descrição"}'

# Deletar item
curl -X DELETE http://localhost:8000/items/1
```

## Prints da execução

| Arquivo | Descrição |
|---------|-----------|
| [print-terminal-uvicorn.png](./print-terminal-uvicorn.png) | Terminal com Uvicorn em execução |
| [print-browser-hello-world.png](./print-browser-hello-world.png) | Browser acessando `/` |
| [print-browser-items.png](./print-browser-items.png) | Browser acessando `/items` |
| [print-browser-docs.png](./print-browser-docs.png) | Documentação automática do FastAPI em `/docs` |

## Testes via Postman

A coleção do Postman está disponível em [`postman_collection.json`](./postman_collection.json). Para importar:

1. Abra o Postman
2. Clique em **Import**
3. Selecione o arquivo `postman_collection.json`
