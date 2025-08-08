Proyecto Final DevOps – AWS Free Tier
Este proyecto despliega una aplicación web con FastAPI, utilizando servicios gratuitos de AWS, infraestructura como código con Terraform, y automatización del ciclo de vida con GitHub Actions (CI/CD).

 Objetivo
Desplegar automáticamente una aplicación web con:
- Backend en FastAPI (Python)
- Infraestructura definida en Terraform
- Automatización CI/CD con GitHub Actions
- Arquitectura completamente sobre el Free Tier de AWS

Arquitectura
Usuario → DNS / IP Pública
        ↓
    [ECS Fargate]
        ↓
 [Contenedor FastAPI]
        ↓
       [RDS PostgreSQL]

Servicios AWS Utilizados:
- Amazon ECS (Fargate)
- Amazon ECR
- Amazon RDS (PostgreSQL)
- IAM
- VPC/Subnet pública
- GitHub Actions

 Estructura del Proyecto
proyecto-final-devops/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── Dockerfile
├── infra/
│   ├── main.tf
│   ├── vpc.tf
│   ├── rds.tf
│   ├── ecs.tf
│   ├── ecr.tf
│   ├── iam.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
└── .github/
    └── workflows/
        ├── docker-build.yml
        └── deploy-terraform.yml

 Requisitos
- Cuenta de AWS (Free Tier)
- IAM Role con OIDC habilitado (para GitHub Actions)
- Terraform ≥ v1.4
- GitHub repo configurado
- AWS CLI configurado localmente (opcional)

 Instrucciones de Despliegue
1. Clona el repositorio
git clone https://github.com/<tu-usuario>/proyecto-final-devops.git
cd proyecto-final-devops

2. Configura variables en terraform.tfvars
aws_region  = "us-east-1"
db_username = "postgres"
db_password = "admin12345"

3. Inicializa y despliega Terraform (opcional local)
cd infra
terraform init
terraform apply -auto-approve

4. Ejecución local para desarrollo
   La aplicación FastAPI puede iniciarse sin requerir un servidor PostgreSQL.
   Por defecto se utilizará una base de datos SQLite local.

   ```bash
   cd app
   uvicorn main:app --reload
   ```

   Para usar PostgreSQL, define la variable de entorno `DATABASE_URL` con la URL completa del servidor.

 Automatización CI/CD
GitHub Actions:
- docker-build.yml: Construye y sube imagen Docker a ECR
- deploy-terraform.yml: Despliega infraestructura con Terraform

 Endpoints de la API (FastAPI)
GET /
→ { "message": "¡Hola desde FastAPI en ECS con RDS!" }

 Capturas de Pantalla
- Terraform Apply
- ECS Running Task
- RDS PostgreSQL
*(Agregar capturas en la entrega final)*

 IA utilizada
Durante el desarrollo se utilizó ChatGPT (Codex) para:
- Generación de scripts Terraform
- Creación de workflows
- Asistencia en debugging
- Documentación

 Créditos
Proyecto realizado por Paulina Quiroz
Rol: DevOps Engineer
Curso: AWS

