## Project 4 - Production Kubernetes Deployment on AWS EKS Fargate


## Overview
This repo contains a production-ready deployment of a containerized python web application running on Kubernetes using AWS EKS Fargate.
The project Demonstrates end-to-end DevOps practices including containerization, CI/CD automation, rolling deployments, healt monitoring, and cloud observability.
The primary goal was to simulate a real-world cloud deployment workflow used in modern DevOps environments.

## Objectives
- Deploy a containerized application to a managed Kubernetes environment
- Implement automated CI/CD for build and deployment 
- Ensure zero-downtime deployments using rolling updates.
- Implment health monitoring and readiness validation
- Apply production resources management practices 
- Integrate centralized logging and monitoring 

## Architecture Summary 
- Containerized python web service 
- kubernetes Deployment with multiple replicas 
- LoadBalancer Service for external traffic
- CI/CD pipeline triggering automated updates
- Managed Kubernetes infrastructure (EKS Fargate)
- CloudWatch-based observability

## Technology Stack 
- Python / FastAPI
- Docker 
- Kubernetes
- AWS EKS (Fargate)
- Github ACtions
- AWS CloudWatch

## Core Implemention
### Containerization
- Application packaged into a Docker Image
- Exposed via internal container port 
- Designed for immutable deployments 

### Kubernetes Deployment
- Multi-replica Deployment for availability
- Rolling updates strategy for zero downtime
- Label-based service discovery
- Production resource request and limits

### Health Monitoring 
- Liveness probe for container recovery
- Rediness probe for traffic control
- Startup probe for initialization checks 
- /health endpoint for operational checks 

### Service Exposure
- Kubernetes Loadbalancer Service 
- External IP based public access 
- Traffic routed to healthy pods only 

### CI/CD Pipeline
Automated workflow triggered on repository updates:
1. Source code push
2. Docker image build 
3. Image push to container registry
4. Kubernetes deployment updated
5. Rolling pod replacement executed

### Observability
- Cluster monitoring via CloudWatch
- Application logs aggregation
- Deployment and runtime troubleshooting

## Deployment WorkFlow 
```
Developer push -> CI/CD Pipeline -> Image Build -> Registry Push -> Kubernetes Deployment Update -> Rolling Pod Replacement -> Application available via LoadBalancer 
```

## Repository Structure 

Dockerfile
    |
main.py
    |
deployment-prod.yaml
    | 
.gitthub/workfulows/
o     cilcd.yaml

## Operoationarl Pr acteicems Impilemented 
- Immutable deployments
- Zero downtime rollout 
- Health-based traffic rouing 
- Resource management for stability
- Automated infrastructure interaction
- Production yaml consolidation

## Running the Deployment 
Apply production configuration

```bash

kubectl apply -f deployment-prod.yaml
```
Verify resources 
```kubectl get pods 
   kubectl get svc
```
Access application through LoadBalancer External IP

## Key Learning Outcomes 
- Designing production kubernetes deployments
- Implementing CI/CD pipelines for containerized workloads 
- Managing deployments on managed kubernetes service 
- Applying health chekcs and rollout strategies 
- Troubleshooting distributed cloud applications 

## Author 
Uzair Munir 
DevOps / Cloud Engineering Enthusiast

## License 
Portfolio and educational use.

