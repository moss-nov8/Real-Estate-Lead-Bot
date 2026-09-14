# DEPLOYMENT_SPEC.md

# Real Estate Lead Bot — VPS Deployment Specification

## 1. Purpose

This document defines how the Real Estate Lead Bot should be deployed to a VPS.

The deployment should be:

- Simple.
- Affordable.
- Easy to maintain.
- Easy to troubleshoot.
- Suitable for an MVP and early production use.

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

---

## 3. Recommended Stack

- Ubuntu LTS
- Docker + Docker Compose
- Nginx (reverse proxy + HTTPS)
- PostgreSQL (container or managed)
- n8n (container)
- Let’s Encrypt / Certbot for HTTPS

---

## 4. High-Level Steps

1. Provision VPS
2. Create deploy user + SSH hardening
3. Install Docker + Docker Compose
4. Clone repository
5. Configure production `.env`
6. Build frontend
7. Run migrations
8. Start services with Docker Compose
9. Configure Nginx + domain + HTTPS
10. Validate end-to-end
11. Set up backups and monitoring

---

## 5. Environment Variables (Production)

Use a production `.env` (never committed) with:

- Strong `SECRET_KEY` / `JWT_SECRET`
- Production `DATABASE_URL`
- Correct `CORS_ORIGINS`
- Real `N8N_WEBHOOK_URL` / secrets
- Real AI provider keys
- Google Sheets credentials if used

---

## 6. Docker Compose (Production)

A production `docker-compose.prod.yml` (or override) should run:

- postgres (with volume)
- backend (FastAPI)
- n8n (with volume)
- (optional) frontend served by Nginx or a static container

---

## 7. Nginx

- Serve React build on the main domain
- Proxy `/api` to FastAPI
- Proxy n8n on a subdomain if needed
- Force HTTPS and set security headers

---

## 8. Backups

- PostgreSQL daily dumps
- n8n data volume
- Off-site retention

---

## 9. Validation Checklist

- Frontend accessible over HTTPS
- API health endpoint returns 200
- Database connected
- n8n reachable and webhooks work
- Customer message → AI → lead stored → response
- HOT lead notification works
- Restart survival test

---

## 10. Principle

Start with a single VPS. Scale only when the application needs it.

The full original DEPLOYMENT_SPEC content is available in git history if more detail is required.
