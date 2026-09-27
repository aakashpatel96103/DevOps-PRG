pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aakashpatel96103/DevOps-PRG.git'

                echo 'Source code checked out successfully.'
            }
        }

        stage('Environment') {
            steps {
                bat 'python --version'
                bat 'docker --version'
                bat 'kubectl version --client'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Automated Testing') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Security Validation') {
            steps {
                bat 'python -m pip_audit'
            }
        }

        stage('Versioned Artifact') {
            steps {
                bat 'if not exist artifacts mkdir artifacts'
                bat 'tar -a -c -f artifacts\employee-management-1.0.%BUILD_NUMBER%.zip app tests requirements.txt Dockerfile'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t employee-management:1.0.%BUILD_NUMBER% .'
                bat 'docker tag employee-management:1.0.%BUILD_NUMBER% employee-management:latest'
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                bat 'kubectl apply -f k8s\deployment.yaml'
                bat 'kubectl apply -f k8s\service.yaml'
                bat 'kubectl set image deployment/employee-management employee-management=employee-management:1.0.%BUILD_NUMBER%'
                bat 'kubectl rollout status deployment/employee-management'
            }
        }

        stage('Health Check') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get services'
                bat 'kubectl get deployment'
            }
        }

        stage('Monitoring') {
            steps {
                bat 'kubectl get pods -o wide'
                echo 'Basic application and Kubernetes monitoring completed.'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline Completed Successfully.'
        }

        failure {
            echo 'Pipeline Failed. Check Console Output.'
        }
    }
}
