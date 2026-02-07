# CloudShip 🚢 - End-to-End Kubernetes CI/CD Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue.svg)](https://kubernetes.io)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://python.org)

---

## 📖 Overview

**CloudShip** is a complete, production-ready example of a modern CI/CD pipeline with Kubernetes. It demonstrates industry best practices for containerization, orchestration, and automated deployment. Perfect for learning DevOps concepts or as a template for your own projects!

This platform includes everything you need:
- 🐍 A Python Flask application
- 🐳 Docker containerization with optimized builds
- ☸️ Full Kubernetes deployment manifests
- 🤖 Automated CI/CD with GitHub Actions
- 📦 Ready-to-scale architecture

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| **🐳 Containerized App** | Python Flask application optimized in Docker with multi-stage builds |
| **☸️ Kubernetes-Ready** | Complete K8s manifests for deployment, scaling, and ingress |
| **🤖 CI/CD Automation** | GitHub Actions workflow for build, test, and automatic deployment |
| **📈 Scalable** | Horizontal pod autoscaling ready with resource management |
| **🌐 Ingress Ready** | External HTTP/HTTPS access configured out of the box |
| **🔍 Service Discovery** | Internal Kubernetes DNS for pod-to-pod communication |
| **🔐 Best Practices** | Security, resource limits, health checks included |

---

## 📋 Prerequisites

Make sure you have these tools installed before getting started:

