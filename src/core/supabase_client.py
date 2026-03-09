import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from supabase import create_client, Client

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

def get_secret(name: str):
    value = os.getenv(name)
    if value:
        return value

    try:
        return st.secrets[name]
    except Exception:
        return None

SUPABASE_URL = get_secret("SUPABASE_URL")
SUPABASE_KEY = get_secret("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is missing")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_card(question: str, answer: str, image_url: str, public_id: str):
    data = {
        "question": question,
        "answer": answer,
        "image_url": image_url,
        "public_id": public_id,
    }
    return supabase.table("cards").insert(data).execute()


def get_latest_cards(limit: int = 5):
    return (
        supabase.table("cards")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )


def get_cards_count():
    return (
        supabase.table("cards")
        .select("id", count="exact")
        .execute()
    )