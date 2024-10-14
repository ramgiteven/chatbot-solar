from app.repositories.openai_repository import openai_repository

class parse_financial_analisis:
    def __init__(self):
        # Instanciar el repositorio de OpenAI y obtener el cliente
        self.openai_repository = openai_repository()

    def execute(self, user_bill, financial_analyses):
        print(f" execute GenerateFinancialAnalisis { user_bill, financial_analyses}")
        closest_financial_analysis = None
        smallest_difference = float('inf')
        for analysis in financial_analyses:
            bill_amount = int(analysis.get('monthlyBill', {}).get('units', 0))
            difference = abs(bill_amount - user_bill)
            if difference < smallest_difference:
                smallest_difference = difference
                closest_financial_analysis = analysis

        if closest_financial_analysis:
            return self.openai_repository.simplify_financial_data_with_gpt(closest_financial_analysis)
        else:
            print("No suitable financial analysis found.")
            return {
                "error": "No suitable financial analysis found for the given bill."
            }
    