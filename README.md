# Employee Management System – CI/CD Pipeline

## Project Title

Employee Management System Using FastAPI and CI/CD

## Requirements Covered

- FastAPI employee management application
- Authentication
- Employee CRUD operations
- Git and GitHub
- Jenkins CI/CD
- Automated testing
- Versioned artifacts
- Docker
- Kubernetes deployment
- Health checks
- Monitoring
- Security validation

## Local Run

python -m venv venv

Windows:

venv\Scripts\activate

Install:

python -m pip install -r requirements.txt

Start:

uvicorn app.main:app --reload

Swagger:

http://127.0.0.1:8000/docs

Health:

http://127.0.0.1:8000/health

Metrics:

http://127.0.0.1:8000/metrics

## Testing

python -m pytest

## Security

python -m pip_audit

## Docker

docker build -t employee-management:1.0.0 .

docker run -p 8000:8000 employee-management:1.0.0

## Docker Compose

docker-compose up --build

## Kubernetes

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

kubectl get pods
kubectl get services
kubectl get deployment

## Jenkins

Change the GitHub URL in Jenkinsfile:

https://github.com/YOUR_USERNAME/Employee-Management.git

Then create a Jenkins Pipeline job and run the pipeline.
