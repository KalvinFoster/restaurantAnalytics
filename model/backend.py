import pandas as pd

class SalesModel:

    # initialize objects
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    # Loading csv into data fram
    def load_csv(self):
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



