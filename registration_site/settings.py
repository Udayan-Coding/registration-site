import os

from dotenv import load_dotenv

load_dotenv()


def project_id():
    return os.getenv("PROJECT_ID")


def private_key_id():
    return os.getenv("PRIVATE_KEY_ID").replace('\\n', '\n')


def private_key():
    return os.getenv("PRIVATE_KEY")


def client_email():
    return os.getenv("CLIENT_EMAIL")


def client_id():
    return os.getenv("CLIENT_ID")


def auth_uri():
    return os.getenv("AUTH_URI")


def token_uri():
    return os.getenv("TOKEN_URI")


def sheet_id():
    return os.getenv("SHEET_ID")


def secret_key():
    return os.getenv("SECRET_KEY")
