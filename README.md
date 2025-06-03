# Supabase Product Funnel Insights App

Simulate and analyze Supabase-style product usage funnels — from user activation to retention and monetization — using Supabase, dbt, SQL, and Hex.

---

## 📊 Project Summary

This project delivers lifecycle analytics across **activation**, **retention**, and **monetization**, modeled on product data pipelines similar to those used by modern digital products. Using simulated behavioral and billing data based on realistic usage patterns, the analysis provides a comprehensive view of user engagement and revenue dynamics.

**Activation → Retention → Monetization**

---

## 🛠️ Stack

| Area              | Tool                  |
|-------------------|-----------------------|
| Database          | Supabase (PostgreSQL) |
| Data Simulation   | Python + Faker        |
| Transformation    | dbt                   |
| Visualization     | Hex                   |
| Docs & Hosting    | GitHub, GitHub Pages  |

---

## 🎯 Project Goals

- Simulate user lifecycle events (signup → feature use → billing)
- Model activation funnels, retention cohorts, and monetization metrics
- Analyze product usage patterns to surface behavioral insights
- Present findings in an interactive dashboard format for exploration

---

## 📈 Key Metrics Tracked

- **Activation Funnel**: Signup → Project Created → Feature Used
- **Retention**: DAU, WAU, MAU, and Cohort-Based Retention
- **Monetization**: MRR, Upgrade Events, Churn Rates, Freemium → Paid

---

## 🧱 dbt Models Overview

| Model Name                 | Layer     | Description                                                                                       |
|----------------------------|-----------|----------------------------------------------------------------------------------------------------|
| `fct_users`                | Staging   | Cleans and exposes user-level data                                                                |
| `fct_projects`             | Staging   | Cleans project creation events linked to users                                                    |
| `fct_events`               | Staging   | Normalizes event logs (e.g., table creation, auth events)                                         |
| `fct_billing`              | Staging   | Prepares user billing and plan data                                                               |
| `int_activation_funnel`    | Marts     | Tracks user progression from signup → project creation → feature use                              |
| `int_retention_metrics`    | Marts     | Aggregates DAU, WAU, MAU over time using rolling windows                                          |
| `int_retention_cohorts`    | Marts     | Builds week-based signup cohorts and tracks retention across weeks                                |
| `int_monetization_metrics` | Marts     | Captures upgrade dates, churn status, and total revenue per user                                  |
| `int_mrr_by_month`         | Marts     | Calculates Monthly Recurring Revenue (MRR) segmented by plan and billing month                    |

---

### 🧠 Funnel Analysis Value

The `int_activation_funnel` model answers:

- Who signed up but didn’t create a project?
- Who created a project but didn’t use a feature?
- When did users hit each funnel milestone?

---

### 🧠 Retention Analysis Value

The `int_retention_metrics` and `int_retention_cohorts` models answer:

- How many users return daily, weekly, or monthly?
- What percentage of users remain active after 1, 2, or 4+ weeks?
- How does retention vary across signup cohorts?

---

### 🧠 Monetization Analysis Value

The `int_monetization_metrics` and `int_mrr_by_month` models answer:

- When do users convert to paid plans?
- Who has churned?
- What is the total revenue per user?
- How is MRR evolving month-over-month?

---

## 📊 Live Dashboard

👉 [View Interactive Hex Dashboard](https://app.hex.tech/0196c415-b593-7111-b943-46da3d29a52c/app/0196c58b-b00d-7116-a2aa-464d145e7ab8/latest)  

**Dashboard Screenshots:**

<img width="1507" alt="supabase dash 1" src="https://github.com/user-attachments/assets/12c69bf4-7a02-4d6b-9bd7-c58a25894c3b" />
<img width="1503" alt="supabase dash 2" src="https://github.com/user-attachments/assets/185f47f7-eb37-4a9b-810a-622d68b3fd41" />
<img width="1503" alt="supabase dash 3" src="https://github.com/user-attachments/assets/5eadb8b9-60bc-4fc0-9e34-3b2729e6b439" />

---

## 📎 Disclaimer

This project uses simulated data that does not represent real Supabase users or behavior. It is created for educational purposes only and is not affiliated with or endorsed by Supabase.

Because the data is randomly generated, some logical inconsistencies may occur — for example:
- Users who “used a feature” without having first “created a project”
- Fluctuating MRR or upgrade behavior not tied to real customer behavior

These quirks are a normal part of randomized simulation and are left intentionally to reflect the complexity of real-world modeling.

---

**Author**: Enisa Ismaili · 2025
