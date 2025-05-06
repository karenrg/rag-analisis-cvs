from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_FOLDER = os.getenv("GITHUB_FOLDER", "")