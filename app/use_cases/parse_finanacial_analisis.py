from app.repositories.openai_repository import openai_repository

class parse_financial_analisis:
    openai_repository_instance = openai_repository()

    def __init__(self):
        pass

    def execute(self, user_bill, financial_analyses):
        closest_financial_analysis = None
        smallest_difference = float('inf')
        for analysis in financial_analyses:
            bill_amount = int(analysis.get('monthlyBill', {}).get('units', 0))
            difference = abs(bill_amount - user_bill)
            if difference < smallest_difference:
                smallest_difference = difference
                closest_financial_analysis = analysis

        if closest_financial_analysis:
            return self.openai_repository_instance.simplify_financial_data_with_gpt(closest_financial_analysis)
        else:
            return {
                "error": "No se encontró ningún análisis financiero adecuado para la facturaciòn en cuestión."
            }
    