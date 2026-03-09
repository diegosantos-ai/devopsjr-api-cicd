# devopsjr-api-cicd

Projeto de portfólio DevOps criado para demonstrar a construção, validação, containerização e automação inicial de CI/CD de uma API simples com FastAPI.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-API-009688?style=flat-square&logo=fastapi&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img alt="Pytest" src="https://img.shields.io/badge/Pytest-Tests-0A9EDC?style=flat-square&logo=pytest&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white">
  <img alt="Release" src="https://img.shields.io/badge/Release-v0.1.0-1f2328?style=flat-square">
</p>

<p align="left">
  <a href="https://github.com/diegosantos-ai/devopsjr-api-cicd/releases/tag/v0.1.0">
    <img alt="Release" src="https://img.shields.io/badge/Release-v0.1.0-1f883d?style=for-the-badge">
  </a>
  <a href="https://github.com/diegosantos-ai/devopsjr-api-cicd/actions">
    <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-Workflow-24292f?style=for-the-badge&logo=githubactions&logoColor=white">
  </a>
  <a href="COLE_AQUI_O_LINK_DO_DOCKER_HUB">
    <img alt="Docker Hub" src="https://img.shields.io/badge/Docker_Hub-Image-0db7ed?style=for-the-badge&logo=docker&logoColor=white">
  </a>
</p>

---

## Visão geral

O `devopsjr-api-cicd` foi desenvolvido como um projeto de portfólio com foco em práticas fundamentais de DevOps aplicadas a uma API simples.

A proposta não foi apenas fazer a aplicação funcionar, mas conduzir o projeto com método, incluindo:

- estruturação do repositório
- execução local validada
- testes automatizados
- containerização com Docker
- integração contínua com GitHub Actions
- publicação automatizada de imagem no Docker Hub
- versionamento com tag Git e release no GitHub

---

## Objetivo

Demonstrar um fluxo inicial de trabalho DevOps usando uma aplicação simples, cobrindo desde a base do projeto até a entrega versionada de um artefato publicável.

Este projeto foi construído para consolidar práticas como:

- organização de código
- validação antes de merge
- automação de pipeline
- publicação de imagem versionada
- fechamento formal de release

---

## Stack

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub Actions
- Docker Hub

---

## Resultados alcançados

Ao final da versão `v0.1.0`, o projeto já demonstra:

- API funcional com endpoints `/`, `/health` e `/info`
- execução local validada
- testes automatizados com Pytest
- build Docker validado
- execução da aplicação em container
- pipeline CI no GitHub Actions
- publicação automática de imagem no Docker Hub pela branch `main`
- versionamento inicial com tag `v0.1.0`
- release inicial publicada no GitHub

---

## Estrutura do projeto

```text
.
├── app/
│   └── main.py
├── tests/
│   ├── conftest.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
````

---

## Arquitetura da aplicação

A aplicação foi mantida propositalmente simples para destacar a base operacional e de automação.

### Componentes principais

* **FastAPI** como framework da API
* **Uvicorn** para execução local
* **Pytest** para validação automatizada
* **Docker** para empacotamento
* **GitHub Actions** para CI e publicação
* **Docker Hub** como registry de imagem

### Fluxo resumido

1. desenvolvimento local em branch de contexto
2. validação local da aplicação e dos testes
3. merge na `main`
4. execução do workflow no GitHub Actions
5. build da imagem Docker
6. publicação automática no Docker Hub
7. criação de tag e release no GitHub

---

## Endpoints

### `GET /`

Retorna a mensagem inicial da aplicação.

### `GET /health`

Retorna o status de saúde da API.

### `GET /info`

Retorna informações básicas da aplicação, como nome, versão e ambiente.

---

## Execução local

### 1. Clonar o repositório

```bash
git clone https://github.com/diegosantos-ai/devopsjr-api-cicd.git
cd devopsjr-api-cicd
```

### 2. Criar e ativar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

### 5. Acessar localmente

* API: `http://127.0.0.1:8000`
* Docs interativas: `http://127.0.0.1:8000/docs`

