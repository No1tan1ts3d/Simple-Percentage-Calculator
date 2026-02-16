import tkinter as tk
from tkinter import ttk

class PercentageCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Percentage Calculator")
        self.geometry("320x450")
        self.resizable(False, False)
        
        # Main container with padding
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input Section
        ttk.Label(main_frame, text="Enter Amount (N):", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        
        # Trace variable to automatically trigger calculation on typing
        self.amount_var = tk.StringVar()
        self.amount_var.trace_add("write", self.calculate)
        
        entry = ttk.Entry(main_frame, textvariable=self.amount_var, font=("Segoe UI", 12))
        entry.pack(fill=tk.X, pady=(0, 15))
        entry.focus() # Auto-focus the input field
        
        # Separator line
        ttk.Separator(main_frame, orient='horizontal').pack(fill=tk.X, pady=(0, 10))
        
        # Results Section
        self.results_frame = ttk.Frame(main_frame)
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Generate the labels for 0.2% to 1.5%
        self.result_labels = []
        for i in range(2, 16):
            pct = i / 10.0
            lbl = ttk.Label(self.results_frame, text=f"Add sum with {pct:.1f}% = 0.00", font=("Segoe UI", 10))
            lbl.pack(anchor=tk.W, pady=2)
            self.result_labels.append((pct, lbl))
            
    def calculate(self, *args):
        try:
            val_str = self.amount_var.get().strip()
            # Handle empty input gracefully
            if not val_str:
                n = 0.0
            else:
                n = float(val_str)
                
            # Update all labels with the calculated formulas
            for pct, lbl in self.result_labels:
                result = n + (n * (pct / 100.0))
                lbl.config(text=f"Add sum with {pct:.1f}% = {result:.2f}")
                
        except ValueError:
            # Handle non-numeric text typed by the user
            for pct, lbl in self.result_labels:
                lbl.config(text=f"Add sum with {pct:.1f}% = Invalid Input")

if __name__ == "__main__":
    app = PercentageCalculator()
    app.mainloop()