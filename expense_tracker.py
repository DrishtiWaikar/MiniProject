import tkinter as tk 
from tkinter import messagebox
import csv
from datetime import datetime
# Function to add an expense or savings     

def add_transaction():
    amount = float(amount_entry.get())
    description = description_entry.get()
    category = categroy_var.get()

    if amount <=0:
        messagebox.showwarning("Invalid Amount!!", "Please enter a valid amount!" )
        return 
    transactions.append({"amount":amount,"description":description, "category":category})
    update_transaction_list()
    clear_entries()
    # Save data to CSV file
    with open('transactions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount, description, category])

# Function to update an existing transaction
def update_transaction():
    selected_index = transaction_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("No Transaction Selected", "Please select a transaction to update.")
        return

    index = selected_index[0]
    amount_input = amount_entry.get()
    description = description_entry.get()
    category = categroy_var.get()

    if not amount_input:
        messagebox.showwarning("Missing Amount", "Please enter the updated amount.")
        return

    try:
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
    except ValueError:
        messagebox.showwarning("Invalid Amount", "Please enter a valid positive number for the amount.")
        return

    transactions[index]["amount"] = amount
    transactions[index]["description"] = description
    transactions[index]["category"] = category
    update_transaction_list()
    clear_entries()
    # Save updated data to CSV file
    with open('transactions.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for transaction in transactions:
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), transaction['amount'], transaction['description'], transaction['category']])


# Function to delete a transaction 

def delete_transaction():
    selected_index = transaction_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("No Transaction Selected", "Please select a transaction to delete.")
        return 
    index = selected_index[0]
    del transactions[index]
    update_transaction_list()
 # Save updated data to CSV file
    with open('transactions.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for transaction in transactions:
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), transaction['amount'], transaction['description'], transaction['category']])

# Function to clear entry fields 

def clear_entries():
    amount_entry.delete(0,tk.END)
    description_entry.delete(0, tk.END)

#Function to update the transaction list in the listbox 
def update_transaction_list():
    transaction_listbox.delete(0, tk.END)
    for transaction in transactions: 
        transaction_listbox.insert(tk.END, f"{transaction['category']}: {transaction['amount']} - {transaction['description']}")

#Main Function

if __name__ == "__main__":
    transactions = []

    root = tk.Tk()
    root.title("My Expense Tracker App")

    #Labels
    amount_label = tk.Label(root, text="Amount:")
    amount_label.grid(row=0, column=0, padx=5, pady=5)
    description_label = tk.Label(root, text="Description:")
    description_label.grid(row=1, column=0,padx=5, pady=5 )
    category_label = tk.Label(root, text="Category: ")
    category_label.grid(row=2, column=0, padx=5, pady=5)
    #Entry Fields 
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)
    description_entry = tk.Entry(root)
    description_entry.grid(row=1, column=1, padx=5, pady=5)
    #Category Dropdown 
    categroy_var = tk.StringVar(root)
    categroy_var.set("Expense") #Defalut Value
    category_dropdown = tk.OptionMenu(root, categroy_var, "Expense", "Savings")
    category_dropdown.grid(row=2, column=1, padx=5, pady=5)
    #Buttons 
    add_button = tk.Button(root, text="Add Transaction", command=add_transaction)
    add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    update_button = tk.Button(root, text="Update Transaction", command=update_transaction)
    update_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    delete_button = tk.Button(root, text="Delete Transaction", command=delete_transaction)
    delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    
#ListBox to display transactions 
transaction_listbox = tk.Listbox(root, width=50)
transaction_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
update_transaction_list()

root.mainloop()