---

## Variáveis de ambiente

Atualmente a aplicação utiliza a variável abaixo:

* `APP_ENV`

Exemplo de execução com ambiente definido:

```bash
APP_ENV=dev uvicorn app.main:app --reload
```

Se a variável não for definida, a aplicação usa o valor padrão configurado no código.

---

## Testes

Para executar os testes localmente:

```bash
pytest
```

Os testes cobrem a validação básica dos endpoints principais da aplicação.

---

## Execução com Docker

### Build da imagem

```bash
docker build -t devopsjr-api-cicd:local .
```

### Subir o container

```bash
docker run --rm -p 8000:8000 devopsjr-api-cicd:local
```

### Acessar

* API: `http://127.0.0.1:8000`
* Docs interativas: `http://127.0.0.1:8000/docs`

---

## Pipeline CI/CD

O projeto possui um workflow em `.github/workflows/ci.yml` com responsabilidade de:

* instalar dependências
* executar testes automatizados
* validar a aplicação no pipeline
* construir a imagem Docker
* publicar a imagem no Docker Hub quando a branch é `main`

### Comportamento do pipeline

* em branches de feature: validação e testes
* na `main`: validação, testes, build e publicação da imagem

---

## Imagens publicadas

A imagem do projeto é publicada com as tags:

* `0.1.0`
* `latest`

> Atualize o botão e o link do Docker Hub no topo deste README com a URL real do seu repositório de imagem.

---

## Versionamento e release

A primeira versão estável do projeto foi marcada com:

* **tag Git:** `v0.1.0`
* **release GitHub:** `Projeto 01 - Release inicial v0.1.0`

Essa release representa o primeiro fechamento formal do projeto com base funcional, testes, containerização e automação de pipeline.

---

## Evidências do projeto

Durante a conclusão da release inicial, foram registradas evidências visuais do projeto, incluindo:

* visão geral do repositório no GitHub
* release `v0.1.0` publicada
* execução bem-sucedida do workflow no GitHub Actions
* imagem publicada no Docker Hub
* aplicação rodando localmente
* evidência funcional da API e testes executados

Essas evidências serão utilizadas posteriormente na página de portfólio.

---

## Fluxo de trabalho adotado

Este projeto foi conduzido seguindo um padrão de execução com foco em previsibilidade e validação:

* `main` como branch principal
* uma branch por contexto de trabalho
* merge somente após validação real
* um card por vez em andamento
* fechamento de versão com tag e release

---

## Troubleshooting

### Erro: `ModuleNotFoundError: No module named 'app'`

Causa mais provável: execução do comando fora da raiz do projeto.

Validação:

```bash
pwd
```

Correção:

```bash
cd /caminho/do/projeto
uvicorn app.main:app --reload
```

### A aplicação não responde na porta esperada

Valide se o processo está rodando corretamente e se a porta `8000` está livre.

### Os testes falham por problema de import

Verifique se a estrutura do projeto está preservada e se o ambiente virtual correto está ativado.

---

## Próximos passos

Evoluções possíveis para próximas versões:

* criação de Makefile com comandos operacionais
* melhoria do Dockerfile para otimização de camadas e cache
* proteção básica da branch `main`
* definição de estratégia inicial de deploy
* publicação da aplicação em ambiente externo

---

## Links

* Repositório: `https://github.com/diegosantos-ai/devopsjr-api-cicd`
* Release inicial: `https://github.com/diegosantos-ai/devopsjr-api-cicd/releases/tag/v0.1.0`
* Actions: `https://github.com/diegosantos-ai/devopsjr-api-cicd/actions`
* Docker Hub: `https://hub.docker.com/repository/docker/santosdiegoj86/devopsjr-api-cicd/general`

---

## Sobre o projeto

Este repositório faz parte de uma trilha prática de projetos voltados para evolução profissional em DevOps, com foco em automação, infraestrutura, validação, versionamento e boas práticas operacionais.

````


