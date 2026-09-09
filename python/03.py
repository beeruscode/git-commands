# ==========================================================
# LESSON 3: INPUT, OUTPUT & TYPE CONVERSION IN PYTHON
# ==========================================================

import sys

# ----------------------------------------------------------
# 1. OUTPUT: THE print() FUNCTION & FORMATTING
# Output is how your program speaks to the user or screen.
# ----------------------------------------------------------
print("--- 1. Output Techniques ---")

# A. Basic printing
print("Hello, programmer!")

# B. Custom Separator ('sep')
# Controls what goes between items (default is a single space)
print("apple", "banana", "cherry", sep=", ")
print("2026", "09", "08", sep="-")  # 2026-09-08

# C. Custom End Character ('end')
# By default, print() adds a newline (\n). You can change it:
print("Loading", end="...")
print(" Done!")  # Stays on the same line

# D. Modern Output: F-Strings (Formatted Strings)
product = "Laptop"
price = 899.99
quantity = 2

# You can evaluate expressions, round numbers, and format inside { }
print(f"Product: {product} | Unit Price: ${price:.2f}")
print(f"Total: ${price * quantity:,.2f}")


# ----------------------------------------------------------
# 2. TYPE CONVERSION (CASTING)
# Converting a value from one data type to another.
# ----------------------------------------------------------
print("\n--- 2. Type Conversion (Explicit Casting) ---")

# A. String to Integer: int()
str_age = "20"
num_age = int(str_age)
print(f"num_age + 5 = {num_age + 5}")  # 25 (Math works!)

# B. String to Float: float()
str_rating = "4.8"
rating = float(str_rating)
print(f"Rating as float: {rating}")

# C. Numbers to String: str()
score = 95
score_text = "Your score is " + str(score)
print(score_text)

# D. Boolean Conversion: bool()
# In Python, empty things are False ("Truthy" vs "Falsy")
print("bool(0):", bool(0))          # False
print("bool(1):", bool(1))          # True
print("bool(''):", bool(""))        # False (empty string)
print("bool('Hello'):", bool("Hello")) # True (non-empty string)
print("bool([]):", bool([]))        # False (empty list)


# ----------------------------------------------------------
# 3. IMPLICIT CONVERSION (AUTOMATIC)
# Python automatically converts smaller types to larger types.
# ----------------------------------------------------------
print("\n--- 3. Implicit Type Conversion ---")
int_val = 10       # int
float_val = 2.5    # float
result = int_val + float_val  # int is automatically promoted to float

print(f"10 + 2.5 = {result} (Type: {type(result)})")


# ----------------------------------------------------------
# 4. INPUT: RECEIVING DATA FROM THE USER
# CRITICAL RULE: input() ALWAYS returns data as a STRING (str)!
# Even if the user types '25', Python sees it as the text '25'.
# ----------------------------------------------------------
print("\n--- 4. Input & Conversion Example ---")

# Safe input wrapper: runs interactively if run in terminal,
# or uses defaults if run in an automated non-interactive runner.
if sys.stdin.isatty():
    name = input("Enter your name: ")
    birth_year_str = input("Enter your birth year (e.g., 2000): ")
else:
    # Default values for automated/demonstration mode
    name = "Coder"
    birth_year_str = "2002"
    print(f"(Automated Demo) Input Name: {name}")
    print(f"(Automated Demo) Input Birth Year: {birth_year_str}")

# CONVERT string to integer for calculation:
birth_year = int(birth_year_str)
current_year = 2026
calculated_age = current_year - birth_year

print(f"Hello, {name}! You are approximately {calculated_age} years old.")


# ----------------------------------------------------------
# 5. DEFENSIVE PROGRAMMING (HANDLING CONVERSION ERRORS)
# What if someone enters 'abc' when you ask for a number?
# ----------------------------------------------------------
print("\n--- 5. Safe Input Validation ---")
user_entry = "42a"  # Invalid number

# Method 1: Using .isdigit()
if user_entry.isdigit():
    valid_num = int(user_entry)
    print(f"Converted successfully: {valid_num}")
else:
    print(f"Warning: '{user_entry}' is not a valid whole number!")

# Method 2: Using try-except block
user_input_float = "ten point five"
try:
    converted = float(user_input_float)
except ValueError:
    print(f"Could not convert '{user_input_float}' to a float!")


# ----------------------------------------------------------
# 6. WHAT CAN WE BUILD WITH THIS? (MINI BILL CALCULATOR)
# ----------------------------------------------------------
print("\n--- 6. Real-World Project: Tip Calculator ---")
bill_amount = 50.00
tip_percentage = 15  # 15%

tip_value = bill_amount * (tip_percentage / 100)
grand_total = bill_amount + tip_value

print(f"Subtotal:       ${bill_amount:>7.2f}")
print(f"Tip ({tip_percentage}%):       ${tip_value:>7.2f}")
print(f"Grand Total:    ${grand_total:>7.2f}")
