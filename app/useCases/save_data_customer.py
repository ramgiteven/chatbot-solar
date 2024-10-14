from app.repositories.airtable_repository import airtable_repository

class save_data_customer:
    def __init__(self, repository_customer_Data = airtable_repository):
        self.repositoryCustomerData = repository_customer_Data()


    def execute(self, name, phone, address):
        return self.repositoryCustomerData.execute(name, phone, address)
    