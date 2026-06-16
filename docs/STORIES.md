# STORIES.md

## Project: dev‑vps  
**Goal:** Deliver a fully‑managed VPS platform that lets developers spin up, configure, and scale virtual machines with minimal friction, while providing robust security, monitoring, and billing.

---

## Epic 1 – Onboarding & Self‑Service

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| **E1‑S1** | **As a developer, I want to create an account with a single click, so that I can start provisioning VPS instances immediately.** | • Sign‑up page accepts email or GitHub OAuth.<br>• Email verification is sent and validated.<br>• New user is automatically added to the default “dev‑team” group. |
| **E1‑S2** | **As a developer, I want to view a dashboard of my active VPS instances, so that I can see status and resource usage at a glance.** | • Dashboard lists instance ID, name, status, CPU, RAM, IP, and uptime.<br>• Each row links to detailed metrics page.<br>• Data refreshes every 30 s via WebSocket. |
| **E1‑S3** | **As a developer, I want to provision a new VPS with a pre‑configured image, so that I can start coding right away.** | • “Create Instance” button opens a wizard.<br>• User selects image, size, region, and optional SSH key.<br>• Instance is created within 2 min and appears on the dashboard. |
| **E1‑S4** | **As a developer, I want to delete an instance, so that I can free up resources when I’m done.** | • Delete button shows confirmation modal.<br>• Instance is terminated within 30 s.<br>• Billing stops immediately after deletion. |
| **E1‑S5** | **As a developer, I want to view usage logs, so that I can audit what happened on my VPS.** | • Logs page shows timestamp, event type, and actor.<br>• Ability to filter by date range and event type.<br>• Export logs as CSV. |

---

## Epic 2 – Configuration & Customization

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| **E2‑S1** | **As a developer, I want to attach an SSH key to my VPS, so that I can securely access it.** | • Key upload accepts public key file or paste.<br>• Key is validated for correct format.<br>• Key appears in instance details under “SSH Keys”. |
| **E2‑S2** | **As a developer, I want to install custom software via a script, so that my environment matches my workflow.** | • “Run Script” button opens a modal.<br>• User pastes or uploads a shell script.<br>• Script executes on the instance and logs output.<br>• Success/failure status shown on instance page. |
| **E2‑S3** | **As a developer, I want to set environment variables for my instance, so that my applications can read configuration.** | • Environment variables can be added/edited via UI.<br>• Variables are stored encrypted at rest.<br>• Variables are injected into the instance at boot time. |
| **E2‑S4** | **As a developer, I want to set a custom hostname, so that my instance is easily identifiable.** | • Hostname field accepts alphanumeric, dashes, dots.<br>• Validation ensures uniqueness within the region.<br>• Hostname is applied immediately via cloud provider API. |

---

## Epic 3 – Monitoring & Alerts

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| **E3‑S1** | **As a developer, I want to view real‑time CPU, memory, and disk usage, so that I can detect performance bottlenecks.** | • Grafana dashboard embedded in instance page.<br>• Metrics update every 5 s.<br>• Thresholds configurable per instance. |
| **E3‑S2** | **As a developer, I want to receive email alerts when my instance exceeds a CPU threshold, so that I can take action before downtime.** | • Alert rule UI allows threshold, duration, and notification channel.<br>• Email sent via SendGrid with clear subject and body.<br>• Alerts can be silenced for 15 min. |
| **E3‑S3** | **As a developer, I want to view historical uptime and downtime, so that I can report SLA compliance.** | • Uptime chart shows 30‑day trend.<br>• Exportable CSV of uptime periods.<br>• SLA calculation (99.9%) displayed. |

---

## Epic 4 – Billing & Cost Management

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| **E4‑S1** | **As a developer, I want to see a cost estimate before provisioning, so that I can budget my usage.** | • Estimate calculator shows hourly rate per instance type.<br>• Option to select duration (hourly, daily, monthly). |
| **E4‑S2** | **As a developer, I want to view a detailed monthly invoice, so that I can reconcile expenses.** | • Invoice page lists instances, hours, rates, and total.<br>• PDF download available.<br>• API endpoint `/api/invoices/{month}` returns JSON. |
| **E4‑S3** | **As a developer, I want to set a spending cap, so that I don’t exceed my budget.** | • Cap can be set per project or globally.<br>• When cap is reached, new instance creation is blocked.<br>• Email notification sent when 80 % of cap is used. |

---

## Epic 5 – Security & Compliance

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| **E5‑S1** | **As a developer, I want my VPS to be protected by a firewall with default deny, so that unauthorized traffic is blocked.** | • Firewall rules created automatically on instance creation.<br>• Only inbound SSH (port 22) and user‑defined ports allowed.<br>• Rules can be edited via UI. |
| **E5‑S2** | **As a developer, I want to enable two‑factor authentication for the portal, so that my account is more secure.** | • TOTP (Google Authenticator) integration.<br>• 2FA can be enabled/disabled in account settings.<br>• Enforced for all admin actions. |
| **E5‑S3** | **As a developer, I want my data to be encrypted at rest, so that I comply with GDPR.** | • All instance disks use cloud provider encryption.<br>• Encryption keys managed by AWS KMS or equivalent.<br>• Audit log records key access. |

---

## Epic 6 – Integration & Extensibility

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| **E6‑S1** | **As a developer, I want to integrate with GitHub Actions, so that I can deploy code directly to my VPS.** | • Action `dev-vps/deploy` accepts instance ID and SSH key.<br>• Action pushes repo to instance via rsync.<br>• Success/failure status reported in GitHub Actions log. |
| **E6‑S2** | **As a developer, I want to expose a REST API for instance management, so that I can automate provisioning in my own tools.** | • Endpoints: `POST /instances`, `GET /instances/{id}`, `DELETE /instances/{id}`.<br>• API uses OAuth2 bearer tokens.<br>• Rate limiting (100 req/min). |
| **E6‑S3** | **As a developer, I want to add custom monitoring plugins, so that I can extend metrics collection.** | • Plugin upload endpoint accepts Docker image.<br>• Plugin runs as sidecar container.<br>• Metrics exposed to Grafana via Prometheus. |

---

## MVP Release Order

1. **Epic 1** – Onboarding & Self‑Service  
2. **Epic 2** – Configuration & Customization  
3. **Epic 3** – Monitoring & Alerts  
4. **Epic 4** – Billing & Cost Management  
5. **Epic 5** – Security & Compliance  
6. **Epic 6** – Integration & Extensibility  

---

### Notes for the Team
- All UI components should follow the company’s design system (see `arkashira/design-system`).  
- Backend services must be containerized with Docker and orchestrated via Kubernetes.  
- Use the shared `pgvector` knowledge base for any AI‑powered recommendations (e.g., auto‑scaling suggestions).  
- Ensure compliance with data licenses listed in the dataset section when using external data for training or analytics.  

---
