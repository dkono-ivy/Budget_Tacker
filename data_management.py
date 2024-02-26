# data_management.py

def add_expense(name, amount):
    """Add an expense to the storage system (e.g., database, file)."""
  
    print(f"Adding expense: {name}, Amount: {amount}")

def get_all_expenses():
    """Retrieve all expenses from the storage system."""
   
    print("Retrieving all expenses...")
    
    return [("Groceries", 150.00), ("Utilities", 90.50)]
