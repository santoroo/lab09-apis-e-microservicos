# Exercício 9.1 - API Flask

Implementação de uma aplicação "Hello World" em Flask transformada em uma API RESTful completa, com CRUD de items.

## Itens do exercício

- **a)** Implementar uma aplicação "Hello World" em Flask
- **b)** Transformar em uma API RESTful
- **c)** Servir a API localmente
- **d)** Testar os endpoints e métodos via Postman

## Como rodar

```bash
pip install -r requirements.txt
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

## Exemplos de uso

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

## Testes via Postman

A coleção do Postman está disponível em [`postman_collection.json`](./postman_collection.json). Para importar:

1. Abra o Postman
2. Clique em **Import**
3. Selecione o arquivo `postman_collection.json`
