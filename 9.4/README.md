# Exercício 9.4 - API RESTful na Nuvem

API RESTful Flask hospedada na Azure App Services com deploy automático via GitHub Actions.

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

## Deploy

Push na branch `master` dispara o pipeline do GitHub Actions que faz deploy no Azure App Services automaticamente.

O `gunicorn` é usado como servidor de produção (configurado em `startup.txt`).
