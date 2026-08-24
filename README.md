<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&size=32&duration=3000&pause=1000&color=2563EB&center=true&vCenter=true&width=600&lines=PataFundi;Pata+Fundi+Sahihi%2C+Kwa+Wakati+Sahihi;Find+the+Right+Technician%2C+at+the+Right+Time." alt="Typing SVG" />

<br/>

**Tanzanian technician & services marketplace** — website-first · API-first · free-first · certificate-optional · bilingual (Kiswahili / English) · multi-theme

<br/>

![Version](https://img.shields.io/badge/version-2.0-2563EB?style=for-the-badge)
![License](https://img.shields.io/badge/license-Proprietary-lightgrey?style=for-the-badge)
![Branch](https://img.shields.io/badge/default_branch-develop-orange?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)

<br/>

### 🛠️ Built With

<img src="https://skillicons.dev/icons?i=react,ts,vite,tailwind,fastapi,py,postgres,redis,docker,git&theme=dark" alt="tech stack icons" />

<br/><br/>

![React](https://img.shields.io/badge/React_18-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=flat-square&logo=jsonwebtokens&logoColor=white)

</div>

<br/>

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Features](#-features)
3. [Tech Stack](#-tech-stack)
4. [System Architecture](#-system-architecture)
5. [Repository Structure](#-repository-structure)
6. [Prerequisites](#-prerequisites)
7. [Clone the Project](#-clone-the-project)
8. [Branching Workflow](#-branching-workflow)
9. [Local Setup](#-local-setup)
10. [Environment Variables](#-environment-variables)
11. [Seed Accounts](#-seed-accounts)
12. [Key Routes & API](#-key-routes--api)
13. [UI / UX Notes](#-ui--ux-notes)
14. [Development Guidelines](#-development-guidelines)
15. [Roadmap](#-roadmap)
16. [License](#-license)

<br/>

## 🌍 Overview

**PataFundi** connects customers with trusted local technicians (*fundis*) across Tanzania and provides a spares marketplace for parts (phone screens, batteries, AC components, tools, and more).

| Role | What they do |
|---|---|
| 🙋 **Customers** | Search by service and distance, book jobs, track status, leave reviews |
| 🔧 **Technicians** | Register (certificates optional), manage availability, complete jobs |
| 🛒 **Merchants** | List and sell spare parts |
| 🛡️ **Admins** | Manage users, categories, and platform health |

The product is **mobile-first**, with a polished responsive UI, five visual themes, light/dark appearance, and full Kiswahili / English support.

<br/>

## ✨ Features

<table>
<tr><td width="24%"><b>🔐 Auth & Roles</b></td><td>JWT auth, RBAC (customer, technician, merchant, admin)</td></tr>
<tr><td><b>🔎 Find a Fundi</b></td><td>Category search, distance radius, ratings, availability</td></tr>
<tr><td><b>📋 Jobs / Bookings</b></td><td>Full lifecycle, status history, reviews</td></tr>
<tr><td><b>🛍️ Marketplace</b></td><td>List, browse, and order spare parts</td></tr>
<tr><td><b>📤 Uploads</b></td><td>Images, video, and documents on jobs, listings, profiles</td></tr>
<tr><td><b>⚡ Realtime</b></td><td>WebSocket channel skeleton (<code>/ws</code>)</td></tr>
<tr><td><b>🌐 i18n</b></td><td>Kiswahili (default) + English</td></tr>
<tr><td><b>🎨 Themes</b></td><td>Classic · Ocean · Forest · Sunset · Midnight + light/dark/system</td></tr>
</table>

<br/>

## 🧰 Tech Stack

<details open>
<summary><b>Frontend</b></summary>
<br/>

- React 18 + TypeScript
- Vite
- Tailwind CSS (design tokens via CSS variables)
- React Router v6
- TanStack Query (server state)
- Axios
- Lucide React (icons)
- Plus Jakarta Sans

</details>

<details open>
<summary><b>Backend</b></summary>
<br/>

- FastAPI
- SQLAlchemy 2 + Alembic
- PostgreSQL (Docker / production) or **SQLite** (local example DB)
- Redis (optional locally; used at scale / future token blacklist & pub-sub)
- JWT (`python-jose`), Passlib / bcrypt
- Geo-ready fields (lat/lng, radius); PostGIS image in Compose

</details>

<details open>
<summary><b>Infrastructure</b></summary>
<br/>

- Docker Compose: `postgres` (PostGIS), `redis`, `backend`, `frontend`
- Local uploads volume

</details>

<br/>

## 🏗️ System Architecture

```
┌─────────────────┐     HTTPS / JSON      ┌──────────────────┐
│  React + Vite   │ ◄──────────────────► │  FastAPI (API)   │
│  (port 5173)    │   /api/v1/* · /ws    │  (port 8000)     │
└─────────────────┘                       └────────┬─────────┘
                                                    │
                                    ┌───────────────┼───────────────┐
                                    ▼                ▼               ▼
                              PostgreSQL          Redis           Uploads
                              (or SQLite)      (optional)         (files)
```

- **Frontend** talks only to the public API (`VITE_API_URL`).
- **Backend** owns auth, domain logic, persistence, and file storage.
- **Compose** wires services; local-without-Docker uses SQLite + optional Redis.

<br/>

## 📁 Repository Structure

Backend and frontend live in **one monorepo**:

```text
patafundi/
├── README.md                 # This file
├── .gitignore
├── docker-compose.yml        # Postgres, Redis, backend, frontend
├── docs/
│   └── ARCHITECTURE.md
├── infrastructure/           # Extra deploy notes / scripts
│
├── backend/                  # FastAPI application
│   ├── .env.example
│   ├── .env                  # Local secrets (do not commit real secrets)
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic/              # Migrations
│   ├── tests/
│   └── app/
│       ├── main.py           # App entry, lifespan, seed_data()
│       ├── core/
│       │   ├── config.py     # Settings (pydantic-settings)
│       │   ├── database.py   # Engine, SessionLocal, Base
│       │   ├── dependencies.py
│       │   └── security.py   # JWT, password hashing
│       ├── models/           # SQLAlchemy models
│       │   ├── user.py       # User, TechnicianProfile, ServiceCategory
│       │   ├── job.py
│       │   ├── spare.py
│       │   ├── media.py
│       │   └── enums.py
│       ├── schemas/          # Pydantic request/response models
│       ├── routers/          # HTTP + WebSocket routes
│       │   ├── auth.py
│       │   ├── users.py
│       │   ├── technicians.py
│       │   ├── categories.py
│       │   ├── jobs.py
│       │   ├── spares.py
│       │   ├── uploads.py
│       │   ├── admin.py
│       │   └── ws.py
│       ├── services/         # Business logic
│       ├── repositories/     # Data access layer
│       ├── utils/
│       ├── middleware/
│       ├── integrations/
│       └── workers/          # Background / Celery hooks
│
└── frontend/                 # React + Vite SPA
    ├── Dockerfile
    ├── package.json
    ├── vite.config.ts
    ├── tailwind.config.js
    ├── postcss.config.js
    ├── tsconfig.json
    ├── index.html
    ├── public/
    └── src/
        ├── main.tsx
        ├── App.tsx           # Route definitions
        ├── index.css         # Shared component classes (btn, card, input…)
        ├── themes/
        │   └── themes.css    # Classic, Ocean, Forest, Sunset, Midnight
        ├── layouts/
        │   └── MainLayout.tsx
        ├── pages/
        │   ├── HomePage.tsx
        │   ├── FindFundiPage.tsx
        │   ├── TechnicianDetailPage.tsx
        │   ├── JobsPage.tsx
        │   ├── NewJobPage.tsx
        │   ├── JobDetailPage.tsx
        │   ├── MarketplacePage.tsx
        │   ├── SellSparePage.tsx
        │   ├── SpareDetailPage.tsx
        │   ├── DashboardPage.tsx
        │   ├── SettingsPage.tsx
        │   ├── LoginPage.tsx
        │   ├── RegisterPage.tsx
        │   └── NotFoundPage.tsx
        ├── providers/
        │   ├── AuthProvider.tsx
        │   ├── LanguageProvider.tsx
        │   └── ThemeProvider.tsx
        ├── services/
        │   └── api.ts        # Axios client + API helpers
        ├── translations/
        │   ├── en.json
        │   └── sw.json
        ├── components/
        ├── hooks/
        ├── context/
        ├── types/
        ├── utils/
        └── assets/
```

<br/>

## ✅ Prerequisites

| Tool | Notes |
|------|--------|
| **Git** | Clone and branching |
| **Node.js 18+** | Frontend (`npm`) |
| **Python 3.11+** | Backend |
| **Docker Desktop** *(optional)* | Full stack with Postgres + Redis |
| **PostgreSQL 16** *(optional)* | Only if not using SQLite or Docker |

<br/>

## ⬇️ Clone the Project

Replace the URL with your real remote (GitHub / GitLab / Bitbucket).

```bash
# HTTPS
git clone https://github.com/<org-or-user>/patafundi.git
cd patafundi

# SSH
git clone git@github.com:<org-or-user>/patafundi.git
cd patafundi
```

Always start from an up-to-date **`develop`** branch (not `main`):

```bash
git fetch origin
git checkout develop
git pull origin develop
```

If `develop` does not exist on the remote yet, create and publish it once:

```bash
git checkout -b develop
git push -u origin develop
```

<br/>

## 🌿 Branching Workflow

> **Policy:** all day-to-day work is pushed to `develop`. Do **not** push feature commits directly to `main`.

| Branch | Purpose |
|--------|---------|
| `main` | Stable / production-ready only (protected; merge via PR from `develop` or release tags) |
| `develop` | Integration branch — **default target for PRs and team pushes** |
| `feature/<name>` | New features (branch from `develop`) |
| `fix/<name>` | Bug fixes |
| `chore/<name>` | Tooling, docs, dependency updates |

### Create a feature branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/find-fundi-map
```

### Commit and push (feature branch → PR into `develop`)

```bash
git add .
git status
git commit -m "feat(frontend): add distance filter on Find Fundi"
git push -u origin feature/find-fundi-map
```

Open a **Pull Request** with **base branch = `develop`** (not `main`).

### After review — merge into `develop`

```bash
git checkout develop
git pull origin develop
git merge feature/find-fundi-map
git push origin develop
```

Or merge through the hosting provider's PR UI targeting **`develop`**.

### Release to `main` (maintainers only)

```bash
git checkout main
git pull origin main
git merge develop
git push origin main
git tag -a v2.0.1 -m "Release 2.0.1"
git push origin v2.0.1
```

### Quick rules

1. **Never** `git push origin main` for normal feature work.
2. Base every branch on the latest `develop`.
3. Prefer small, focused PRs into `develop`.
4. Use clear commit messages (e.g. Conventional Commits: `feat:`, `fix:`, `docs:`).

<br/>

## 💻 Local Setup

<details>
<summary><b>Option A — SQLite example database (no Docker)</b></summary>
<br/>

On first start the backend creates `backend/patafundi_example.db` and seeds demo data.

```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Ensure .env uses SQLite (see Environment variables)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

```bash
# Frontend (second terminal)
cd frontend
npm install
npm run dev
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| API docs | http://localhost:8000/api/docs |
| Health | http://localhost:8000/health |

</details>

<details>
<summary><b>Option B — Docker Compose (Postgres + Redis + full stack)</b></summary>
<br/>

```bash
cd patafundi
docker compose up --build
```

Same URLs as above. Compose sets `DATABASE_URL` to Postgres on the internal network.

</details>

<details>
<summary><b>Option C — Docker only for databases</b></summary>
<br/>

```bash
docker compose up -d postgres redis
# then run backend/frontend locally with a Postgres URL in .env
```

</details>

<br/>

## 🔑 Environment Variables

```bash
cd backend
cp .env.example .env
```

| Variable | Local example | Notes |
|----------|---------------|--------|
| `DATABASE_URL` | `sqlite:///./patafundi_example.db` | Use Postgres URL for Docker/production |
| `SECRET_KEY` | long random string | Required for JWT |
| `BACKEND_CORS_ORIGINS` | `["http://localhost:5173"]` | JSON list |
| `REDIS_URL` | `redis://localhost:6379/0` | Optional locally |
| `UPLOAD_DIR` | `./uploads` | File storage path |
| `PAYMENT_MODE` | `development` | Fake payments in dev |
| `VITE_API_URL` | `http://localhost:8000/api/v1` | Frontend env / Compose |

<br/>

## 👤 Seed Accounts

Created automatically when the database is empty:

| Role | Email | Password |
|------|--------|----------|
| Super Admin | admin@patafundi.co.tz | Admin@123 |
| Customer | customer@example.com | Customer1! |
| Technician | fundi@example.com | Fundi123! |
| Merchant | merchant@example.com | Merchant1! |

Also seeded: service categories, sample technician profile, and related demo data via `seed_data()` in `app/main.py`.

<br/>

## 🔗 Key Routes & API

### Frontend routes

| Path | Purpose |
|------|---------|
| `/` | Home — hero, services, how it works, featured fundis |
| `/find-fundi` | Search technicians |
| `/technicians/:id` | Technician profile |
| `/jobs` · `/jobs/new` · `/jobs/:id` | Bookings & status |
| `/marketplace` · `/marketplace/sell` · `/marketplace/:id` | Spares |
| `/dashboard` | Role-aware quick actions |
| `/settings` | Language, theme, account |
| `/login` · `/register` | Auth |

### API highlights (prefix `/api/v1`)

```http
POST   /auth/login
POST   /auth/register
GET    /technicians/search?lat=&lng=&radius_km=
GET    /categories
POST   /jobs/
PATCH  /jobs/{id}/status
POST   /jobs/{id}/review
GET    /spares/parts
POST   /spares/parts
POST   /spares/orders
POST   /uploads/
WS     /ws?token=<access_token>
```

Interactive docs: http://localhost:8000/api/docs

<br/>

## 🎨 UI / UX Notes

The interface is **mobile-first** and consistent across pages:

- **Design tokens** — brand blues, savannah gold accent, surface / text / border variables per theme
- **Components** — `.btn-primary`, `.btn-secondary`, `.btn-ghost`, `.card`, `.input`, badges, glass sticky header
- **Typography** — Plus Jakarta Sans; titles scale by breakpoint
- **Themes** — Classic (default), Ocean, Forest, Sunset, Midnight + light / dark / system
- **Language** — Kiswahili default; toggle to English in the header
- **Accessibility** — focus-visible rings, ≥44px touch targets, reduced-motion support

When adding UI, follow patterns in `index.css`, `themes/themes.css`, and `layouts/MainLayout.tsx`.

<br/>

## 📐 Development Guidelines

1. **Branch from `develop`**, open PRs **into `develop`**, never force-push `main`.
2. Keep backend schemas and frontend `api.ts` types aligned.
3. Prefer small commits with clear messages.
4. Do not commit secrets, `venv/`, `node_modules/`, or `*.db` files.
5. Use API `--reload` and Vite HMR during development.
6. After model changes, add Alembic migrations for Postgres; local SQLite can be deleted and re-seeded if needed.
7. Add bilingual keys in both `en.json` and `sw.json` for new user-facing copy.

<br/>

## 🗺️ Roadmap

| Version | Focus |
|---------|--------|
| **V1** | Foundation, auth, RBAC, themes, language, responsive UI, optional certificates |
| **V2 (current)** | Distance search, job lifecycle, dashboards, spares marketplace, uploads, WebSocket skeleton |
| **V3** | Trust system, chat, notifications, payments / escrow, advanced admin, mobile app |

<br/>

## 📄 License

Proprietary / project-specific — replace this section with your organisation's license before a public release.

<br/>

<div align="center">

Built with ❤️ for Tanzania.

**PataFundi-TZ** — *Find the Right Technician, at the Right Time.*

<br/>

> ⚠️ **Reminder:** Clone → checkout **`develop`** → create `feature/...` → push and open a PR against **`develop`**. Do **not** push routine work to `main`.

</div>
