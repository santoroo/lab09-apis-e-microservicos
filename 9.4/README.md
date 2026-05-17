# Exercício 9.4 - API RESTful na Nuvem

API RESTful Flask hospedada na Azure App Services com deploy automático via GitHub Actions. Continuação do [Exercício 9.3](../9.3), agora servindo uma API REST completa em vez de apenas um Hello World.

## Itens do exercício

- **a)** Implementar uma API RESTful utilizando Flask
- **b)** Fazer commit da API para o GitHub e acompanhar o deploy automático
- **c)** Testar a API publicada utilizando o Postman

## Como rodar localmente

```bash
pip install -r requirements.txt
python app.py
```

A API sobe em `http://localhost:5002`

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Mensagem inicial |
| GET | `/items` | Lista todos os itens |
| GET | `/items/<id>` | Busca item por ID |
| POST | `/items` | Cria novo item |
| PUT | `/items/<id>` | Atualiza item |
| DELETE | `/items/<id>` | Remove item |

## Exemplos de uso

```bash
# Listar itens
curl http://localhost:5002/items

# Criar item
curl -X POST http://localhost:5002/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Novo Item", "description": "Descrição"}'

# Atualizar item
curl -X PUT http://localhost:5002/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Item Atualizado"}'

# Deletar item
curl -X DELETE http://localhost:5002/items/1
```

## Deploy na Azure

O deploy reaproveita a infraestrutura criada no [Exercício 9.3](../9.3) — mesmo App Service com pipeline CI/CD configurado pelo GitHub Actions.

A cada `push` na branch `master`, o GitHub Actions publica a aplicação automaticamente na Azure. O servidor de produção utilizado é o **Gunicorn**, com o comando de inicialização em [`startup.txt`](./startup.txt):

```
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

## Testes via Postman

A coleção do Postman está disponível em [`postman_collection.json`](./postman_collection.json). Ela utiliza a variável `{{baseUrl}}` — basta alterar para a URL do App Service na Azure para testar a aplicação em produção:

1. Abra o Postman
2. Clique em **Import** e selecione `postman_collection.json`
3. Na coleção, edite a variável `baseUrl`:
   - Local: `http://localhost:5002`
   - Azure: `https://<nome-do-app>.azurewebsites.net`

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| [app.py](./app.py) | API RESTful em Flask |
| [requirements.txt](./requirements.txt) | Dependências (Flask + Gunicorn) |
| [startup.txt](./startup.txt) | Comando de inicialização usado pela Azure |
| [postman_collection.json](./postman_collection.json) | Coleção do Postman para testar os endpoints |
