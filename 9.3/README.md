# Exercício 9.3 - Deploy na Nuvem

Aplicação Flask "Hello World" hospedada na Azure App Services (tier Free) com deploy automático via GitHub Actions.

## Itens do exercício

- Implementar uma aplicação "Hello World" em Flask
- Criar um repositório no GitHub para hospedar o código
- Criar um ambiente para hospedagem na nuvem via App Services
- Utilizar o tier Free para não gastar créditos
- Configurar um pipeline de CI/CD do GitHub para a Azure
- Testar a página publicada

## Como rodar localmente

```bash
pip install -r requirements.txt
python app.py
```

A aplicação sobe em `http://localhost:5000`

## Deploy na Azure

### 1. Criar o App Service

1. Acesse [portal.azure.com](https://portal.azure.com)
2. Pesquise **App Services** → **Create**
3. Configure:
   - **Runtime stack:** Python 3.11
   - **Pricing plan:** Free F1
   - **Operating System:** Linux

### 2. Configurar CI/CD com GitHub

1. Dentro do App Service criado, abra **Deployment Center**
2. Source: **GitHub**
3. Autorize a conta e selecione:
   - Repositório: `lab09-apis-e-microservicos`
   - Branch: `master`
4. Salve — o pipeline do GitHub Actions é criado automaticamente

### 3. Configurar o startup command

Em **Configuration → General settings → Startup Command**, coloque:

```
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

Esse comando também está disponível em [`startup.txt`](./startup.txt).

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| [app.py](./app.py) | Aplicação Flask Hello World |
| [requirements.txt](./requirements.txt) | Dependências (Flask + Gunicorn) |
| [startup.txt](./startup.txt) | Comando de inicialização usado pela Azure |
