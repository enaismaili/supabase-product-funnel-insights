with events as (
    select 
        user_id,
        date_trunc('day', timestamp) as activity_date
    from {{ ref('fct_events') }}
),

-- Get 1 row per active user per day
daily_user_activity as (
    select distinct
        user_id,
        activity_date
    from events
),

-- Count unique users per day = DAU
daily_agg as (
    select
        activity_date,
        count(user_id) as dau
    from daily_user_activity
    group by activity_date
),

-- For WAU and MAU, count unique users seen in past 7/30 days
rolling_users as (
    select
        d.activity_date,
        d.dau,
        (
            select count(distinct user_id)
            from daily_user_activity du
            where du.activity_date between d.activity_date - interval '6 days' and d.activity_date
        ) as wau,
        (
            select count(distinct user_id)
            from daily_user_activity du
            where du.activity_date between d.activity_date - interval '29 days' and d.activity_date
        ) as mau
    from daily_agg d
)

select *
from rolling_users
order by activity_date