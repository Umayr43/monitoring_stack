# Containerized Monitoring Stack

A production-style observability stack built with Docker Compose, demonstrating 
multi-container orchestration, metrics collection, visualization, and alerting.

## Stack

| Component | Purpose |
|-----------|---------|
| Python/Flask app | Exposes custom application metrics via /metrics |
| Prometheus | Scrapes and stores time-series metrics |
| Grafana | Visualizes metrics via dashboards |
| Alertmanager | Routes alerts to Slack when thresholds are breached |
| Node Exporter | Exposes host system metrics (CPU, memory, disk) |

## Architecture

Flask App (/metrics) ──┐
Node Exporter ──────────┼──► Prometheus ──► Grafana (dashboards)
                        │         │
                        └─────────┴──► Alertmanager ──► Slack

## Running locally

docker compose up -d --build

Services:
- Flask app:    http://localhost:5000
- Prometheus:   http://localhost:9090
- Grafana:      http://localhost:3000  (admin/admin)
- Alertmanager: http://localhost:9093

## Key concepts demonstrated

- Multi-stage Dockerfile for minimal, secure images
- Docker named volumes for persistent data
- Custom bridge network for inter-container DNS resolution
- Grafana datasource and dashboard provisioning via config files
- PromQL queries for CPU, memory, and custom application metrics
- Alert rules with severity labels and Slack webhook delivery