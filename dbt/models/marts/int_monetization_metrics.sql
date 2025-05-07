with users as (
    select user_id, plan, signup_date
    from {{ ref('fct_users') }}
),

billing as (
    select user_id, billing_date, amount, plan_type
    from {{ ref('fct_billing') }}
),

first_paid_event as (
    select 
        user_id,
        min(billing_date) as upgrade_date
    from billing
    where amount > 0
    group by user_id
),

last_billing as (
    select 
        user_id,
        max(billing_date) as last_billed
    from billing
    group by user_id
),

revenue_by_user as (
    select 
        user_id,
        sum(amount) as total_revenue
    from billing
    group by user_id
)

select
    u.user_id,
    u.signup_date,
    u.plan,
    fpe.upgrade_date,
    lb.last_billed,
    case 
        when lb.last_billed < current_date - interval '30 days' then true 
        else false 
    end as is_churned,
    rbu.total_revenue
from users u
left join first_paid_event fpe on u.user_id = fpe.user_id
left join last_billing lb on u.user_id = lb.user_id
left join revenue_by_user rbu on u.user_id = rbu.user_id