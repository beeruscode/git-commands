# ==========================================
# LESSON 1: VARIABLES & DATA TYPES IN PYTHON
# ==========================================

# ------------------------------------------
# 1. WHAT IS A VARIABLE?
# A variable is a named container/box used to store data in memory.
# Syntax: variable_name = value
# ------------------------------------------
player_name = "Alex"
player_score = 100

print("--- 1. Basic Variables ---")
print("Player:", player_name)
print("Score:", player_score)


# ------------------------------------------
# 2. CORE DATA TYPES
# ------------------------------------------
# A. Integers (int): Whole numbers (positive, negative, or zero)
age = 25
temperature = -3

# B. Floats (float): Decimal / real numbers
price = 19.99
pi_value = 3.14159

# C. Strings (str): Text wrapped in single or double quotes
greeting = "Hello, World!"
language = 'Python'

# D. Booleans (bool): Either True or False (capitalized!)
is_game_over = False
has_passed = True

# E. NoneType (None): Represents the absence of a value
user_bio = None

print("\n--- 2. Checking Data Types using type() ---")
print("age:", type(age))
print("price:", type(price))
print("greeting:", type(greeting))
print("is_game_over:", type(is_game_over))
print("user_bio:", type(user_bio))


# ------------------------------------------
# 3. WHAT CAN WE DO WITH VARIABLES?
# ------------------------------------------

# A. Arithmetic Operations (Math)
x = 10
y = 3

print("\n--- 3A. Math Operations ---")
print("Addition (10 + 3):", x + y)
print("Subtraction (10 - 3):", x - y)
print("Multiplication (10 * 3):", x * y)
print("Division (10 / 3):", x / y)
print("Floor Division (10 // 3):", x // y)  # chops off decimal
print("Remainder/Modulo (10 % 3):", x % y)  # useful to check even/odd
print("Power/Exponent (10 ** 3):", x ** y)  # 10 to power 3

# B. String Manipulation
first_name = "Bruce"
last_name = "Wayne"

# Joining strings (Concatenation)
full_name = first_name + " " + last_name

# Modern way: F-Strings (Formatted Strings)
message = f"Welcome, {full_name}! Your score is {player_score}."

print("\n--- 3B. String Operations ---")
print(message)
print("Uppercase:", full_name.upper())
print("Character count:", len(full_name))

# C. Variable Updating / Reassignment
counter = 0
counter = counter + 1  # Standard update
counter += 5           # Shorthand for counter = counter + 5
print("\n--- 3C. Updated Counter ---")
print("Counter:", counter)

# D. Type Conversion (Casting)
# Changing data from one type to another
str_number = "50"
real_number = int(str_number)  # Converts string "50" to integer 50

print("\n--- 3D. Type Casting ---")
print("real_number + 10 =", real_number + 10)
print("float(10) =", float(10))
print("str(99) =", str(99))


# ------------------------------------------
# 4. COLLECTION DATA TYPES (Storing multiple items)
# ------------------------------------------
# List: Ordered, changeable list of items
inventory = ["sword", "shield", "potion"]
inventory.append("magic ring")

# Dictionary: Key-Value pairs (like a real dictionary or database entry)
user_profile = {
    "username": "coder123",
    "level": 5,
    "is_online": True
}

print("\n--- 4. Collections ---")
print("Inventory:", inventory)
print("First item in inventory:", inventory[0])
print("User profile level:", user_profile["level"])
