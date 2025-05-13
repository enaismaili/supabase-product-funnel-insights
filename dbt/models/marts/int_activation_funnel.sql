with users as (
    select user_id, signup_date from {{ ref('fct_users') }}
),

projects as (
    select user_id, min(created_at) as first_project_date
    from {{ ref('fct_projects') }}
    group by user_id
),

events as (
    select user_id, min(timestamp) as first_feature_use
    from {{ ref('fct_events') }}
    where event_type in ('project_created', 'table_created')
    group by user_id
)

select
    u.user_id,
    u.signup_date,
    p.first_project_date,
    e.first_feature_use,

    -- Funnel step flags
    case when p.first_project_date is not null then true else false end as reached_step_2,
    case when e.first_feature_use is not null then true else false end as reached_step_3
from users u
left join projects p on u.user_id = p.user_id
left join events e on u.user_id = e.user_id