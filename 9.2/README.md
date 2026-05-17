# Exercício 9.2 - API FastAPI

API RESTful implementada com FastAPI e servida com Uvicorn.

## Como rodar

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
```

A API sobe em `http://localhost:8000`

A documentação automática fica disponível em `http://localhost:8000/docs`

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Hello World |
| GET | `/items` | Lista todos os itens |
| GET | `/items/{id}` | Busca item por ID |
| POST | `/items` | Cria novo item |
| PUT | `/items/{id}` | Atualiza item |
| DELETE | `/items/{id}` | Remove item |

## Exemplo de uso

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
