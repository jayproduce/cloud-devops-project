# 07 - CI/CD avec GitHub Actions

## Objectif
Automatiser le build et les tests du projet FastAPI + Docker à chaque push sur `main`.

## Workflow CI (`ci.yml`)
Déclenché à chaque push ou pull request sur `main`.

### Étapes du pipeline
1. **Checkout** du code source
2. **Build** de l'image Docker (`fastapi-app`)
3. **Start containers** via Docker Compose
4. **Wait** 10s que l'API soit prête
5. **Test API POST** `/numbers` avec curl
6. **Test API GET** `/numbers` avec curl
7. **Stop containers**

## Badge
![CI](https://github.com/jayproduce/cloud-devops-project/actions/workflows/ci.yml/badge.svg)

## Concepts clés
- Pipeline CI/CD
- GitHub Actions (YAML workflow)
- Test d'API automatisé avec curl
- Build et orchestration Docker
