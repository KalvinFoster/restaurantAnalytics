# main.py
import tkinter as tk
from controller.app_controller import SalesController
from view.gui import SalesView

if __name__ == "__main__":
    CSV_PATH = "data/Sales-Data-Analysis.csv"

    root = tk.Tk()
    controller = SalesController(CSV_PATH)
    SalesView(root, controller)
    root.mainloop()







