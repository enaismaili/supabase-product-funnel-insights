with user_cohorts as (
    select 
        user_id,
        date_trunc('week', signup_date) as signup_week
    from {{ ref('fct_users') }}
),

weekly_activity as (
    select 
        user_id,
        date_trunc('week', timestamp) as activity_week
    from {{ ref('fct_events') }}
    group by user_id, activity_week
),

cohort_activity as (
    select
        u.signup_week,
        a.activity_week,
        floor(extract(epoch from (a.activity_week - u.signup_week)) / 604800) as week_number,
        u.user_id
    from user_cohorts u
    join weekly_activity a 
      on u.user_id = a.user_id
    where a.activity_week >= u.signup_week
)

select
    signup_week,
    week_number,
    count(distinct user_id) as retained_users
from cohort_activity
group by signup_week, week_number
order by signup_week, week_number