from supabase import create_client, Client
from faker import Faker
from dotenv import load_dotenv 
import os
import uuid
import random
from datetime import datetime, timedelta

load_dotenv()

# API data
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
fake = Faker()

NUM_USERS = 1000 #1000 simulated users

users = []
projects = []
events = []
billing = []

print("Simulating data...")

for _ in range(NUM_USERS):
    user_id = str(uuid.uuid4())
    signup_date = fake.date_time_between(start_date="-180d", end_date="now")
    
    # user profile
    users.append({
        "user_id": user_id,
        "signup_date": signup_date.isoformat(),
        "plan": random.choice(["free", "pro", "team"]),
        "lifecycle_stage": random.choice(["active", "inactive", "churned"])
    })

    # optional project creation (70% chance)
    if random.random() < 0.7:
        projects.append({
            "project_id": str(uuid.uuid4()),
            "user_id": user_id,
            "project_type": random.choice(["personal", "collab", "demo"]),
            "created_at": (signup_date + timedelta(days=random.randint(1, 14))).isoformat()
        })

    # realistic weekly event activity over 5 weeks (retention logic)
    for week_offset in range(5):
        # higher engagement in earlier weeks
        if random.random() < [1.0, 0.3, 0.2, 0.1, 0.05][week_offset]:
            num_events = random.randint(1, 3)
            for _ in range(num_events):
                event_time = signup_date + timedelta(days=week_offset * 7 + random.randint(0, 5))
                events.append({
                    "event_id": str(uuid.uuid4()),
                    "user_id": user_id,
                    "event_type": random.choice(["sign_up", "project_created", "table_created", "auth_used", "api_call"]),
                    "timestamp": event_time.isoformat()
                })

    # optional billing event (50% chance)
    if random.random() < 0.5:
        billing.append({
            "billing_id": str(uuid.uuid4()),
            "user_id": user_id,
            "amount": round(random.uniform(5, 99), 2),
            "billing_date": (signup_date + timedelta(days=random.randint(10, 90))).isoformat(),
            "plan_type": random.choice(["monthly", "yearly"])
        })

print("Uploading to Supabase...")

supabase.table("users").insert(users).execute()
supabase.table("projects").insert(projects).execute()
supabase.table("events").insert(events).execute()
supabase.table("billing").insert(billing).execute()

print("Simulation complete - data inserted.")
