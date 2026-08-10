# 🚗 Vehicle MLOps — End-to-End Machine Learning Platform

> A production-oriented MLOps project for training, validating, evaluating, deploying, and serving vehicle-related machine-learning models—backed by MongoDB Atlas, AWS S3, Docker, and GitHub Actions.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20ECR%20%7C%20EC2-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)

## ✨ Why this project?

This repository demonstrates how a machine-learning solution moves beyond a notebook and into a repeatable, deployable system. It applies practical software-engineering and cloud-native practices to the full ML lifecycle:

- **Data ingestion** from MongoDB Atlas into a reproducible local artifact workflow.
- **Data validation** driven by an explicit YAML schema.
- **Feature engineering and transformation** packaged as pipeline components.
- **Model training, evaluation, and registry workflows** with AWS S3 integration.
- **Inference serving** through a web application and prediction pipeline.
- **Automated container delivery** using Docker, Amazon ECR, EC2, and GitHub Actions.

## 🧰 Tech Stack

| Area | Tools & services |
|---|---|
| Language & packaging | Python 3.12+, `pyenv`, virtual environments, `pip`, `setup.py`, `pyproject.toml` |
| Data platform | MongoDB Atlas, Pandas, Jupyter notebooks |
| ML workflow | EDA, feature engineering, schema-based validation, training, evaluation, prediction pipeline |
| Reliability | Custom logging and exception handling |
| Cloud | AWS IAM, S3, ECR, EC2 (Ubuntu) |
| Delivery | Docker, GitHub Actions, self-hosted GitHub runner |
| Web application | `app.py`, static assets, templates, training and prediction routes |

## 🏗️ MLOps Architecture

```text
MongoDB Atlas
     │
     ▼
Data Ingestion ──► Data Validation ──► Data Transformation ──► Model Trainer
     │                    │                      │                    │
     └──────────── artifacts / logs / schema ────┴────────────────────┘
                                                                        │
                                                                        ▼
                                                          Model Evaluation
                                                                        │
                                         previous model ◄── AWS S3 ───► approved model
                                                                        │
                                                                        ▼
                                                               Model Pusher
                                                                        │
                                                                        ▼
                                             Prediction Pipeline + Web Application
                                                                        │
                                                                        ▼
                              Docker → Amazon ECR → EC2 → GitHub Actions CI/CD
```

## 🔄 ML Pipeline

| Stage | Responsibility |
|---|---|
| **Data Ingestion** | Connects to MongoDB, fetches source records, converts key-value documents to a DataFrame, and produces ingestion artifacts. |
| **Data Validation** | Checks dataset expectations against `config/schema.yaml` and records validation artifacts. |
| **Data Transformation** | Prepares model-ready features and persists preprocessing objects for consistent inference. |
| **Model Trainer** | Trains and serializes the candidate model using the transformed data. |
| **Model Evaluation** | Compares a candidate against the currently registered model using the configured change threshold. |
| **Model Pusher** | Publishes approved model artifacts to the S3 model registry. |
| **Prediction Pipeline** | Loads the required inference assets and serves predictions through the application. |

## 📁 Project Structure

```text
.
├── app.py
├── demo.py
├── setup.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── config/
│   └── schema.yaml
├── notebook/
│   ├── mongoDB_demo.ipynb
│   └── ... dataset and EDA / feature-engineering notebooks
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   ├── configuration/
│   │   ├── mongo_db_connections.py
│   │   └── aws_connection.py
│   ├── data_access/
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   ├── estimator.py
│   │   └── s3_estimator.py
│   ├── aws_storage/
│   ├── pipeline/
│   ├── utils/
│   │   └── main_utils.py
│   ├── logger.py
│   └── exception.py
├── static/
├── templates/
└── .github/workflows/
    └── aws.yaml
```

> The exact package and module names should match the implementation in this repository.

## 🚀 Quick Start

### 1. Create the project scaffold

Run the template script to create the initial project structure:

```bash
python template.py
```

### 2. Configure local package installation

Use `setup.py` and `pyproject.toml` so the project package can be imported locally. See `crashcourse.txt` in this project for packaging notes.

### 3. Create the Python environment

Use `pyenv` to install/select Python and create an isolated environment, then install project dependencies:

```bash
pip install -r requirements.txt
pip list
```

Confirm that the local project package appears in the installed-package list.

### 4. Configure environment variables

Never commit credentials, connection strings, or downloaded cloud-access CSV files. Set secrets locally or through your deployment platform.

