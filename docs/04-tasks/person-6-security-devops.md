# 👤 Person 6 — Đinh Tiến Luân (Cyber Security & DevOps Engineer)

> **Người phụ trách**: **Đinh Tiến Luân**
> **Sở hữu**: Hạ tầng CI/CD GitHub Actions, Docker Compose, bảo mật FastAPI, Pydantic Input/Output Validation Audit, Rate Limiting & Pentest OWASP Top 10 xuyên suốt toàn dự án.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 3 Tasks | 0/3 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | 0/2 | 🔲 To Do |
| **Sprint 2** | 0 Tasks (Support Review API Security) | 0/0 | 🔲 To Do |
| **Sprint 3** | 0 Tasks (Support Review Export/Mail) | 0/0 | 🔲 To Do |
| **Sprint 4** | 4 Tasks | 0/4 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — Infrastructure & CI/CD Setup
- [ ] **`TASK-006`** **Docker Compose & Environment Setup**
  - **Feature**: N/A
  - **Target Files**: `docker-compose.yml`, `backend/Dockerfile`, `.env.example`
  - **Acceptance Criteria**: `docker compose up -d` starts PostgreSQL 15, Redis 7, FastAPI server without errors.
- [ ] **`TASK-007`** **GitHub Actions Pipeline Setup**
  - **Feature**: N/A
  - **Target Files**: `.github/workflows/ci.yml`
  - **Acceptance Criteria**: Automated runs on PR: `ruff check backend`, `mypy backend`, `pytest backend`, `npm run lint frontend`, `npm run build frontend`.
- [ ] **`TASK-008`** **Pre-commit Hooks & Linter Setup**
  - **Feature**: N/A
  - **Target Files**: `.pre-commit-config.yaml`, `backend/pyproject.toml`
  - **Acceptance Criteria**: Blocks local git commit if Ruff linting fails or Black formatting drifts.

### Sprint 1 — Security Middlewares & Auth Review
- [ ] **`TASK-116`** **FastAPI Security Middlewares**
  - **Feature**: Security Baseline
  - **Target Files**: `backend/app/main.py`
  - **Acceptance Criteria**: Configures `CORSMiddleware` (restricted origins), `TrustedHostMiddleware`, security headers via middleware.
- [ ] **`TASK-117`** **Auth Module Security Review**
  - **Feature**: Security
  - **Target Files**: `backend/app/api/v1/auth.py`
  - **Acceptance Criteria**: Sign-off on bcrypt cost factor ≥ 10, JWT secret length ≥ 32 chars, httpOnly cookie settings, rate limit configuration.

### Sprint 4 — Pentest, Pydantic Audits & Production Deploy
- [ ] **`TASK-411`** **Input Sanitization & Boundary Validation Audit**
  - **Feature**: Security
  - **Target Files**: `backend/app/ai_agents/`, `backend/app/schemas/`
  - **Acceptance Criteria**: Verifies all user inputs are sanitized (Pydantic & bleach); checks system/user/assistant message roles framing without raw string concatenation.
- [ ] **`TASK-412`** **Pydantic Output Validation Audit**
  - **Feature**: Security
  - **Target Files**: `backend/app/ai_agents/llm_provider.py`
  - **Acceptance Criteria**: Ensures unparseable or malicious LLM outputs trigger graceful fallback without server crash or raw output leakage.
- [ ] **`TASK-413`** **OWASP Top 10 Security Pentest**
  - **Feature**: Security
  - **Target Files**: Entire Application
  - **Acceptance Criteria**: Verifies SQL injection safety (SQLAlchemy parameterized queries), XSS escaping, CORS enforcement, and authorization guards across all endpoints.
- [ ] **`TASK-414`** **Production Build & Deployment Validation**
  - **Feature**: DevOps
  - **Target Files**: `docker-compose.prod.yml`, GitHub Actions
  - **Acceptance Criteria**: Production Docker container builds cleanly; staging deployment verified with SSL, environment secrets, and green health checks.

---

## 🤝 Handover & Review Guidelines (Person 6)

1. **Buddy / Backup**: Any available team member
2. **Task Completion**: Verify CI run pass green on GitHub Actions. Push branch `feature/TASK-xxx` and review all PRs within 24h.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
