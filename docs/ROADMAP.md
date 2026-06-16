# Roadmap – dev‑vps

## Vision
**dev‑vps** is a managed VPS platform tailored for developers. It removes the operational overhead of provisioning, scaling, and maintaining virtual machines, allowing teams to focus on code, not infra. The product will be built on Axentx’s proven infrastructure stack, leveraging our existing data‑driven insights and rapid‑iteration pipeline.

---

## MVP (Must‑Have for Launch)

| # | Feature | Owner | Acceptance Criteria | Notes |
|---|---------|-------|---------------------|-------|
| 1 | **Self‑service portal** – user registration, login, and dashboard | PM / Front‑end | • Users can sign up with email or GitHub SSO.<br>• Dashboard shows current VPS instances, usage, and billing. | Critical for first‑time adoption. |
| 2 | **One‑click VPS provisioning** | Backend / DevOps | • User selects OS image, CPU, RAM, disk.<br>• Instance starts within 30 s.<br>• SSH key auto‑generated and displayed. | Core value proposition. |
| 3 | **Secure SSH access** | Security | • Public key authentication only.<br>• Auto‑rotate keys every 90 days. | Must meet dev‑security standards. |
| 4 | **Basic monitoring & alerts** | Ops | • CPU, memory, disk usage metrics.<br>• Email/SMS alert on threshold breach. | Enables quick issue detection. |
| 5 | **Billing & usage analytics** | Finance / Backend | • Pay‑as‑you‑go model.<br>• Exportable CSV of usage. | Enables revenue validation. |
| 6 | **Support & knowledge base** | Customer Success | • Ticketing integration (e.g., Zendesk).<br>• Self‑service docs. | Reduces churn. |

> **MVP‑Critical**: Items 1‑5. Item 6 is important for retention but can be rolled out in v1.

---

## v1 – Core Platform Enhancements

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **Scalability** | Auto‑scaling groups | DevOps | • Instances auto‑scale based on CPU/memory thresholds.<br>• Minimum/maximum limits configurable. |
| **Developer Experience** | One‑click Docker image deployment | Front‑end / Backend | • User selects Docker image; container starts in < 20 s.<br>• Auto‑generated port mapping. |
| **Security** | Managed firewall & IP whitelisting | Security | • Users can whitelist IP ranges.<br>• Default deny‑all inbound except SSH. |
| **Observability** | Centralized logs & metrics | Ops | • Logs shipped to Loki/Prometheus.<br>• Grafana dashboards pre‑built. |
| **Marketplace** | Pre‑built dev stacks (Node, Python, Go) | PM / Backend | • One‑click stack install.<br>• Includes recommended tooling (VS Code Server, Git). |
| **Billing** | Subscription plans | Finance | • Monthly/annual plans with discounts.<br>• Auto‑renewal and cancellation flow. |

> **v1‑Critical**: Auto‑scaling, Docker deployment, firewall, and subscription billing.

---

## v2 – Enterprise & Automation

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **CI/CD Integration** | GitHub Actions runner as VPS | DevOps | • Runner auto‑provisioned on demand.<br>• Runs within 10 s of job trigger. |
| **Multi‑tenant Isolation** | Namespace & resource quotas | Security | • Each tenant has isolated network namespace.<br>• Resource limits enforced at hypervisor level. |
| **Advanced Monitoring** | AI‑driven anomaly detection | Data Science | • Detects abnormal usage patterns.<br>• Auto‑scales or alerts accordingly. |
| **Marketplace Expansion** | Third‑party stack integrations | PM | • Marketplace API for external vendors.<br>• Vetting workflow for new stacks. |
| **Compliance** | GDPR & SOC 2 readiness | Legal | • Data residency options.<br>• Audit logs retained 12 months. |
| **Developer Tools** | VS Code Server & GitHub Codespaces support | Front‑end | • In‑browser IDE pre‑configured.<br>• Seamless SSH key sync. |

> **v2‑Critical**: CI/CD runner, multi‑tenant isolation, and compliance features.

---

## Release Cadence

| Release | Target Date | Scope |
|---------|-------------|-------|
| **MVP** | Q3 2026 | Core portal, provisioning, SSH, monitoring, billing |
| **v1** | Q1 2027 | Auto‑scaling, Docker stacks, firewall, subscription billing |
| **v2** | Q3 2027 | CI/CD runner, multi‑tenant isolation, compliance, marketplace |

---

## Success Metrics

| Metric | Target |
|--------|--------|
| **Activation** | 1,000 active VPS instances by end of MVP |
| **Retention** | 70 % monthly churn rate ≤ 10 % |
| **Revenue** | $50k ARR by end of v1 |
| **Support** | Avg. ticket resolution < 4 h |
| **Compliance** | SOC 2 Type II audit passed by end of v2 |

---

## Dependencies & Risks

- **Infrastructure**: Requires robust hypervisor layer; we’ll use our existing cloud‑agnostic stack (KVM + libvirt).  
- **Security**: Zero‑trust SSH model; need to audit key rotation.  
- **Billing**: Integration with Stripe; ensure PCI‑DSS compliance.  
- **Data**: Leverage existing `auto` and `instr-resp` datasets for auto‑scaling heuristics.  

---

## Next Steps

1. Finalize MVP feature list with stakeholders.  
2. Set up sprint backlog and assign owners.  
3. Begin rapid prototyping of the self‑service portal.  
4. Draft compliance checklist for SOC 2.  

---
