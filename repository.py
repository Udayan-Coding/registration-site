import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_credentials():
    account_info = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
    }

    credential = ServiceAccountCredentials.from_json_keyfile_dict(account_info,
                                                                  ["https://spreadsheets.google.com/feeds",
                                                                   "https://www.googleapis.com/auth/spreadsheets",
                                                                   "https://www.googleapis.com/auth/drive.file",
                                                                   "https://www.googleapis.com/auth/drive"])
    return credential


def get_sheet(chapter):
    client = gspread.authorize(get_credentials())
    book = client.open_by_key(os.getenv("SHEET_ID"))
    if chapter not in book.worksheets():
        book.add_worksheet(chapter, rows=100, cols=76)
    return book.worksheet(chapter)
