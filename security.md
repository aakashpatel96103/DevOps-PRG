# Security Validation

Run dependency security validation:

python -m pip_audit

Optional Docker image scan:

trivy image employee-management:1.0.0

The application uses JWT authentication and protected employee APIs.
