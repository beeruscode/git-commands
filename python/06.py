# ==============================================================================
# LESSON 6: DEEP DIVE - VARIABLES (MEMORY & SCOPE), FILES & OOP
# ==============================================================================

import json
import os

# ==============================================================================
# PART 1: VARIABLES IN DEPTH (MEMORY, MUTABILITY, AND SCOPE)
# ==============================================================================
print("=== PART 1: VARIABLES & MEMORY MODEL ===")

# A. Reference vs Value & Object Identity (id())
# In Python, variables do NOT hold the data directly; they are pointers/references
# to objects in memory.
x = [1, 2, 3]
y = x          # y points to the EXACT SAME memory location as x
z = [1, 2, 3]  # z points to a NEW list with identical values

print("x memory address:", id(x))
print("y memory address:", id(y))
print("z memory address:", id(z))

# '==' checks if values are equal. 'is' checks if they are the exact same object!
print("x == z (Values match?):", x == z)  # True
print("x is z (Same object?):", x is z)    # False
print("x is y (Same object?):", x is y)    # True

# B. The Mutability Trap (Aliasing)
# Since y refers to the same list as x, mutating y ALSO modifies x!
y.append(4)
print("Modified y, now x is:", x)  # [1, 2, 3, 4]

# To make an independent copy:
independent_copy = x.copy()
independent_copy.append(99)
print("After copying, original x remains:", x)

# C. Variable Scope: The LEGB Rule (Local, Enclosing, Global, Built-in)
app_version = "1.0.0"  # Global variable

def update_version():
    global app_version  # Must declare 'global' to reassign a global variable inside a function
    app_version = "2.0.0"

update_version()
print("Updated Global App Version:", app_version)


# ==============================================================================
# PART 2: FILE HANDLING (READ, WRITE, APPEND & JSON)
# ==============================================================================
print("\n=== PART 2: FILE HANDLING ===")

file_path = "sample_notes.txt"
json_path = "data_store.json"

# A. Writing to a file using Context Manager ('with')
# 'with' ensures the file is automatically closed, even if an error occurs.
# Mode 'w' overwrites or creates the file.
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Line 1: Python Masterclass\n")
    f.write("Line 2: File Handling is Essential\n")

# B. Appending to a file ('a' mode)
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended without overwriting!\n")

# C. Reading from a file ('r' mode)
# Memory-efficient way: iterate directly over the file object
print("Reading file line-by-line:")
with open(file_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"  [{line_num}] {line.strip()}")

# D. Working with Structured Data (JSON: JavaScript Object Notation)
# JSON is the universal format for configs, databases, and web APIs.
server_config = {
    "host": "127.0.0.1",
    "port": 8080,
    "debug": True,
    "allowed_users": ["Alice", "Bob", "Charlie"]
}

# Writing JSON to file
with open(json_path, "w", encoding="utf-8") as jf:
    json.dump(server_config, jf, indent=4)
print("\nJSON configuration saved successfully.")

# Reading JSON back into a Python dictionary
with open(json_path, "r", encoding="utf-8") as jf:
    loaded_config = json.load(jf)
print("Loaded Port from JSON:", loaded_config["port"])


# ==============================================================================
# PART 3: OBJECT-ORIENTED PROGRAMMING (OOP) IN DEPTH
# ==============================================================================
print("\n=== PART 3: OBJECT-ORIENTED PROGRAMMING (OOP) ===")

# --- 1. Encapsulation & The 4 Pillars ---
class BankAccount:
    """
    Base class demonstrating:
    - Encapsulation: Protecting data with private attributes (__balance).
    - Class Attributes vs Instance Attributes.
    - Dunder (Magic) methods: __str__, __repr__, __add__.
    """
    # Class Attribute: Shared across all instances of BankAccount
    bank_name = "Global Apex Bank"
    total_accounts_created = 0

    def __init__(self, owner: str, starting_balance: float = 0.0):
        # Instance Attributes: Unique to each individual account
        self.owner = owner
        # Double underscore '__' makes the attribute private (Encapsulation)
        self.__balance = float(starting_balance)
        BankAccount.total_accounts_created += 1

    # Getter property: Read-only access to private __balance
    @property
    def balance(self) -> float:
        return self.__balance

    # Controlled method to deposit
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.__balance += amount
        print(f"[Deposit] +${amount:.2f} to {self.owner}'s account. New Balance: ${self.__balance:.2f}")

    # Controlled method to withdraw
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.__balance:
            print(f"[Declined] Insufficient funds for {self.owner}. Balance: ${self.__balance:.2f}")
            return False
        self.__balance -= amount
        print(f"[Withdraw] -${amount:.2f} from {self.owner}'s account. Remaining: ${self.__balance:.2f}")
        return True

    # Polymorphic method: Subclasses can customize this
    def calculate_monthly_fee(self) -> float:
        return 5.0  # Standard maintenance fee

    # Dunder Method: User-friendly string representation (used by print(obj))
    def __str__(self):
        return f"BankAccount(Owner: {self.owner}, Balance: ${self.__balance:.2f})"

    # Dunder Method: Combining two accounts using the '+' operator!
    def __add__(self, other):
        if isinstance(other, BankAccount):
            combined_owner = f"{self.owner} & {other.owner}"
            combined_balance = self.balance + other.balance
            return BankAccount(combined_owner, combined_balance)
        raise TypeError("Can only combine with another BankAccount!")


# --- 2. Inheritance & Polymorphism ---
class SavingsAccount(BankAccount):
    """
    Subclass inheriting from BankAccount.
    Demonstrates:
    - Inheritance: Inherits all methods and properties from BankAccount.
    - super(): Calling the parent constructor.
    - Polymorphism: Overriding parent methods with customized behavior.
    """
    def __init__(self, owner: str, starting_balance: float = 0.0, interest_rate: float = 0.03):
        # Call parent constructor
        super().__init__(owner, starting_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"[Interest Applied] Added ${interest:.2f} interest.")

    # Overriding the parent's fee method (Polymorphism)
    def calculate_monthly_fee(self) -> float:
        # Savings accounts have NO monthly fee if balance > 500
        if self.balance >= 500:
            return 0.0
        return 2.5


# ==============================================================================
# PART 4: TESTING OOP & REAL-WORLD WORKFLOW
# ==============================================================================
print("\n--- Testing Accounts & Encapsulation ---")
acc1 = BankAccount("Alice", 1000)
acc2 = SavingsAccount("Bob", 600, interest_rate=0.05)

acc1.deposit(250)
acc1.withdraw(100)

# Polymorphism in action: calling the same method on different classes
accounts = [acc1, acc2]
for acc in accounts:
    fee = acc.calculate_monthly_fee()
    print(f"{acc.owner}'s account ({type(acc).__name__}) Monthly Fee: ${fee:.2f}")

acc2.apply_interest()

# Testing Operator Overloading (__add__)
joint_account = acc1 + acc2
print("\nCombined Joint Account created via '+' operator:")
print(joint_account)


# ==============================================================================
# CLEANUP (Optional: Remove temporary demo files)
# ==============================================================================
for temp_file in [file_path, json_path]:
    if os.path.exists(temp_file):
        os.remove(temp_file)
print("\nCleaned up temporary demo files.")
