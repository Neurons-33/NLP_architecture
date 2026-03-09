import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import cloudinary

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

def init_cloudinary():
    cloudinary.config(
        cloud_name=get_secret("CLOUDINARY_CLOUD_NAME"),
        api_key=get_secret("CLOUDINARY_API_KEY"),
        api_secret=get_secret("CLOUDINARY_API_SECRET"),
    )

init_cloudinary()

GOOGLE_API_KEY = get_secret("GOOGLE_API_KEY")