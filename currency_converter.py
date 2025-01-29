import tkinter as tk
from tkinter import ttk, messagebox
import requests
import flag

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Rupee Currency Converter")
        self.root.geometry("500x450")
        self.root.configure(bg='#f0f0f0')
        
        # API endpoint for exchange rates
        self.api_url = "https://api.exchangerate-api.com/v4/latest/INR"
        
        # Fetch and store exchange rates
        self.exchange_rates = self.get_exchange_rates()
        
        # Create UI components
        self.create_ui()
    
    def get_exchange_rates(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            return data['rates']
        except requests.RequestException:
            messagebox.showerror("Error", "Unable to fetch exchange rates")
            return {}
    
    def create_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Currency Converter", 
                                font=("Helvetica", 16, "bold"), 
                                bg='#f0f0f0', fg='#333')
        title_label.pack(pady=10)
        
        # Amount input frame
        amount_frame = tk.Frame(main_frame, bg='#f0f0f0')
        amount_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(amount_frame, text="Amount (₹):", bg='#f0f0f0').pack(side=tk.LEFT)
        self.amount_entry = tk.Entry(amount_frame, width=20, font=('Arial', 12))
        self.amount_entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
        
        # Currency selection frame
        currency_frame = tk.Frame(main_frame, bg='#f0f0f0')
        currency_frame.pack(fill=tk.X, pady=10)
        
        # From Currency
        from_label = tk.Label(currency_frame, text="From Currency:", bg='#f0f0f0')
        from_label.pack(side=tk.LEFT)
        self.from_currency = ttk.Combobox(currency_frame, 
                                          values=list(self.exchange_rates.keys()), 
                                          width=20)
        self.from_currency.pack(side=tk.RIGHT, expand=True, fill=tk.X)
        self.from_currency.set("INR")
        
        # To Currency
        to_frame = tk.Frame(main_frame, bg='#f0f0f0')
        to_frame.pack(fill=tk.X, pady=10)
        
        to_label = tk.Label(to_frame, text="To Currency:", bg='#f0f0f0')
        to_label.pack(side=tk.LEFT)
        self.to_currency = ttk.Combobox(to_frame, 
                                        values=list(self.exchange_rates.keys()), 
                                        width=20)
        self.to_currency.pack(side=tk.RIGHT, expand=True, fill=tk.X)
        self.to_currency.set("USD")
        
        # Convert Button
        convert_btn = tk.Button(main_frame, text="Convert", 
                                command=self.convert_currency,
                                bg='#4CAF50', fg='white', 
                                font=('Arial', 12, 'bold'))
        convert_btn.pack(pady=10)
        
        # Result Label
        self.result_label = tk.Label(main_frame, text="", 
                                     font=("Arial", 14), 
                                     bg='#f0f0f0', fg='#333')
        self.result_label.pack(pady=10)
    
    def convert_currency(self):
        try:
            # Get input values
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            # Convert using INR as base
            inr_amount = amount / self.exchange_rates[from_curr]
            converted_amount = inr_amount * self.exchange_rates[to_curr]
            
            # Display result
            result_text = f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}"
            self.result_label.config(text=result_text)
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        except KeyError:
            messagebox.showerror("Error", "Please select valid currencies")

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()