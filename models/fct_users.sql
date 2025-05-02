select
    user_id,
    signup_date,
    plan,
    lifecycle_stage
from {{ source('public', 'users') }}

--from public.users