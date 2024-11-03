import gspread
from google.oauth2.service_account import Credentials
import json
import os

class google_sheets_repository:
    def __init__(self):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]


        with open("credentials_sheets.json") as f:
            credentials_dict = json.load(f)
        credentials_dict["private_key"] = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")

        creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
        self.client_sheets  = gspread.authorize(creds)
        self.sheet = self.client_sheets.open_by_key(os.getenv("GOOGLE_SHEET_CONTACT"))


    def execute(self, name, phone, address):
        """
            Agrega un contacto en Google Sheets
        """
        sheet_1 = self.sheet.sheet1
        new_row = [name, phone, address]

        try:
            sheet_1.append_row(new_row)
            print(f"Contacto agregado: {new_row}")
            return {"status": "success", "message": "Contacto creado satisfactoriamente.", "data": new_row}
        except Exception as e:
            print(f"Error al crear el contacto: {e}")
            return None
      

   