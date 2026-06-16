# Product Requirements Document – dev‑vps

**Project:** dev‑vps  
**Owner:** Axentx Product Team  
**Version:** 1.0 – 2026‑06‑16  
**Status:** Draft

---

## 1. Problem Statement

Developers spend a disproportionate amount of time provisioning, configuring, and maintaining virtual private servers (VPS).  
- **Setup friction:** Manual SSH key management, OS image selection, and dependency installation create onboarding delays.  
- **Operational overhead:** Security patches, backups, and scaling decisions fall on the developer, diverting focus from code.  
- **Cost inefficiency:** Idle servers or over‑provisioned resources lead to unnecessary spend.  
- **Collaboration gaps:** Sharing environments across teams is error‑prone and hard to version.

**Result:** Developers waste 20‑30 % of their time on infrastructure, reducing velocity and increasing time‑to‑delivery.

---

## 2. Target Users

| Persona | Role | Pain Points | Desired Outcomes |
|---------|------|-------------|------------------|
| **Solo Developer / Indie** | Full‑stack engineer | Needs quick, low‑maintenance hosting for prototypes | One‑click VPS, auto‑scaling, zero admin |
| **Startup Team** | CTO / DevOps | Requires reproducible dev environments, CI integration | Immutable snapshots, easy rollback, cost control |
| **Enterprise DevOps** | Site Reliability Engineer | Needs compliance, monitoring, and multi‑region support | Auditable logs, auto‑patching, SLA guarantees |
| **Educators / Students** | Instructor / Learner | Wants isolated, shareable labs | Self‑contained environments, auto‑reset |

---

## 3. Goals & Success Metrics

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Reduce onboarding time** | Avg. time from “Create VPS” to “Ready for code” | < 2 min |
| **Lower operational overhead** | % of manual server maintenance tasks | < 5 % |
| **Improve cost efficiency** | Avg. cost per active hour | $0.02/h (incl. auto‑shutoff) |
| **Enhance collaboration** | % of environments shared without manual setup | 90 % |
| **Drive adoption** | Monthly active users | 5,000 by Q4 2026 |
| **Ensure reliability** | 99.9 % uptime, 1 min max recovery | 99.9 % |

---

## 4. Key Features (Prioritized)

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|---------------------|
| **1** | **One‑Click VPS Provisioning** | Users select OS, region, and size; system auto‑creates a VM with default dev stack (Node.js, Python, Docker, Git). | • Provision completes < 2 min.<br>• SSH key auto‑generated and added to instance. |
| **2** | **Immutable Environment Snapshots** | Snapshots of the base image are versioned; developers can roll back to a known good state. | • Snapshot creation < 30 s.<br>• Rollback restores exact state. |
| **3** | **Auto‑Patch & Security Updates** | Background agent applies OS and package updates; alerts on critical vulnerabilities. | • Updates applied within 24 h of release.<br>• No downtime during patching. |
| **4** | **Integrated CI/CD Runner** | VPS can be used as a GitHub Actions runner or self‑hosted runner with pre‑installed tools. | • Runner registers automatically.<br>• Build logs accessible via UI. |
| **5** | **Auto‑Shutdown & Scaling** | Idle VPS shut down after configurable timeout; auto‑scale based on CPU/memory thresholds. | • Idle timeout configurable (5‑60 min).<br>• Scale‑up/down triggers within 2 min. |
| **6** | **Environment Sharing & Collaboration** | Shareable URLs with token‑based access; team dashboards. | • Invite link works for 3 users.<br>• Permissions (read/write) configurable. |
| **7** | **Cost Dashboard & Alerts** | Real‑time cost monitoring, budget alerts, exportable reports. | • Cost displayed per hour.<br>• Alert sent when threshold exceeded. |
| **8** | **Compliance & Auditing** | Immutable logs, role‑based access, SOC‑2‑ready audit trail. | • Log retention 90 days.<br>• Exportable audit logs. |
| **9** | **Marketplace Extensions** | Plugin system for adding language runtimes, databases, CI tools. | • Third‑party plugin installs in < 1 min. |
| **10** | **Multi‑Region Deployment** | Users can spin up VPS in any supported region; latency‑aware routing. | • Region selection in UI.<br>• Latency < 80 ms to primary region. |

---

## 5. Scope

| Item | Included | Excluded |
|------|----------|----------|
| **Core VPS Engine** | ✔ | ❌ |
| **User Management** | ✔ | ❌ |
| **Billing & Subscription** | ✔ | ❌ |
| **Marketplace Extensions** | ✔ | ❌ |
| **Enterprise SSO & LDAP** | ✔ | ❌ |
| **Custom OS Images** | ✔ | ❌ |
| **Bare‑Metal Hosting** | ❌ | ✔ |
| **Container‑Only Service** | ❌ | ✔ |
| **On‑Prem Deployment** | ❌ | ✔ |

---

## 6. Dependencies

- **Infrastructure**: AWS EC2, GCP Compute Engine, Azure VMs (multi‑cloud).  
- **Orchestration**: Terraform + Pulumi for IaC.  
- **Monitoring**: Prometheus + Grafana; CloudWatch integration.  
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins.  
- **Security**: OpenSSH, fail2ban, CIS Benchmarks.  
- **Billing**: Stripe API, internal cost‑allocation service.  

---

## 7. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Vendor lock‑in** | High | Use Terraform modules for multi‑cloud abstraction. |
| **Security breaches** | Critical | Harden SSH, enable MFA, run CIS scans nightly. |
| **Cost overruns** | Medium | Auto‑shutdown, real‑time cost alerts, budget caps. |
| **Feature creep** | Medium | Strict feature gating, backlog prioritization. |
| **Compliance gaps** | High | SOC‑2 audit, regular penetration testing. |

---

## 8. Timeline (Milestones)

| Phase | Deliverable | Target Date |
|-------|-------------|-------------|
| **Research & Design** | Architecture doc, user flows | 2026‑07‑15 |
| **MVP Core** | One‑click provisioning, SSH access | 2026‑08‑31 |
| **Beta Release** | Snapshots, auto‑patch, CI runner | 2026‑10‑15 |
| **Public Launch** | Full feature set, billing, marketplace | 2026‑12‑01 |
| **Post‑Launch** | Auto‑scaling, multi‑region, compliance | 2027‑02‑01 |

---

## 9. Success Criteria

- **Adoption**: 5,000 MAU by Q4 2026.  
- **Retention**: 70 % of users continue after 30 days.  
- **Revenue**: $200k ARR by end of 2026.  
- **Customer Satisfaction**: NPS ≥ 50.  

---

## 10. Appendices

- **User Journey Maps** (attached in separate folder).  
- **Technical Architecture Diagram** (link to repo `docs/architecture.png`).  
- **Compliance Checklist** (link to repo `docs/compliance.md`).  

---
