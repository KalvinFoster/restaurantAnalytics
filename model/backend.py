import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
class SalesModel:

    # initialize objects
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    # Loading csv into data fram
    def load_data(self):
        self.df = pd.read_csv(self.csv_path)
        self.clean_data()
        return self.df

    #Function to clean the data
    def clean_data(self):
        # Convert Date column to datetime
        if 'Data' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        # Removing leading / trailing spaces in column names
        self.df.columns = [col.strip() for col in self.df.columns]

        # Handle missing values
        self.df.fillna({
            'Price': 0,
            'Quantity': 0,
            'Purchase Type': 'Unknown',
            'Payment Method': 'Unknown',
            'Manager': 'Unknown',
            'City': 'Unknown'
        }, inplace=True)

    def get_summary(self):
        return self.df.describe(include='all')

    def arima_forecast(self, periods=3):
        """Fit ARIMA on total monthly sales and forecast next 'periods' months."""
        if self.df is None:
            self.load_data()

        # Ensure 'Date' column is datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        # Drop rows where 'Date' could not be parsed
        self.df = self.df.dropna(subset=['Date'])

        # Calculate total sales
        self.df['Total'] = self.df['Price'] * self.df['Quantity']

        # Aggregate sales monthly
        monthly_sales = self.df.set_index('Date').resample('M')['Total'].sum()

        # Fit ARIMA model (simple order, can be tuned)
        model = ARIMA(monthly_sales, order=(1, 1, 1))
        model_fit = model.fit()

        # Forecast next `periods` months
        forecast = model_fit.forecast(steps=periods)

        return forecast


