# Projeto 01 — devopsjr-api-cicd

## Resumo

O `devopsjr-api-cicd` é um projeto de portfólio criado para demonstrar uma base prática de DevOps aplicada a uma API simples, cobrindo estruturação do repositório, containerização, testes automatizados, integração contínua e publicação de imagem em registry.

A proposta do projeto foi construir uma aplicação pequena, mas tratada com critérios reais de trabalho: organização de código, validação local, automação de pipeline, versionamento por release e publicação de artefato.

---

## Objetivo

Demonstrar a construção e evolução de uma API simples com foco em práticas fundamentais de DevOps, incluindo:

- organização inicial do projeto
- execução local validada
- containerização com Docker
- testes automatizados com Pytest
- pipeline CI com GitHub Actions
- publicação automática de imagem no Docker Hub
- versionamento inicial com tag e release no GitHub

---

## Stack utilizada

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub Actions
- Docker Hub

---

## O que foi implementado

### Aplicação
- endpoint `/`
- endpoint `/health`
- endpoint `/info`
- centralização de variáveis da aplicação como nome, versão e ambiente

### Validação local
- execução local da API com Uvicorn
- testes automatizados com Pytest
- validação de leitura de ambiente

### Containerização
- `Dockerfile` para empacotamento da aplicação
- `.dockerignore` para reduzir contexto de build
- build e execução do container validados localmente

### CI/CD
- workflow de CI com GitHub Actions
- execução automática de testes
- build Docker automatizado
- push automático da imagem no Docker Hub a partir da `main`

### Versionamento
- publicação da imagem com tags:
  - `0.1.0`
  - `latest`
- criação da tag Git `v0.1.0`
- criação da release inicial no GitHub

---

## Resultados práticos

Com esse projeto, foi possível demonstrar na prática:

- uso de branch principal e branches de contexto
- validação antes de merge e antes de release
- integração entre aplicação, testes, container e pipeline
- publicação de artefato versionado
- fechamento formal de uma primeira versão estável

---

## Evidências registradas

As evidências visuais do projeto incluem:

- visão geral do repositório no GitHub
- release `v0.1.0` publicada
- execução bem-sucedida do workflow no GitHub Actions
- imagem publicada no Docker Hub
- aplicação rodando localmente
- evidência funcional da API e/ou testes executados com sucesso

---

## Principais aprendizados

Este projeto reforçou práticas importantes de rotina DevOps, como:

- validar o estado atual antes de alterar qualquer coisa
- trabalhar com branch por contexto
- automatizar tarefas repetitivas com critério
- testar localmente antes de depender apenas do pipeline
- tratar release como marco real de entrega, e não só como detalhe visual
- organizar o projeto para ficar apresentável tecnicamente e compreensível para terceiros

---

## Próximas evoluções possíveis

Algumas evoluções planejadas ou possíveis para versões futuras:

- criação de Makefile com comandos operacionais
- melhoria do Dockerfile para otimização de camadas e cache
- definição de estratégia inicial de deploy
- publicação da aplicação em ambiente externo
- validação pública da aplicação publicada

---

## Links

### Repositório
https://github.com/diegosantos-ai/devopsjr-api-cicd

### Release inicial
https://github.com/diegosantos-ai/devopsjr-api-cicd/releases

### Imagem publicada
https://hub.docker.com/repository/docker/santosdiegoj86/devopsjr-api-cicd/general

---

## Descrição curta para portfólio

Projeto de portfólio DevOps com FastAPI, Docker, Pytest, GitHub Actions e Docker Hub, criado para demonstrar a construção, validação, containerização e automação inicial de CI/CD de uma API simples.

---

## Descrição média para portfólio

Desenvolvi o projeto `devopsjr-api-cicd` para consolidar fundamentos práticos de DevOps em um fluxo completo: estruturação de uma API com FastAPI, testes com Pytest, containerização com Docker, pipeline de CI no GitHub Actions e publicação automatizada de imagem no Docker Hub. O projeto também foi versionado com tag Git e release no GitHub, simulando um ciclo inicial de entrega mais próximo de um ambiente real.

---

## Descrição longa para portfólio

O `devopsjr-api-cicd` foi criado como um projeto de portfólio com foco em práticas reais de DevOps aplicadas a uma API simples. A proposta não foi apenas “fazer a aplicação funcionar”, mas conduzir o projeto com método: organizar o repositório, validar execução local, estruturar testes, empacotar com Docker, automatizar validações no GitHub Actions e publicar a imagem resultante no Docker Hub.

Além da parte técnica da aplicação, o projeto também serviu para consolidar hábitos operacionais importantes, como uso de branch por contexto, validação antes de merge, revisão do estado do ambiente antes de mudanças e fechamento formal de versão por meio de tag e release. A release `v0.1.0` representa a primeira entrega estável do projeto e estabelece uma base sólida para evoluções futuras, como melhorias operacionais, otimização de build e deploy inicial.