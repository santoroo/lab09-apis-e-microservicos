# Exercício 9.1 - API Flask

Aplicação Flask com Hello World e API RESTful completa.

## Como rodar

```bash
pip install flask
python app.py
```

A API sobe em `http://localhost:5001`

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Hello World |
| GET | `/items` | Lista todos os itens |
| GET | `/items/<id>` | Busca item por ID |
| POST | `/items` | Cria novo item |
| PUT | `/items/<id>` | Atualiza item |
| DELETE | `/items/<id>` | Remove item |

## Exemplo de uso

```bash
# Hello World
curl http://localhost:5001/

# Listar itens
curl http://localhost:5001/items

# Criar item
curl -X POST http://localhost:5001/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Novo Item", "description": "Descrição"}'

# Atualizar item
curl -X PUT http://localhost:5001/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Item Atualizado"}'

# Deletar item
curl -X DELETE http://localhost:5001/items/1
```