| Tool | Version | Purpose |
|------|---------|---------|
| [Docker](https://docker.com/get-started) | v20.10+ | Build and run containerized apps |
| [Kubernetes Cluster](https://kubernetes.io/docs/setup/) | v1.20+ | Orchestrate containers (local: Minikube/Docker Desktop, cloud: EKS/GKE/AKS) |
| [kubectl](https://kubernetes.io/docs/tasks/tools/) | Latest | Interact with your Kubernetes cluster |
| [Python](https://python.org/downloads/) | v3.10+ | Run the application locally |
| [Git](https://git-scm.com/downloads) | Latest | Clone and manage the repository |

**Quick check:**
```bash
docker --version
kubectl version --client
python --version
git --version
```

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/CloudShip-End-to-End-Kubernetes-CI-CD-Platform.git
cd CloudShip-End-to-End-Kubernetes-CI-CD-Platform
```

### Step 2: Run Locally (Python)

Get the application running on your machine without Docker:

```bash
# Navigate to the app directory
cd app

# Install Python dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

Open your browser and visit **`http://localhost:5000`** to see the app! 🎉

### Step 3: Containerize with Docker

Build and run the app inside a Docker container:

```bash
# Build the Docker image
docker build -t cloudship:latest .

# Run the container
docker run -p 5000:5000 cloudship:latest

# Visit http://localhost:5000
```

**Tips:**
- Use `-d` flag to run in detached mode: `docker run -d -p 5000:5000 cloudship:latest`
- Use `docker logs <container-id>` to see log output
- Use `docker ps` to list running containers

### Step 4: Deploy to Kubernetes

Deploy the application to your Kubernetes cluster:

```bash
# Apply all Kubernetes manifests (deployment, service, ingress)
kubectl apply -f k8s/

# Watch the deployment progress
kubectl get deployments -w

# Verify all resources are created
kubectl get pods
kubectl get svc
kubectl get ingress
```

**Check your app is running:**
```bash
# Port forward to access locally (without ingress)
kubectl port-forward svc/cloudship-service 5000:80

# Visit http://localhost:5000
```

---

## 🐳 Docker Configuration

The `Dockerfile` is optimized for production deployments:

```dockerfile
# Multi-stage build for efficiency
FROM python:3.10-slim as base
# Installs dependencies only when needed

FROM base as final
# Non-root user for security
USER app
EXPOSE 5000
CMD ["python", "app.py"]
```

**Why this approach:**
- ✅ **Small image size** - Uses slim Python image
- ✅ **Fast builds** - Multi-stage caching
- ✅ **Secure** - Runs as non-root user
- ✅ **Optimized layers** - Dependencies cached separately

---

## ☸️ Kubernetes Deep Dive

### Understanding the Manifests

Your Kubernetes configuration files in the `k8s/` directory:

#### 1. **deployment.yaml**
Defines how your app runs in Kubernetes:
- **Replicas**: 2 instances for high availability
- **Container**: Uses your Docker image
- **Resources**: CPU and memory limits
- **Environment**: Configuration via ConfigMaps and Secrets

```bash
# View deployment details
kubectl describe deployment cloudship-deployment

# View pod logs
kubectl logs <pod-name>
```

#### 2. **service.yaml**
Exposes your app inside the cluster:
- **Type**: ClusterIP (internal-only) or LoadBalancer (external)
- **Port**: 80 → forwards to port 5000 in containers
- **Selector**: Routes traffic to pods with matching labels

```bash
# Check service status
kubectl get svc cloudship-service
```

#### 3. **ingress.yaml**
Provides external HTTP access:
- **Host**: Maps domain to service
- **Path**: Routes traffic based on URL paths
- **TLS-ready**: Supports HTTPS setup

```bash
# Verify ingress configuration
kubectl describe ingress cloudship-ingress

# Get ingress IP (may take a minute)
kubectl get ingress
```

### Scaling Your Application

Need more instances? Scale dynamically:

```bash
# Scale to 5 replicas
kubectl scale deployment cloudship-deployment --replicas=5

# Watch the new pods spin up
kubectl get pods -w

# Auto-scale based on CPU (optional)
kubectl autoscale deployment cloudship-deployment --min=2 --max=10 --cpu-percent=80
```

### Updating the Application

When you push a new Docker image:

```bash
# Update the image in deployment
kubectl set image deployment/cloudship-deployment \
  cloudship=cloudship:v2.0

# Watch the rolling update
kubectl rollout status deployment/cloudship-deployment

# Rollback if needed
kubectl rollout undo deployment/cloudship-deployment
```

---

## 🔄 CI/CD Pipeline with GitHub Actions

Automate your build, test, and deployment process!

### Pipeline Flow

```
git push → Docker build → Run tests → Push to registry → Deploy to K8s
```

### Setting Up CI/CD

#### 1. Add Docker Hub Credentials

Go to your GitHub repository:
1. Settings → Secrets and variables → Actions
2. Create secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub personal access token

#### 2. Configure Kubernetes Access (for cloud clusters)

For remote Kubernetes clusters (EKS, GKE, AKS):
```bash
# Get your kubeconfig and add as a secret
kubectl config view --raw

# Add as KUBE_CONFIG secret in GitHub
```

#### 3. Trigger the Pipeline

Simply push to the `main` branch:
```bash
git add .
git commit -m "Update app"
git push origin main
```

The workflow automatically:
1. ✅ Builds Docker image
2. ✅ Runs tests (when configured)
3. ✅ Pushes to Docker Hub
4. ✅ Deploys to Kubernetes (if configured)

**Monitor your pipeline:**
- Go to Actions tab in GitHub
- Click on the latest workflow run
- View detailed logs for each step

---

## 📁 Project Structure

```
CloudShip-End-to-End-Kubernetes-CI-CD-Platform/
│
├── app/                          # Python Flask application
│   ├── app.py                    # Main application code
│   └── requirements.txt          # Python dependencies
│
├── k8s/                          # Kubernetes manifests
│   ├── deployment.yaml           # Pod deployment config
│   ├── service.yaml              # Internal service
│   ├── ingress.yaml              # External access
│   ├── configmap.yaml            # Configuration data
│   └── secret.yaml               # Sensitive data
│
├── .github/
│   └── workflows/
│       └── ci-cd.yaml            # GitHub Actions automation
│
├── Dockerfile                     # Container build instructions
├── README.md                      # This file
└── images/                        # Documentation images
```

---

## 🔧 Configuration

### Environment Variables

Control app behavior with environment variables:

```bash
# In your deployment.yaml or locally
export PORT=5000         # Server port
export HOST=0.0.0.0      # Server host (0.0.0.0 = listen on all interfaces)
export ENV=production    # Environment (development/production)
```

**In Kubernetes:**
```yaml
# deployment.yaml
env:
  - name: PORT
    value: "5000"
  - name: ENV
    value: "production"
```

### Customizing Kubernetes Manifests

Adapt the manifests for your setup:

**Change the image:**
```yaml
# In deployment.yaml
image: your-docker-hub/cloudship:latest
```

**Update the domain:**
```yaml
# In ingress.yaml
host: your-domain.com
```

**Adjust resources:**
```yaml
# In deployment.yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

---

## 🧪 Testing

Write and run tests for your application:

```bash
# Install test dependencies (if not in requirements.txt)
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_app.py
```

**In CI/CD pipeline**: Tests run automatically before deployment!

---

## 📊 Monitoring & Debugging

### View Logs

```bash
# See logs from a specific pod
kubectl logs <pod-name>

# Follow logs in real-time
kubectl logs -f <pod-name>

# See all logs from deployment
kubectl logs -l app=cloudship
```

### Debugging Issues

```bash
# Get detailed pod info
kubectl describe pod <pod-name>

# Execute commands inside a pod
kubectl exec -it <pod-name> -- /bin/bash

# Check pod events
kubectl get events --sort-by='.lastTimestamp'

# Port forward for local testing
kubectl port-forward pod/<pod-name> 5000:5000
```

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Fork & Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### Make Your Changes

```bash
# Make your awesome changes
# Add tests for new features
pytest

# Ensure Docker builds
docker build -t cloudship:test .
```

### Commit & Push

```bash
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
```

### Create a Pull Request

Open a pull request on GitHub with:
- Clear description of changes
- Reference to related issues
- Evidence of testing (test output, screenshots)

### Development Guidelines

- ✅ Follow [PEP 8](https://pep8.org/) for Python code
- ✅ Write tests for new features
- ✅ Update documentation
- ✅ Ensure `docker build` succeeds
- ✅ Update README if adding new features

---

## 📚 Learning Resources

Deepen your DevOps knowledge:

- **Kubernetes**: [Official K8s Tutorial](https://kubernetes.io/docs/tutorials/)
- **Docker**: [Docker Getting Started](https://docs.docker.com/get-started/)
- **CI/CD**: [GitHub Actions Docs](https://docs.github.com/en/actions)
- **Flask**: [Flask Official Guide](https://flask.palletsprojects.com/)
- **DevOps**: [The DevOps Handbook](https://itrevolution.com/the-devops-handbook/)

---

## 🆘 Troubleshooting

### Pod won't start

```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

Check for:
- ❌ Image pull errors → verify Docker image exists
- ❌ Port conflicts → change port in service.yaml
- ❌ Resource limits → check node resources

### Ingress not working

```bash
# Check ingress status
kubectl get ingress
kubectl describe ingress cloudship-ingress

# Verify service is running
kubectl get svc cloudship-service
```

### Docker build fails

```bash
# Build with verbose output
docker build -t cloudship:latest . --progress=plain

# Check Dockerfile syntax
docker run --rm -i hadolint/hadolint < Dockerfile
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙋 Support & Community

Need help? Here are your options:

1. **Open an Issue**: [GitHub Issues](https://github.com/your-username/CloudShip-End-to-End-Kubernetes-CI-CD-Platform/issues)
2. **Documentation**: Check [Kubernetes Docs](https://kubernetes.io/docs/), [Docker Docs](https://docs.docker.com/)
3. **Community**: Ask on [Stack Overflow](https://stackoverflow.com/) (tag: kubernetes, docker, github-actions)

---

## 🎯 Roadmap

Future enhancements coming soon:

- [ ] 📊 Comprehensive test suite with 80%+ coverage
- [ ] 🏥 Liveness and readiness health checks
- [ ] 📈 Prometheus monitoring and Grafana dashboards
- [ ] 🗄️ Database integration example (PostgreSQL)
- [ ] 🌍 Multi-environment deployment (dev/staging/prod)
- [ ] 🎁 Helm chart for easier K8s deployment
- [ ] 🔐 HTTPS/TLS with cert-manager
- [ ] 🧹 ArgoCD for GitOps workflow

---

## 🎉 Get Started Now!

Everything is ready to go. Just follow the **Getting Started** section above!

```bash
# The quick version:
git clone <this-repo>
cd CloudShip-End-to-End-Kubernetes-CI-CD-Platform
kubectl apply -f k8s/
kubectl port-forward svc/cloudship-service 5000:80
# Open http://localhost:5000 in your browser
```

---

**Happy shipping with CloudShip! 🚢**

*Made with ❤️ for the DevOps community*
