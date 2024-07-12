# google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_data_from_google_sheets():
    # Подключение к Google Sheets
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_service_account_key.json', scope)
    gc = gspread.authorize(credentials)

    # Открытие таблицы
    spreadsheet_id = 'your_spreadsheet_id'
    sheet = gc.open_by_key(spreadsheet_id).sheet1

    # Пример чтения данных
    data = sheet.get_all_records()
    return data
