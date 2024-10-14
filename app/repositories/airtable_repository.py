import os
import requests

class airtable_repository:
    def __init__(self):
        self.api_key = os.getenv('AIRTABLE_API_KEY')
        self.base_id = 'appTbPd6hbHBvMHlc'
        self.table_name = "Leads"

        if not self.api_key or not self.base_id:
            raise ValueError("La API Key o Base ID de Airtable no están configurados.")

    def execute(self, name, phone, address):
        """
            Create lead Airtable
        """
        url = f"https://api.airtable.com/v0/{self.base_id}/{self.table_name}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "records": [{
                "fields": {
                    "Name": name,
                    "Phone": phone,
                    "Address": address
                }
            }]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("Lead created successfully.")
            return response.json()
        else:
            print(f"Failed to create lead: {response.text}")
            return None
