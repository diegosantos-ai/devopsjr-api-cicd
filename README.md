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
- Docker Hub

## Estrutura inicial
- `app/` código da aplicação
- `tests/` testes
- `.github/workflows/` automações CI/CD
- `Dockerfile` definição da imagem
- `.dockerignore` controle de contexto de build
- `requirements.txt` dependências Python
- `README.md` documentação do projeto

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

## Execução com Docker

### 1. Build da imagem

```bash
docker build -t devopsjr-api-cicd:local .
```

### 2. Subir o container

```bash
docker run --rm -p 8000:8000 devopsjr-api-cicd:local
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

### 3. Validar endpoints com curl

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/info
```

### Respostas esperadas

#### Health

```json
{"status":"ok","service":"devopsjr-api-cicd"}
```

#### Info

```json
{"project":"devopsjr-api-cicd","version":"0.1.0","environment":"dev","timestamp":"<timestamp-utc>"}
```

### Observação operacional

Se a porta `8000` já estiver em uso no host, o container não conseguirá iniciar.

Nesse caso:

* pare o processo local que estiver usando a porta
* ou publique o container em outra porta, por exemplo `8001:8000`

## Endpoints

* `GET /health`
* `GET /info`

## Fluxo do projeto

O fluxo atual do projeto segue esta sequência:

1. desenvolvimento da aplicação localmente
2. validação local com `uvicorn` e `curl`
3. build da imagem Docker
4. validação da execução em container
5. push do código para o GitHub
6. execução automática da pipeline no GitHub Actions
7. build automático da imagem Docker
8. publicação automática da imagem no Docker Hub quando há alteração na `main`

Esse fluxo garante que a aplicação seja validada localmente, empacotada de forma reproduzível e publicada automaticamente como artefato utilizável.

## Arquitetura

A arquitetura atual do projeto é simples e focada em demonstrar uma base DevOps funcional.

### Componentes

* **FastAPI**: responsável pelos endpoints da aplicação
* **Uvicorn**: servidor ASGI usado para execução local e no container
* **Docker**: empacotamento da aplicação
* **GitHub Actions**: automação de validação, build e publicação
* **Docker Hub**: registry para armazenamento e distribuição da imagem

### Endpoints disponíveis

* `GET /health`: valida se o serviço está respondendo
* `GET /info`: retorna informações básicas da aplicação

### Estrutura de alto nível

* `app/main.py`: aplicação principal
* `Dockerfile`: definição da imagem
* `.github/workflows/ci.yml`: pipeline CI/CD
* `requirements.txt`: dependências Python
* `.dockerignore`: controle de contexto de build
* `README.md`: documentação do projeto

## Pipeline

A pipeline atual está configurada no GitHub Actions e possui três etapas principais:

### 1. `validate`

Executa validação básica da aplicação:

* checkout do código
* configuração do Python
* instalação das dependências
* import da aplicação para validação estrutural

### 2. `docker-build`

Executa o build da imagem Docker:

* checkout do código
* configuração do Docker Buildx
* build da imagem sem publicação

### 3. `docker-publish`

Executa a publicação automática da imagem no Docker Hub:

* roda somente na branch `main`
* faz login no Docker Hub com secrets do repositório
* builda e publica as tags `latest` e `0.1.0`

### Regras atuais da pipeline

* branches `feature/**` executam validação e build
* a branch `main` executa validação, build e publicação
* a publicação não acontece em branches de feature

## Troubleshooting

### Erro: porta 8000 já está em uso

**Causa provável:** outro processo local já está usando a porta, como `uvicorn` em execução.

**Como validar:**

```bash
ss -ltnp | grep 8000
```

**Como corrigir:**

* parar o processo local com `Ctrl + C`
* ou usar outra porta no `docker run`, por exemplo `8001:8000`

### Erro: container não sobe por conflito de porta

**Causa provável:** a aplicação já está rodando localmente na mesma porta publicada pelo Docker.

**Como corrigir:**

* encerrar a execução local
* repetir o `docker run`
* ou publicar em outra porta

### Erro: workflow falha por arquivo não encontrado

**Causa provável:** o commit executado não continha ainda o arquivo do workflow no estado esperado.

**Como validar:**

* verificar branch
* verificar commit da execução
* verificar se o arquivo existia naquele snapshot

### Build Docker com contexto muito grande

**Causa provável:** ausência ou problema no `.dockerignore`.

**Como validar:**
observar a linha:

```text
Sending build context to Docker daemon ...
```

**Como corrigir:**

* revisar `.dockerignore`
* remover arquivos e diretórios desnecessários do contexto de build

### Push para Docker Hub não executa na feature

**Causa provável:** comportamento esperado da pipeline.

**Motivo:** o job de publicação está restrito à branch `main`.

**Trecho responsável:**

```yaml
if: github.ref == 'refs/heads/main'
```

## Próximos passos

1. revisar e finalizar a documentação do projeto
2. adicionar testes básicos dos endpoints
3. incluir etapa de testes na pipeline
4. preparar a apresentação final do projeto para portfólio
5. evoluir a aplicação com melhorias funcionais simples

````

