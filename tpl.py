import tkinter as tk
from tkinter import ttk
import requests
import json

# Function to fetch the list of available currencies
def fetch_currency_list():
    api_key = 'b23c9ce19e3d44c084756137feec014c'
    url = f'https://openexchangerates.org/api/currencies.json?app_id={api_key}'
    response = requests.get(url)
    currency_list = json.loads(response.text)
    return currency_list

# Function to perform currency conversion using the Open Exchange Rates API
def convert_currency():
    # Get user inputs
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()

    api_key = 'b23c9ce19e3d44c084756137feec014c'
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
    response = requests.get(url)
    rates = json.loads(response.text)['rates']

    # Calculate the conversion using fetched exchange rates
    from_rate = rates[from_currency]
    to_rate = rates[to_currency]
    converted_amount = (amount / from_rate) * to_rate

    # Update the result label with the converted amount
    result_label.config(text=f'Converted Amount: {converted_amount:.2f} {to_currency}')

# Function to reset the user inputs and result label
def reset():
    amount_entry.delete(0, tk.END)
    from_currency_combobox.set('')
    to_currency_combobox.set('')
    result_label.config(text='')

# Fetch currency list
currencies = fetch_currency_list()

# Create GUI
root = tk.Tk()
root.title('Bcs201028 Currency Converter')

# Create style for the interface
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), padding=50)
style.configure('TEntry', font=('Arial', 12), padding=10)
style.configure('TButton', font=('Arial', 12), padding=10)

# Create amount input UI
amount_label = ttk.Label(root, text='Amount:')
amount_label.grid(column=0, row=0, padx=10, pady=10)
amount_entry = ttk.Entry(root)
amount_entry.grid(column=1, row=0)

# Create from currency dropdown UI
from_currency_label = ttk.Label(root, text='From Currency:')
from_currency_label.grid(column=0, row=1, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=list(currencies.keys()))
from_currency_combobox.grid(column=1, row=1)

# Create to currency dropdown UI
to_currency_label = ttk.Label(root, text='To Currency:')
to_currency_label.grid(column=0, row=2, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=list(currencies.keys()))
to_currency_combobox.grid(column=1, row=2)

# Create Convert button UI
convert_button = ttk.Button(root, text='Convert', command=convert_currency)
convert_button.grid(column=0, row=3, padx=10, pady=10, columnspan=2)

# Create Result label UI
result_label = ttk.Label(root, text='')
result_label.grid(column=0, row=4, columnspan=2)

# Create Reset button UI
reset_button = ttk.Button(root, text='Reset', command=reset)
reset_button.grid(column=0, row=5, padx=10, pady=10, columnspan=2)


root.mainloop()
