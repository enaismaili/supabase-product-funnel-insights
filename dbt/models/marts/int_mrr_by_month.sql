with monthly_billing as (
    select
        date_trunc('month', billing_date) as billing_month,
        plan_type,
        sum(amount) as mrr
    from {{ ref('fct_billing') }}
    where amount > 0
    group by billing_month, plan_type
)

select *
from monthly_billing
order by billing_month, plan_type