# Supabase Product Funnel Insights App

Simulate and analyze Supabase-style product usage funnels — from user activation to retention and monetization — using dbt, SQL, and Tableau Public.

---

## 📊 Project Summary

This project delivers lifecycle analytics across activation, retention, and monetization—modeled on the kind of product data pipelines a Supabase analyst would manage. Using realistic simulated behavioral and billing data, it provides full-funnel insights for strategic decision-making.

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

| Model Name                 | Layer     | File Path                                 | Description                                                                                       | Output Schema     |
|----------------------------|-----------|--------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------|
| `fct_users`                | Staging   | `models/staging/fct_users.sql`             | Cleans and exposes user data from the Supabase DB                                                  | `supabase_funnel` |
| `fct_projects`             | Staging   | `models/staging/fct_projects.sql`          | Cleans project creation events linked to users                                                     | `supabase_funnel` |
| `fct_events`               | Staging   | `models/staging/fct_events.sql`            | Normalizes event logs (e.g., table creation, auth events)                                          | `supabase_funnel` |
| `fct_billing`              | Staging   | `models/staging/fct_billing.sql`           | Prepares user billing data and monetization signals                                                | `supabase_funnel` |
| `int_activation_funnel`    | Marts     | `models/marts/int_activation_funnel.sql`   | Tracks user journey from signup → project creation → feature usage, with drop-off indicators       | `supabase_funnel` |
| `int_retention_metrics`    | Marts     | `models/marts/int_retention_metrics.sql`   | Aggregates DAU, WAU, and MAU by day using rolling activity windows                                 | `supabase_funnel` |
| `int_retention_cohorts`    | Marts     | `models/marts/int_retention_cohorts.sql`   | Builds user-level cohort tables with week-based retention offset since signup                      | `supabase_funnel` |
| `int_monetization_metrics` | Marts     | `models/marts/int_monetization_metrics.sql`| Captures upgrade timing, churn risk, and total revenue by user                                     | `supabase_funnel` |
| `int_mrr_by_month`         | Marts     | `models/marts/int_mrr_by_month.sql`        | Calculates Monthly Recurring Revenue (MRR) grouped by plan type and billing month                 | `supabase_funnel` |

---

### 🧠 Funnel Analysis Value

The `int_activation_funnel` model answers:

- Who signed up but didn’t create a project?
- Who created a project but didn’t use a feature?
- When each user hit each funnel stage?

This data supports growth, activation, and onboarding optimization.

---

### 🧠 Retention Analysis Value

The int_retention_metrics and int_retention_cohorts models answer:
- How many users return daily, weekly, or monthly?
- What percentage of users remain active after 1, 2, 4+ weeks?
- How does retention vary by signup cohort?

This data informs product stickiness, user engagement trends, and cohort health over time.

---

### 🧠 Monetization Analysis Value

The int_monetization_metrics and int_mrr_by_month models answer:
- When did users convert from freemium to paid?
- Who has churned (no billing in 30+ days)?
- How much revenue did each user generate?
- What is monthly recurring revenue (MRR) over time?

These models support monetization strategy, customer segmentation, and LTV forecasting.

---

## 📊 Live Dashboard

*Coming soon* – hosted on Tableau Public  
(Link will be added here when the dashboard is published.)

---

## 📎 Disclaimer

All data is simulated and does not represent real Supabase user behavior. The intent is educational.

---

**Author**: Enisa Ismaili, 2025