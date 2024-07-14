# google_sheets.py

def book_kayak_in_google_sheets(date, time, kayak_type, quantity):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_service_account_key.json', scope)
        gc = gspread.authorize(credentials)

        spreadsheet_id = '1Tw6GGkbsTkv9RsI_9yJ5t2BxFgrJ6KdQV-W1exhBNFQ'
        sheet = gc.open_by_key(spreadsheet_id).worksheet('Admin')

        records = sheet.get_all_records()

        for i, record in enumerate(records):
            if record['Дата'] == date and record['Время'] == time:
                if kayak_type == 'Одноместный каяк':
                    sheet.update_cell(i + 2, 3, quantity)
                elif kayak_type == 'Двухместный каяк':
                    sheet.update_cell(i + 2, 4, quantity)
                elif kayak_type == 'САП':
                    sheet.update_cell(i + 2, 5, quantity)
                break
        else:
            print("Запись не найдена для указанной даты и времени.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
