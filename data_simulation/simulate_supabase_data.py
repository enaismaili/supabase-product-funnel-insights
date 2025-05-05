from supabase import create_client, Client
from faker import Faker
from dotenv import load_dotenv 
import os
import uuid
import random
from datetime import datetime, timedelta

load_dotenv()

#Supabase API info
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
fake = Faker()

#Config
NUM_USERS = 1000

users = []
projects = []
events = []
billing = []

print("Simulating data...")

for _ in range(NUM_USERS):
    user_id = str(uuid.uuid4())
    signup_date = fake.date_time_between(start_date="-180d", end_date="now")
    
    users.append({
        "user_id": user_id,
        "signup_date": signup_date.isoformat(),
        "plan": random.choice(["free", "pro", "team"]),
        "lifecycle_stage": random.choice(["active", "inactive", "churned"])
    })

    if random.random() < 0.7:
        projects.append({
            "project_id": str(uuid.uuid4()),
            "user_id": user_id,
            "project_type": random.choice(["personal", "collab", "demo"]),
            "created_at": (signup_date + timedelta(days=random.randint(1, 14))).isoformat()
        })

    for _ in range(random.randint(1, 5)):
        events.append({
            "event_id": str(uuid.uuid4()),
            "user_id": user_id,
            "event_type": random.choice(["sign_up", "project_created", "table_created", "auth_used", "api_call"]),
            "timestamp": (signup_date + timedelta(days=random.randint(1, 30))).isoformat()
        })

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