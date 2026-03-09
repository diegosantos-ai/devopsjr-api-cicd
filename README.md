# devopsjr-api-cicd

Projeto de portfólio DevOps Jr com foco em construção de uma API simples, containerização com Docker e automação inicial com GitHub Actions.

## Objetivo
Este projeto existe para demonstrar a construção, containerização e validação de uma API simples com base para CI/CD.

## Escopo inicial
- endpoint `/health`
- endpoint `/info`
- execução local com uvicorn
- containerização com Docker
- pipeline CI inicial

## Stack
- Python 3
- FastAPI
- Uvicorn
- Docker
- GitHub Actions

## Estrutura inicial
- `app/` código da aplicação
- `tests/` testes
- `.github/workflows/` automações CI

## Execução local

### 1. Criar e ativar o ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
````

### 2. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Subir a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

## Validação local

### Validar endpoint de saúde

```bash
curl http://127.0.0.1:8000/health
```

Resposta esperada:

```json
{"status":"ok","service":"devopsjr-api-cicd"}
```

### Validar endpoint de informações

```bash
curl http://127.0.0.1:8000/info
```

Resposta esperada:

```json
{"project":"devopsjr-api-cicd","version":"0.1.0","environment":"dev","timestamp":"<timestamp-utc>"}
```

## Endpoints

* `GET /health`
* `GET /info`

## Execução com Docker

### 1. Build da imagem
```bash
docker build -t devopsjr-api-cicd:local .
````

### 2. Subir o container

```bash id="4xmr54"
docker run --rm -p 8000:8000 devopsjr-api-cicd:local
```

A aplicação ficará disponível em:

```text id="3rj3t0"
http://127.0.0.1:8000
```

### 3. Validar endpoints com curl

```bash id="h6at9n"
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/info
```

### Respostas esperadas

#### Health

```json id="yns30i"
{"status":"ok","service":"devopsjr-api-cicd"}
```

#### Info

```json id="pv2l0g"
{"project":"devopsjr-api-cicd","version":"0.1.0","environment":"dev","timestamp":"<timestamp-utc>"}
```

### Observação operacional

Se a porta `8000` já estiver em uso no host, o container não conseguirá iniciar.

Nesse caso:

* pare o processo local que estiver usando a porta
* ou publique o container em outra porta, por exemplo `8001:8000`

## Próximos passos

1. revisar README com instruções de execução em Docker
2. publicar repositório no GitHub
3. validar workflow CI no GitHub Actions
4. preparar push de imagem para Docker Hub




```
