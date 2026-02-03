# CloudShip 🚢 - End-to-End Kubernetes CI/CD Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue.svg)](https://kubernetes.io)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://python.org)

A comprehensive end-to-end CI/CD platform demonstrating modern DevOps practices with Kubernetes deployment, automated pipelines, and containerized applications.

## 🌟 Features

- **Containerized Application**: Python Flask app packaged in Docker
- **Kubernetes Deployment**: Complete K8s manifests for deployment, service, and ingress
- **CI/CD Pipeline**: GitHub Actions workflow for automated build, test, and deploy
- **Scalable Architecture**: Ready for production with horizontal scaling
- **Ingress Configuration**: External access via Kubernetes Ingress
- **Service Discovery**: Internal communication through Kubernetes Services

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docker.com/get-started) (v20.10+)
- [Kubernetes Cluster](https://kubernetes.io/docs/setup/) (local or cloud)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) configured
- [Python](https://python.org/downloads/) (v3.10+) for local development
- [Git](https://git-scm.com/downloads) for version control

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CloudShip-End-to-End-Kubernetes-CI-CD-Platform.git
cd CloudShip-End-to-End-Kubernetes-CI-CD-Platform
```

### 2. Local Development

```bash
# Install dependencies
cd app
pip install -r requirements.txt

# Run the application locally
python app.py
```

Visit `http://localhost:5000` to see the app running.

### 3. Docker Build

```bash
# Build the Docker image
docker build -t cloudship:latest .

# Run locally with Docker
docker run -p 5000:5000 cloudship:latest
```

## 🐳 Docker Configuration

The `Dockerfile` is optimized for production:

- Uses Python 3.10 slim base image for smaller size
- Multi-stage build for efficient caching
- Non-root user for security
- Exposes port 5000 for the Flask app

## ☸️ Kubernetes Deployment

### Deploy to Kubernetes

```bash
# Apply all Kubernetes manifests
kubectl apply -f k8s/

# Check deployment status
kubectl get deployments
kubectl get services
kubectl get ingress
```

### Manifests Overview

- **deployment.yaml**: Defines the application deployment with 2 replicas
- **service.yaml**: Exposes the app internally on port 80
- **ingress.yaml**: Provides external access via HTTP

### Scaling

```bash
# Scale the deployment
kubectl scale deployment cloudship-deployment --replicas=5
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci-cd.yaml`) automates:

1. **Build**: Docker image creation on code push
2. **Test**: Automated testing (add your tests in future)
3. **Deploy**: Push to Docker Hub and deploy to Kubernetes

### Setup CI/CD

1. Add Docker Hub credentials to GitHub Secrets:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`

2. Configure Kubernetes access (for deployment to cloud clusters)

3. Push to `main` branch to trigger the pipeline

## 📁 Project Structure

```
CloudShip-End-to-End-Kubernetes-CI-CD-Platform/
├── app/
│   ├── app.py                 # Main Flask application
│   └── requirements.txt       # Python dependencies
├── k8s/
│   ├── deployment.yaml        # Kubernetes deployment
│   ├── service.yaml          # Kubernetes service
│   └── ingress.yaml          # Kubernetes ingress
├── .github/
│   └── workflows/
│       └── ci-cd.yaml        # GitHub Actions CI/CD
├── Dockerfile                # Docker build configuration
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

The application supports the following environment variables:

- `PORT`: Server port (default: 5000)
- `HOST`: Server host (default: 0.0.0.0)

### Kubernetes Customization

Update the manifests in `k8s/` directory:

- Change image repository in `deployment.yaml`
- Modify ingress host in `ingress.yaml`
- Adjust resource limits and requests

## 🧪 Testing

```bash
# Run tests (add your test files)
pytest

# Or with coverage
pytest --cov=app
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add tests for new features
- Update documentation as needed
- Ensure Docker builds pass

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

If you have any questions or need help:

- Open an issue on GitHub
- Check the [Kubernetes documentation](https://kubernetes.io/docs/)
- Review [GitHub Actions documentation](https://docs.github.com/en/actions)

## 🎯 Roadmap

- [ ] Add comprehensive test suite
- [ ] Implement health checks
- [ ] Add monitoring with Prometheus
- [ ] Database integration example
- [ ] Multi-environment deployment
- [ ] Helm chart packaging

---

**Happy Shipping with CloudShip! 🚢**
