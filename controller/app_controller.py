# controller/sales_controller.py
from PIL._tkinter_finder import tk

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
        return self.model.arima_forecast()
