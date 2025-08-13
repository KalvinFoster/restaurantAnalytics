# view/sales_view.py
import tkinter as tk
from tkinter import ttk, scrolledtext

class SalesView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Sales Data Analysis")
        self.root.geometry("800x600")

        # Buttons
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Load Data", command=self.load_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Show Summary", command=self.show_summary).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Run Forecast", command=self.run_forecast).pack(side=tk.LEFT, padx=5)

        # Output Box
        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=30)
        self.output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def load_data(self):
        df = self.controller.load_data()
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, str(df.head()))

    def show_summary(self):
        summary = self.controller.get_summary()
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, str(summary))

    def run_forecast(self):
        forecast_df = self.controller.run_forecast()
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Forecast (placeholder):\n")
        self.output.insert(tk.END, str(forecast_df.head()))
