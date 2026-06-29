# 📄 Cloud Document Platform

A cloud-native Document Management Platform built using **FastAPI**, **PostgreSQL**, **Docker**, **Terraform**, **Amazon Web Services (AWS)**, and **Kubernetes**.

This project is designed as a hands-on learning and portfolio application that demonstrates modern backend development, cloud infrastructure provisioning, containerization, and orchestration.

---

## 🚀 Project Overview

The Cloud Document Platform allows authenticated users to:

* Register and log in using JWT authentication
* Upload documents
* Store document metadata in PostgreSQL
* Download and delete documents
* Secure APIs using JWT Bearer tokens
* Deploy using Docker and Kubernetes
* Provision AWS infrastructure using Terraform

Future enhancements include:

* Amazon S3 for document storage
* Amazon EKS deployment
* AWS WAF protection
* GitHub Actions CI/CD
* Monitoring with Prometheus & Grafana
* Application logging with CloudWatch

---

# 🏗️ Architecture

```text
                Client
                   │
                   ▼
             FastAPI Backend
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 Authentication         Document Service
         │                   │
         ▼                   ▼
 PostgreSQL          Local Storage / Amazon S3
```

Future AWS Architecture

```text
                 Internet
                     │
                     ▼
               AWS WAF
                     │
                     ▼
        Application Load Balancer
                     │
                     ▼
              Amazon EKS Cluster
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     FastAPI Pod          FastAPI Pod
                     │
                     ▼
               Amazon RDS
                     │
                     ▼
                Amazon S3
```

---

# 🛠️ Technology Stack

## Backend

* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* Pydantic v2
* JWT Authentication
* Passlib (bcrypt)

## Cloud

* AWS
* Amazon ECR
* Amazon EKS *(In Progress)*
* Amazon S3 *(In Progress)*
* AWS WAF *(Planned)*

## Infrastructure

* Terraform
* Docker
* Docker Compose
* Kubernetes

## DevOps

* Git
* GitHub
* GitHub Actions *(Upcoming)*

---

# 📁 Project Structure

```text
cloud-document-platform/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── dependencies/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── tests/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── infrastructure/
│   ├── terraform/
│   │   ├── modules/
│   │   ├── ecr/
│   │   ├── eks/
│   │   ├── network/
│   │   ├── waf/
│   │   └── remote-state/
│
├── kubernetes/
│
├── frontend/        (Coming Soon)
│
├── docs/
│
└── README.md
```

---

# ✨ Features

## Authentication

* User Registration
* User Login
* JWT Authentication
* Password Hashing
* Protected Endpoints

---

## Document Management

* Upload Documents
* Download Documents
* Delete Documents
* Store Metadata
* Local File Storage

---

## Infrastructure

* Modular Terraform
* Remote State
* S3 Backend
* DynamoDB State Locking
* AWS ECR Repository

---

# 🐳 Running Locally

## Clone Repository

```bash
git clone https://github.com/<your-username>/cloud-document-platform.git

cd cloud-document-platform/backend
```

---

## Create Virtual Environment

```bash
python3.12 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create

```text
.env
```

Example

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/document_platform

SECRET_KEY=your-secret-key

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Start PostgreSQL

```bash
docker compose up -d postgres
```

---

## Run Database Migrations

```bash
alembic upgrade head
```

---

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# ☁️ Terraform

Initialize

```bash
terraform init
```

Plan

```bash
terraform plan
```

Apply

```bash
terraform apply
```

---

# 📌 AWS Services

| Service           | Status |
| ----------------- | ------ |
| IAM               | ✅      |
| VPC               | ✅      |
| EC2               | ✅      |
| Security Groups   | ✅      |
| Terraform Modules | ✅      |
| S3 Backend        | ✅      |
| DynamoDB Locking  | ✅      |
| ECR               | ✅      |
| EKS               | 🚧     |
| WAF               | 🚧     |
| S3 File Storage   | 🚧     |
| RDS               | 🚧     |

---

# 🛣️ Roadmap

### Phase 1

* ✅ FastAPI
* ✅ PostgreSQL
* ✅ Alembic
* ✅ SQLAlchemy

### Phase 2

* ✅ JWT Authentication
* ✅ Docker
* ✅ Docker Compose

### Phase 3

* ✅ Document Upload
* ✅ Amazon ECR

### Phase 4

* 🚧 Kubernetes
* 🚧 Amazon EKS

### Phase 5

* 🚧 Amazon S3
* 🚧 AWS WAF
* 🚧 GitHub Actions
* 🚧 Monitoring
* 🚧 Logging

---

# 🎯 Learning Objectives

This project demonstrates:

* Backend API Development
* Clean Architecture
* Repository Pattern
* Service Layer Pattern
* JWT Authentication
* Docker Containerization
* Kubernetes Deployments
* Terraform Infrastructure as Code
* AWS Cloud Services
* DevOps Best Practices
* CI/CD Pipelines

---

# 📚 Future Improvements

* Role-Based Access Control (RBAC)
* Multi-Tenant Architecture
* Document Versioning
* Virus Scanning
* Presigned S3 URLs
* Email Notifications
* Audit Logging
* Prometheus Metrics
* Grafana Dashboards
* CloudWatch Integration

---

# 👨‍💻 Author

**Yogesh**

Building this project as a complete cloud-native application to gain hands-on experience with:

* Python
* FastAPI
* Docker
* Kubernetes
* Terraform
* AWS
* DevOps
