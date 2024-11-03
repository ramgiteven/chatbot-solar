import os

class airtable_repository:
    def __init__(self):
        pass
        """""
        self.api_key = os.getenv('AIRTABLE_API_KEY')
        self.base_id = 'appTbPd6hbHBvMHlc'
        self.table_name = "Leads"

        if not self.api_key or not self.base_id:
            raise ValueError("La API Key o Base ID de Airtable no están configurados.")
        """""
    def execute(self, name, phone, address):
        pass
        """"  
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
            print("Contacto creado satisfactoriamente.")
            return response.json()
        else:
            print(f"Fallo al crear el contacto: {response.text}")
            return None
        """""