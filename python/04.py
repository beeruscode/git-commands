# ==========================================================
# LESSON 4: DATA STRUCTURES, INDEXING, SLICING & METHODS
# ==========================================================

# ----------------------------------------------------------
# 1. INDEXING & SLICING (APPLIES TO LISTS, TUPLES & STRINGS)
# Syntax: sequence[start : stop : step]
# Remember: Python uses 0-based indexing! Stop is EXCLUSIVE.
# ----------------------------------------------------------
print("--- 1. Indexing & Slicing ---")
letters = ["A", "B", "C", "D", "E", "F"]

# Positive Indexing: 0 -> First, 1 -> Second
print("First item (index 0):", letters[0])
print("Third item (index 2):", letters[2])

# Negative Indexing: -1 -> Last, -2 -> Second-to-last
print("Last item (index -1):", letters[-1])
print("Second to last (index -2):", letters[-2])

# Slicing: [start:stop]
print("Slice [1:4] (indices 1, 2, 3):", letters[1:4])  # ['B', 'C', 'D']
print("First 3 items [:3]:", letters[:3])             # ['A', 'B', 'C']
print("From index 3 to end [3:]:", letters[3:])        # ['D', 'E', 'F']

# Step: [start:stop:step]
print("Every 2nd item [::2]:", letters[::2])          # ['A', 'C', 'E']

# Reverse trick using step -1
print("Reversed list [::-1]:", letters[::-1])         # ['F', 'E', 'D', 'C', 'B', 'A']


# ----------------------------------------------------------
# 2. LISTS (Ordered, Mutable/Changeable, Allows Duplicates)
# Best for: Collections of items that change over time
# ----------------------------------------------------------
print("\n--- 2. List Methods ---")
tasks = ["code", "eat", "sleep"]

# Adding items
tasks.append("exercise")           # Adds to end
tasks.insert(1, "read book")       # Inserts at specific index
print("After adding:", tasks)

# Removing items
tasks.remove("eat")                # Removes by value
removed_item = tasks.pop()         # Removes & returns last item
print(f"Removed '{removed_item}', Current tasks:", tasks)

# Sorting & Reversing
numbers = [42, 7, 19, 3, 99]
numbers.sort()                     # Sorts in-place (ascending)
print("Sorted numbers:", numbers)
numbers.reverse()                  # Reverses in-place
print("Reversed numbers:", numbers)


# ----------------------------------------------------------
# 3. TUPLES (Ordered, Immutable/Unchangeable)
# Best for: Fixed data that should never be altered
# ----------------------------------------------------------
print("\n--- 3. Tuples & Unpacking ---")
# Defined with parentheses ()
point_3d = (10, 20, 30)

print("Coordinates:", point_3d)
print("X value (index 0):", point_3d[0])

# Tuples cannot be modified! (e.g., point_3d[0] = 15 would raise TypeError)

# Tuple Unpacking: Assign items to multiple variables in one go!
x, y, z = point_3d
print(f"Unpacked -> x: {x}, y: {y}, z: {z}")

# Methods: count() and index()
print("Count of 20:", point_3d.count(20))
print("Index of 30:", point_3d.index(30))


# ----------------------------------------------------------
# 4. SETS (Unordered, Mutable, NO DUPLICATES ALLOWED)
# Best for: Unique items, mathematical unions & intersections
# ----------------------------------------------------------
print("\n--- 4. Sets & Set Operations ---")
# Defined with curly braces {} without keys
skills = {"Python", "Git", "SQL", "Python"}  # Duplicate "Python" is removed!
print("Unique skills:", skills)

# Adding & Removing
skills.add("Docker")
skills.discard("SQL")  # discard() removes safely without error if not found
print("Updated skills:", skills)

# Set Mathematics
team_a = {"Alice", "Bob", "Charlie"}
team_b = {"Charlie", "David", "Eve"}

# Union: Everyone combined (|)
print("Union (All members):", team_a | team_b)

# Intersection: In BOTH sets (&)
print("Intersection (Common members):", team_a & team_b)

# Difference: In team_a but NOT in team_b (-)
print("Difference (Only in Team A):", team_a - team_b)


# ----------------------------------------------------------
# 5. DICTIONARIES (Key-Value Pairs, Fast O(1) Lookups)
# Best for: Structured records, configs, user profiles, JSON
# ----------------------------------------------------------
print("\n--- 5. Dictionary Methods ---")
# Defined with {key: value}
user = {
    "username": "alex_dev",
    "role": "admin",
    "active": True
}

# Accessing values
print("Username:", user["username"])
# Safe access with .get(key, default) -> avoids KeyError if key doesn't exist
print("Email:", user.get("email", "Not provided"))

# Modifying and adding
user["role"] = "superadmin"         # Update existing key
user["email"] = "alex@example.com"  # Add new key
print("Updated user:", user)

# Useful methods: keys(), values(), items()
print("Keys:", list(user.keys()))
print("Values:", list(user.values()))

print("Iterating over key-value pairs:")
for key, value in user.items():
    print(f"  {key}: {value}")


# ----------------------------------------------------------
# 6. REAL-WORLD COMBINATION: LIST OF DICTIONARIES
# How data looks in real apps, databases, and APIs
# ----------------------------------------------------------
print("\n--- 6. Real-World Data Structure ---")
students = [
    {"name": "Sarah", "grade": 95},
    {"name": "Liam", "grade": 82},
    {"name": "Emma", "grade": 91}
]

# Finding student with highest grade
top_student = max(students, key=lambda s: s["grade"])
print(f"Top student: {top_student['name']} with a grade of {top_student['grade']}")
