# Local Kubernetes Microservice Architecture & Monitoring Stack

A production-grade, highly resilient microservice cluster infrastructure deployed locally using **Infrastructure as Code (IaC)** principles. This repository serves as a repeatable blueprint for launching an application with real-time hardware telemetry and automated visualization dashboards.

## 🏗️ Architectural Layout
- **Orchestration Platform:** Kubernetes managed locally via **Kind** (Kubernetes-in-Docker).
- **Application Layer:** 3x Replicas of an **Nginx Web Server** with explicit `Burstable` QoS resource limits (RAM/CPU throttles) to prevent system crashes.
- **Telemetry Engine:** **Kubernetes Metrics Server** and a **Prometheus** time-series database.
- **Observability Layer:** **Grafana Analytics Engine** pre-baked with direct data pipelines rendering live cluster performance metrics.

---

## 🚀 Step-by-Step Deployment Guide (For Future Use)

### 1. Recreate the Cluster & App
When you want to run this project again, open this folder in your terminal and run:
```bash
# Spin up the local cluster
kind create cluster

# Launch your 3 Nginx web servers and load balancer service instantly
kubectl apply -f master-config.yml
```

### 2. Deploy the Metrics Collection Engine
```bash
# Install the core metrics server components
kubectl apply -f https://github.com

# Patch the server for Kind compatibility (Bypasses local TLS check)
kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
```
*Verify it works by waiting 60 seconds and running: `kubectl top pods`*

### 3. Deploy the Monitoring Stack (Prometheus & Grafana)
Using **Helm**, deploy the data collector and display board using your saved configuration profile:
```bash
# Install Prometheus into the monitoring namespace
helm install my-prometheus oci://registry-1.docker.io/bitnamicharts/prometheus --namespace monitoring --create-namespace

# Install Grafana using your pre-configured values file (Sets password to admin123)
helm install my-grafana grafana/grafana --namespace monitoring -f grafana-values.yaml
```

### 4. Access the Live Dashboards
Bridge the internal cluster network to your local Mac browser:
```bash
kubectl port-forward --namespace monitoring service/my-grafana 3000:80
```
1. Open your browser and head to **`http://localhost:3000`**.
2. Log in with Username: **`admin`** and Password: **`admin123`**.
3. Navigate to **Dashboards** -> **Import**.
4. Type in Community Dashboard ID **`315`** and hit **Load**.
5. Select **Prometheus** from the dropdown box and click **Import**!

---

## 🧼 Cleaning Up Your Mac
When you are done testing and want to save your Mac's RAM and battery power, run this single command to completely wipe out the cluster cleanly:
```bash
kind delete cluster
```
