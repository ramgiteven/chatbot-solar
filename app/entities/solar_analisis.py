class SolarAnalysis:
    def __init__(self, address: str, monthly_bill: int, financial_analysis: dict):
        """
        Inicializa un nuevo análisis solar con una dirección, factura mensual y los datos del análisis financiero.
        
        :param address: Dirección donde se realiza el análisis
        :param monthly_bill: Factura mensual del usuario
        :param financial_analysis: Datos del análisis financiero
        """
        self.address = address
        self.monthly_bill = monthly_bill
        self.financial_analysis = financial_analysis

    def get_analysis_summary(self):
        """
        Devuelve un resumen básico del análisis financiero.
        """
        return {
            "address": self.address,
            "monthly_bill": self.monthly_bill,
            "savings_estimate": self.financial_analysis.get('savings', 'N/A'),
            "payback_period": self.financial_analysis.get('paybackPeriod', 'N/A')
        }

    def update_analysis(self, new_financial_analysis: dict):
        """
        Actualiza los datos del análisis financiero.
        
        :param new_financial_analysis: Nuevos datos del análisis financiero
        """
        self.financial_analysis = new_financial_analysis