**Bash / Zsh**

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@<cluster-url>/..."
echo $MONGODB_URL
```

**PowerShell**

```powershell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@<cluster-url>/..."
echo $env:MONGODB_URL
```

On Windows, the same value may be configured as a user or system environment variable named `MONGODB_URL`.

## 🗄️ MongoDB Atlas Data Setup

1. Create a MongoDB Atlas project and deploy an **M0** cluster.
2. Create a database user with a strong, unique password.
3. Obtain the Python connection string via **Connect → Drivers** and set it as `MONGODB_URL`.
4. Place the dataset in the `notebook/` directory.
5. Open `notebook/mongoDB_demo.ipynb` with the project Python kernel.
6. Run the notebook to upload the dataset to MongoDB.
7. Verify the documents in Atlas using **Browse Collections**.

> **Security note:** Restrict Atlas network access to trusted IP addresses or trusted application networks. Do not expose a database to all IP addresses unless there is a controlled, temporary reason to do so.

## 🔬 Notebooks, Logging & Exceptions

- Use the MongoDB demo notebook to load source data.
- Use the EDA and feature-engineering notebook to investigate distributions, quality issues, and candidate features.
- Validate `logger.py` and `exception.py` through `demo.py` before integrating components.
- Keep generated `artifact/` outputs out of source control by adding them to `.gitignore`.

## ⚙️ Pipeline Development Order

The pipeline is implemented incrementally:

1. Define shared constants and the MongoDB connection configuration.
2. Build the data-access layer to retrieve MongoDB documents and convert them into DataFrames.
3. Add ingestion configuration and artifact entities, then execute the training pipeline.
4. Complete `utils/main_utils.py` and document the input-data contract in `config/schema.yaml`.
5. Add validation, transformation, and training components with their corresponding configuration and artifact entities.
6. Add estimators required for training/inference and S3 model interactions.
7. Implement model evaluation and model pusher components.
8. Complete the prediction pipeline and wire it into `app.py`.

## ☁️ AWS Model Registry

AWS S3 is used as the model registry for retrieving and publishing model artifacts.

| Configuration | Example value |
|---|---|
| Region | `us-east-1` |
| Model bucket | `my-model-mlopsproj` |
| Registry prefix | `model-registry` |
| Evaluation change threshold | `0.02` |

Set AWS credentials securely through your shell, an IAM role, or GitHub Actions secrets. Grant only the permissions necessary for the resources used by this project; avoid committing access keys or embedding secrets in source code.

## 🐳 Containerization

Build and run the application locally with Docker:

```bash
docker build -t vehicle-mlops .
docker run --rm -p 5080:5080 --env-file .env vehicle-mlops
```

The `Dockerfile` defines the runtime image, while `.dockerignore` keeps unnecessary files and sensitive local content out of the image build context.

## 🔁 CI/CD Deployment

The delivery workflow is defined in `.github/workflows/aws.yaml` and is triggered by a repository commit and push.

**Deployment path:**

```text
GitHub push → GitHub Actions → Docker image build → Amazon ECR → EC2 deployment
```

### Required GitHub Actions secrets

Configure these repository secrets under **Settings → Secrets and variables → Actions**:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
```

### EC2 runtime

A Ubuntu EC2 instance hosts the container and can be connected to GitHub as a self-hosted runner. Install Docker, configure the runner from the repository’s Actions settings, and keep the runner process available for workflow execution.

For public application access, allow only the specific application port used by the container (for example, `5080`) in the EC2 security group—and restrict source ranges whenever possible.

## 🖥️ Application Routes

| Route | Purpose |
|---|---|
| `/` | Application entry point / prediction interface |
| `/training` | Starts the model-training workflow |

Once deployed, access the app at:

```text
http://<EC2-public-ip>:5080
```

## 🔐 Security Practices

- Keep `MONGODB_URL`, AWS keys, `.env` files, model artifacts, and downloaded credentials out of Git.
- Prefer IAM roles and narrowly scoped IAM policies over long-lived administrator credentials.
- Restrict MongoDB Atlas and EC2 inbound access to known networks whenever feasible.
- Rotate credentials immediately if they are exposed.
- Validate all incoming data against `config/schema.yaml` before model training.

## 🎯 Recruiter Highlights

This project showcases practical experience with:

- Designing modular, artifact-driven ML pipelines
- Working with MongoDB documents and tabular ML datasets
- Building data validation and transformation stages
- Creating reusable estimators and prediction workflows
- Managing model promotion and registry storage in AWS S3
- Containerizing ML applications with Docker
- Implementing CI/CD with GitHub Actions, ECR, and EC2
- Applying environment-based configuration and cloud-security fundamentals

## 📌 Getting Started Checklist

- [ ] Run `template.py`
- [ ] Install the local package and dependencies
- [ ] Set `MONGODB_URL`
- [ ] Upload the dataset through the MongoDB notebook
- [ ] Run ingestion and validate artifacts
- [ ] Complete validation, transformation, training, evaluation, and pusher stages
- [ ] Configure the S3 model registry
- [ ] Run the web application locally
- [ ] Build the Docker image
- [ ] Configure GitHub secrets and deploy through CI/CD

---

Built to demonstrate the path from raw data to a reproducible, cloud-deployed machine-learning service.
