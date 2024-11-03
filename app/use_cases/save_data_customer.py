from app.repositories.google_sheets_repository import google_sheets_repository

class save_data_customer:
    customer_data = google_sheets_repository()

    def __init__(self):
        pass

    def execute(self, name, phone, address):
        return self.customer_data.execute(name, phone, address)
    