select
    billing_id,
    user_id,
    amount,
    billing_date,
    plan_type
--from public.billing
from {{source('public', 'billing')}}