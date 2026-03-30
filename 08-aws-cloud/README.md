# 08 - Deploiement Cloud

## Environnement simule : Ubuntu 24.04 (KillerCoda)

## Etapes effectuees

1. Mise a jour du systeme
   sudo apt update -y

2. Installation de Docker
   curl -fsSL https://get.docker.com | sh

3. Installation de docker-compose
   sudo apt install docker-compose -y

4. Clonage du projet
   git clone https://github.com/jayproduce/cloud-devops-project.git

5. Lancement de l application
   cd cloud-devops-project/06-docker
   docker compose up -d

6. Tests API reussis
   - GET /health  ok
   - POST /numbers  valeur 42 creee
   - GET /numbers  liste retournee

## Stack deployee
- FastAPI + PostgreSQL via Docker
- Pipeline CI/CD GitHub Actions (badge passing)
