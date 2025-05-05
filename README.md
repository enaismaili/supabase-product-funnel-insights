# Supabase Product Funnel Insights App

Simulate and analyze Supabase-style product usage funnels — from user activation to retention and monetization — using dbt, SQL, and Tableau Public.

---

## 📊 Project Summary

This project mimics the kind of analysis a data analyst at Supabase might perform to support product and strategy decisions. It uses a simulated dataset modeled on realistic product behavior and tracks the full lifecycle:

**Activation → Retention → Monetization**

---

## 🛠️ Stack

| Area              | Tool                 |
|-------------------|----------------------|
| Database          | Supabase (PostgreSQL) |
| Data Simulation   | Python + Faker        |
| Transformation    | dbt                   |
| Visualization     | Tableau Public        |
| Docs & Hosting    | GitHub, GitHub Pages  |

---

## 🎯 Project Goals

- Simulate user events across a product lifecycle (signup → feature use → billing)
- Model funnel metrics and KPIs using SQL + dbt
- Visualize product insights for stakeholders (activation drop-offs, retention cohorts, revenue trends)
- Host and document as a full end-to-end portfolio project

---

## 📈 Key Metrics Tracked

- **Activation Funnel**: Signup → Project Created → Feature Used
- **Retention**: DAU, WAU, MAU, and Cohort Analysis
- **Monetization**: MRR, upgrade rates, churn, freemium → paid

---

## 🧱 dbt Models Overview

This project uses a layered dbt structure with `staging` and `marts` folders. Below is a summary of each model and what it does.

| Model Name               | Layer     | File Path                                | Description                                                                                     | Output Schema         |
|--------------------------|-----------|-------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------|
| `fct_users`              | Staging   | `models/staging/fct_users.sql`            | Cleans and exposes user data from the Supabase DB                                                | `supabase_funnel`     |
| `fct_projects`           | Staging   | `models/staging/fct_projects.sql`         | Cleans project creation events linked to users                                                   | `supabase_funnel`     |
| `fct_events`             | Staging   | `models/staging/fct_events.sql`           | Normalizes event logs (e.g., table creation, auth events)                                        | `supabase_funnel`     |
| `fct_billing`            | Staging   | `models/staging/fct_billing.sql`          | Prepares user billing data and monetization signals                                              | `supabase_funnel`     |
| `int_activation_funnel` | Marts      | `models/marts/int_activation_funnel.sql`  | Tracks user journey from signup → project creation → feature usage, with drop-off indicators     | `supabase_funnel`     |

---

### 🧠 Funnel Analysis Value

The `int_activation_funnel` model answers:

- Who signed up but didn’t create a project?
- Who created a project but didn’t use a feature?
- When each user hit each funnel stage?

This data supports growth, activation, and onboarding optimization.

---

## 📊 Live Dashboard

*Coming soon* – hosted on Tableau Public  
(Link will be added here when the dashboard is published.)

---

## 📎 Disclaimer

All data is simulated and does not represent real Supabase user behavior. The intent is educational.

---

**Author**: Enisa Ismaili, 2025