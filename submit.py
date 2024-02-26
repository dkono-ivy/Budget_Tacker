def submit_expense(name, amount):
    errors = validate_expense(name, amount)
    if errors:
        messagebox.showerror("Validation Error", "\n".join(errors))
    else:
        add_expense(name, float(amount))
        messagebox.showinfo("Success", "Expense added successfully.")
