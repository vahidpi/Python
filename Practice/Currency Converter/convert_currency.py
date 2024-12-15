import requests
import tkinter as tk
from tkinter import ttk

api_key= "e35930682f59221bc32c0be3"

def get_exchange_rate(api_key, source_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["conversion_rate"]
    else:
        raise Exception("Failed to fetch exchange rates")
    
def get_currency_list(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["supported_codes"]
    else:
        raise Exception("Failed to fetch currency list")
    

def convert_currency(amount, rate):
    return round(amount * rate, 2)


def main():
    res=get_currency_list(api_key)
    currency_codes = [code[1] for code in res]
    print(currency_codes)


if __name__ == "__main__":
    main()

"""
def convert():
    source = source_currency.get()
    target = target_currency.get()
    amount = float(amount_entry.get())
    try:
        rate = get_exchange_rate(api_key, source, target)
        converted_amount = convert_currency(amount, rate)
        result_label.config(text=f"Converted Amount: {converted_amount} {target}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("Currency Converter")

# Source Currency
tk.Label(root, text="From:").grid(row=0, column=0)
source_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP"])
source_currency.grid(row=0, column=1)

# Target Currency
tk.Label(root, text="To:").grid(row=1, column=0)
target_currency = ttk.Combobox(root, values=["USD", "EUR", "GBP"])
target_currency.grid(row=1, column=1)

# Amount
tk.Label(root, text="Amount:").grid(row=2, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2)

# Result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
"""