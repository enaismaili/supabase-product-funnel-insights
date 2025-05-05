select
    project_id,
    user_id,
    project_type,
    created_at
from {{source('public', 'projects')}}