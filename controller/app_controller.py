# controller/sales_controller.py
from model.backend import SalesModel

class SalesController:
    def __init__(self, csv_path):
        self.model = SalesModel(csv_path)

    def load_data(self):
        """Load dataset through the model"""
        return self.model.load_data()

    def get_summary(self):
        """Get dataset summary from the model"""
        return self.model.get_summary()

    def run_forecast(self):
        """
        Run ML forecast on the sales data.
        Placeholder for now — later will use ARIMA/Prophet/etc.
        """
        # For now, just return the cleaned data
        if self.model.df is None:
            self.model.load_data()
        return self.model.df
