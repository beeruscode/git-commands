# ==============================================================================
# LESSON 5: COMPREHENSIONS, ENUMERATE, ZIP, MAP/FILTER, EXCEPTIONS, & MODULES
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. COMPREHENSIONS (Concise, fast, Pythonic ways to build collections)
# ------------------------------------------------------------------------------
print("--- 1. Comprehensions ---")

numbers = [1, 2, 3, 4, 5, 6]

# A. List Comprehension: [expression for item in iterable if condition]
squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
# With if-else (ternary): ["Even" if n % 2 == 0 else "Odd" for n in numbers]
labeled = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print("Squares:", squares)
print("Evens only:", evens)
print("Labeled:", labeled)

# B. Dictionary Comprehension: {key_expr: value_expr for item in iterable}
names = ["alice", "bob", "charlie"]
name_lengths = {name.title(): len(name) for name in names}
print("Dictionary Comprehension:", name_lengths)

# Updating prices by 10%
prices = {"apple": 1.00, "banana": 0.50, "orange": 1.20}
inflated_prices = {item: round(price * 1.10, 2) for item, price in prices.items()}
print("Updated Prices:", inflated_prices)

# C. Set Comprehension: {expression for item in iterable} (auto-deduplicates)
raw_emails = ["Alex@Dev.com", "ALEX@DEV.COM", "sam@work.org", "Sam@Work.org "]
clean_emails = {email.strip().lower() for email in raw_emails}
print("Clean Unique Emails (Set):", clean_emails)


# ------------------------------------------------------------------------------
# 2. ENUMERATE (Loop with an Index Counter)
# Avoids manual index counting like: i = 0; i += 1
# ------------------------------------------------------------------------------
print("\n--- 2. enumerate() ---")
languages = ["Python", "JavaScript", "Rust", "Go"]

# enumerate(iterable, start=0)
for rank, lang in enumerate(languages, start=1):
    print(f"Rank #{rank}: {lang}")


# ------------------------------------------------------------------------------
# 3. ZIP (Pairing Multiple Iterables Together)
# ------------------------------------------------------------------------------
print("\n--- 3. zip() ---")
students = ["Emma", "Liam", "Noah"]
math_grades = [94, 88, 79]
science_grades = [90, 92, 85]

# A. Looping over multiple lists in parallel
for student, math, science in zip(students, math_grades, science_grades):
    print(f"{student} -> Math: {math}, Science: {science}")

# B. Instant Dictionary Creation from two lists
student_math_dict = dict(zip(students, math_grades))
print("Dict created via zip():", student_math_dict)

# C. Unzipping paired data using the * operator
pairs = [("A", 1), ("B", 2), ("C", 3)]
letters, digits = zip(*pairs)
print("Unzipped letters:", letters)
print("Unzipped digits:", digits)


# ------------------------------------------------------------------------------
# 4. MAP & FILTER (Functional Programming in Python)
# ------------------------------------------------------------------------------
print("\n--- 4. map() and filter() ---")
raw_numbers = ["10", "25", "50", "100"]

# map(function, iterable) applies a function to every item
converted_nums = list(map(int, raw_numbers))
print("Mapped to int:", converted_nums)

# filter(function, iterable) keeps items where function returns True
high_values = list(filter(lambda x: x >= 50, converted_nums))
print("Filtered (>= 50):", high_values)

# Note: In modern Python, List Comprehensions are usually preferred over map/filter
# e.g., [int(x) for x in raw_numbers] and [x for x in converted_nums if x >= 50]


# ------------------------------------------------------------------------------
# 5. EXCEPTION HANDLING (try, except, else, finally, raise)
# Prevents your program from crashing when an error happens.
# ------------------------------------------------------------------------------
print("\n--- 5. Exception Handling ---")

def divide_safely(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero!")
        return None
    except TypeError as e:
        print(f"Type Error: {e}")
        return None
    else:
        # Runs ONLY if NO exception was raised in the try block
        print(f"Calculation successful: {a} / {b} = {result}")
        return result
    finally:
        # ALWAYS runs, no matter what (used for cleanup / closing files)
        print("-> End of division attempt.")

divide_safely(10, 2)
divide_safely(10, 0)

# Raising exceptions deliberately:
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Age set to {age}"

try:
    print(set_age(-5))
except ValueError as err:
    print("Caught custom validation error:", err)


# ------------------------------------------------------------------------------
# 6. MODULES & IMPORTS
# Reusing code from Python's standard library or other files.
# ------------------------------------------------------------------------------
print("\n--- 6. Modules and Imports ---")

# A. Standard module import
import math
print("Square root of 64:", math.sqrt(64))
print("Pi constant:", round(math.pi, 4))

# B. Importing specific functions
from datetime import date
print("Today's date:", date.today())

# C. Importing with an alias (as)
import random as rnd
print("Random number (1-100):", rnd.randint(1, 100))
coin_toss = rnd.choice(["Heads", "Tails"])
print("Coin flip:", coin_toss)


# ------------------------------------------------------------------------------
# 7. REAL-WORLD DATA CLEANING PIPELINE (COMBINING EVERYTHING)
# ------------------------------------------------------------------------------
print("\n--- 7. Real-World Pipeline ---")
raw_data = [
    {"user": " alice ", "age": "24", "score": "88"},
    {"user": "BOB",     "age": "invalid", "score": "95"},
    {"user": "charlie", "age": "30", "score": "42"}
]

clean_records = []
for entry in raw_data:
    try:
        clean_user = entry["user"].strip().title()
        clean_age = int(entry["age"])
        clean_score = int(entry["score"])
        clean_records.append({"user": clean_user, "age": clean_age, "score": clean_score})
    except ValueError:
        print(f"Skipping corrupted record for {entry['user'].strip()}")

# Using List Comprehension to filter top scorers (score >= 70)
top_performers = [record["user"] for record in clean_records if record["score"] >= 70]
print("Valid processed records:", clean_records)
print("Top performers:", top_performers)


# ------------------------------------------------------------------------------
# 8. THE __name__ == '__main__' IDIOM
# Ensures code inside this block only runs when executed directly,
# not when imported as a module into another file.
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("\nLesson 5 executed directly as main script!")
