# Customer Journey Map – dev‑vps

| Phase | Trigger Event | Friction Points | User Emotions | Opportunities to Delight | Metric |
|-------|---------------|-----------------|---------------|--------------------------|--------|
| **Aware** | • Blog post or tutorial on “Why dev‑VPS beats local Docker” <br>• Social‑media ad (LinkedIn, Twitter) <br>• Word‑of‑mouth from a colleague | • Low brand visibility in niche dev forums <br>• Unclear value proposition in one‑liner | Curious, skeptical | • SEO‑optimized landing page with instant value‑calc <br>• Short explainer video (≤ 90 s) <br>• Live chat bot answering “What’s dev‑vps?” | 1. **Impressions** – 150 k/month <br>2. **Click‑through rate** – 4.5 % <br>3. **New sign‑ups** – 3 % of clicks |
| **Consider** | • Requesting a free trial or demo <br>• Attending a webinar on “Managed VPS for dev teams” | • Complex pricing tiers <br>• Lack of clear ROI calculator <br>• Uncertain security compliance | Hopeful, cautious | • One‑click trial signup (no credit card) <br>• Interactive ROI calculator (cost vs. local dev) <br>• Security badge & compliance docs | 1. **Trial sign‑ups** – 1 k/month <br>2. **Demo requests** – 200/month <br>3. **Bounce rate** – < 30 % |
| **Try** | • First login & environment provisioning <br>• First code push to VPS | • Slow provisioning (< 5 min) <br>• Limited OS images <br>• No auto‑backup | Frustrated, then relieved | • Instant “Hello World” tutorial <br>• One‑click OS image selection <br>• Auto‑snapshot on every push <br>• 24/7 live support | 1. **Active users** – 70 % of trials <br>2. **Feature adoption** – 60 % of core features <br>3. **Support tickets** – < 1 per 10 users |
| **Adopt** | • Subscription plan selected (e.g., $19/month) <br>• First billing cycle | • Billing confusion <br>• Limited scalability options <br>• No clear upgrade path | Confident, satisfied | • Transparent billing dashboard <br>• Auto‑scale alerts <br>• “Upgrade now” upsell with 10 % discount <br>• Customer success onboarding call | 1. **Conversion rate** – 30 % of trials <br>2. **Churn** – < 5 %/month <br>3. **NPS** – 45 |
| **Expand** | • Team invites new members <br>• Requesting additional resources (GPU, storage) | • Feature parity gaps for larger teams <br>• Integration friction with CI/CD pipelines <br>• Limited API access | Loyal, advocate | • Multi‑user billing <br>• API key & webhook docs <br>• Referral program (10 % credit) <br>• Quarterly roadmap Q&A | 1. **Upsell revenue** – 25 % of base <br>2. **Referral sign‑ups** – 15 % of active users <br>3. **Retention** – 95 % 1‑yr |

---

## Phase Details

### Aware
- **Trigger Event**: Developer reads a blog post titled *“Stop Wasting Time on VPS Setup”* or sees a LinkedIn ad.
- **Friction**: Brand unknown, generic messaging.
- **Emotions**: Curiosity, mild skepticism.
- **Delight**: Instant value calculator, clear pricing snapshot, social proof (case studies).
- **Metric**: Aim for 4.5 % CTR on paid ads; 150 k monthly impressions.

### Consider
- **Trigger Event**: Developer clicks “Start Free Trial” or registers for a webinar.
- **Friction**: Pricing complexity, unclear ROI, no free trial.
- **Emotions**: Hopeful, cautious.
- **Delight**: One‑click trial, interactive ROI calculator, security compliance badges.
- **Metric**: 1 k trial sign‑ups/month, demo requests 200/month, bounce < 30 %.

### Try
- **Trigger Event**: First login, environment provisioning.
- **Friction**: Slow provisioning, limited OS images, no auto‑backup.
- **Emotions**: Frustration → relief.
- **Delight**: Instant “Hello World” tutorial, auto‑snapshot, 24/7 support.
- **Metric**: 70 % of trials become active users, 60 % core feature adoption, < 1 support ticket per 10 users.

### Adopt
- **Trigger Event**: Subscription plan chosen, billing cycle starts.
- **Friction**: Billing confusion, limited scalability, no upgrade path.
- **Emotions**: Confidence, satisfaction.
- **Delight**: Transparent billing, auto‑scale alerts, upsell with discount, onboarding call.
- **Metric**: 30 % conversion from trial to paid, churn < 5 %/month, NPS 45.

### Expand
- **Trigger Event**: Team invites, resource requests.
- **Friction**: Feature gaps for larger teams, CI/CD integration friction, limited API.
- **Emotions**: Loyalty, advocacy.
- **Delight**: Multi‑user billing, API docs, referral program, roadmap Q&A.
- **Metric**: Upsell revenue 25 % of base, 15 % referral sign‑ups, 95 % 1‑yr retention.

---

**Next Steps**  
- Implement instant value calculator on landing page.  
- Reduce provisioning time to < 3 min.  
- Launch referral program with 10 % credit.  
- Track metrics via GA + Mixpanel dashboards.