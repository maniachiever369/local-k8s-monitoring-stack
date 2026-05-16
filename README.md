# Local Kubernetes Microservice Architecture & Monitoring Stack

A production-grade, highly resilient microservice cluster infrastructure deployed locally using **Infrastructure as Code (IaC)** principles. 

## 🏗️ Architectural Layout
- **Orchestration Platform:** Kubernetes managed locally via **Kind** (Kubernetes-in-Docker)
- **Application Layer:** 3x Replicas of an **Nginx Web Server** with hard-coded `Burstable` QoS resource limits (RAM/CPU throttles).
- **Telemetry Engine:** **Kubernetes Metrics Server** and a **Prometheus** time-series database cluster.
- **Observability Layer:** **Grafana Analytics Engine** pre-baked with direct data pipelines rendering live cluster performance metrics.

## 🚀 Instant Deployment Guide

### 1. Spin up the cluster & application
```bash
kind create cluster
kubectl apply -f master-config.yml
```

### 2. Launch the Monitoring Infrastructure
```bash
# Deploy metrics collection
kubectl apply -f metrics-server.yaml

# Deploy Prometheus database & Grafana visual console via Helm
helm install my-prometheus oci://registry-1.docker.io/bitnamicharts/prometheus --namespace monitoring --create-namespace
helm install my-grafana grafana/grafana --namespace monitoring -f grafana-values.yaml
```

### 3. Open the Dashboards
Extract the Grafana credentials and port-forward to access the live panels on port `3000` (Password: `admin123`):
```bash
kubectl port-forward --namespace monitoring service/my-grafana 3000:80
```
Import **Dashboard ID: 315** to populate real-time graphical metrics!
