# DEPLOYMENT_SPEC.md

# Real Estate Lead Bot — VPS Deployment Specification

## 1. Purpose

This document defines how the Real Estate Lead Bot should be deployed to a VPS.

The deployment should be simple, affordable, easy to maintain, and suitable for an MVP.

---

## 2. Target Environment

```text
ONE VPS
│
├── Nginx
├── React (static build)
├── FastAPI
├── PostgreSQL
└── n8n
```

Stack:
- Ubuntu LTS
- Docker + Docker Compose
- Nginx reverse proxy
- HTTPS (Let’s Encrypt)
- Persistent volumes for PostgreSQL and n8n

---

## 3. High-Level Steps

1. Provision VPS (Ubuntu LTS)
2. Create deploy user + SSH keys
3. Install Docker & Docker Compose
4. Configure firewall
5. Clone repository
6. Create production `.env`
7. Build frontend
8. Start services with Docker Compose
9. Run database migrations
10. Configure Nginx + domain + HTTPS
11. Verify health, chat flow, and notifications
12. Configure backups

---

## 4. Services & Ports (internal)

- FastAPI: 8000
- React (or static via Nginx)
- PostgreSQL: 5432 (not exposed publicly)
- n8n: 5678 (protected)

Public traffic goes through Nginx (80/443).

---

## 5. Environment

Production uses a private `.env` (never committed) based on `.env.example`.

Critical variables:
- `DATABASE_URL`
- `JWT_SECRET` / `SECRET_KEY`
- `N8N_WEBHOOK_SECRET`
- `AI_API_KEY`
- `CORS_ORIGINS`

---

## 6. Docker Compose (production)

A `docker-compose.prod.yml` (or equivalent) should run:
- postgres
- backend
- n8n
- (optional) frontend container or pure static files served by Nginx

Volumes:
- PostgreSQL data
- n8n data

---

## 7. Nginx

- Frontend at domain root
- API under `/api` or `api.` subdomain
- n8n under a protected path or subdomain
- SSL via Certbot / Let’s Encrypt

---

## 8. Backups & Operations

- Daily PostgreSQL dumps
- n8n workflow export / volume backup
- Log rotation
- Ability to restart services after VPS reboot

---

## 9. Validation Checklist

- [ ] Frontend accessible over HTTPS
- [ ] API health endpoint OK
- [ ] Database connected
- [ ] n8n reachable (authenticated)
- [ ] Customer message flow works end-to-end
- [ ] HOT lead notification works
- [ ] Backups configured
- [ ] VPS reboot recovery tested

---

## 10. Principle

Start with a single well-configured VPS. Do not introduce Kubernetes or multi-service clusters until the MVP workload requires it.

Full original detail is preserved in git history of the previous root `DEPLOYMENT_SPEC.md`.
