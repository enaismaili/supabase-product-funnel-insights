select
    event_id,
    user_id,
    event_type,
    timestamp
--from public.events
from {{ source('public', 'events') }}