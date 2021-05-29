import gspread
from oauth2client.service_account import ServiceAccountCredentials

from . import settings


def get_credentials():
    account_info = {
        "type": "service_account",

        "project_id": settings.project_id(),
        "private_key_id": settings.private_key_id(),
        "private_key": settings.private_key(),
        "client_email": settings.client_email(),
        "client_id": settings.client_id(),

        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
    }

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
    ]

    credential = ServiceAccountCredentials.from_json_keyfile_dict(account_info,
                                                                  scopes)
    return credential


def get_sheet(chapter):
    client = gspread.authorize(get_credentials())
    book = client.open_by_key(settings.sheet_id())
    worksheets = [worksheet.title for worksheet in book.worksheets()]

    if chapter not in worksheets:
        book.add_worksheet(chapter, rows=100, cols=76)
    return book.worksheet(chapter)
