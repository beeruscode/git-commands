# ==========================================
# LESSON 2: LOOPS & RANGE IN PYTHON
# ==========================================

# ------------------------------------------
# 1. THE range() FUNCTION
# range(start, stop, step) generates a sequence of numbers.
# Rule: It stops BEFORE the "stop" number!
# ------------------------------------------
print("--- 1. Understanding range() ---")

# A. range(stop) -> starts at 0, counts up to (stop - 1)
print("range(5):", list(range(5)))  # [0, 1, 2, 3, 4]

# B. range(start, stop) -> starts at start, stops before stop
print("range(2, 7):", list(range(2, 7)))  # [2, 3, 4, 5, 6]

# C. range(start, stop, step) -> counts with custom intervals
print("range(0, 10, 2):", list(range(0, 10, 2)))  # [0, 2, 4, 6, 8] (even numbers)

# D. Counting backwards using negative step
print("range(5, 0, -1):", list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]


# ------------------------------------------
# 2. FOR LOOP
# Used when you know how many times to repeat,
# or when looping through items in a collection.
# ------------------------------------------
print("\n--- 2. for Loop with range() ---")
for i in range(1, 4):
    print(f"Count: {i}")

print("\n--- 2B. for Loop over a List ---")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n--- 2C. for Loop over a String ---")
for char in "Code":
    print(f"Letter: {char}")

print("\n--- 2D. enumerate() -> Get index AND value ---")
heroes = ["Spider-Man", "Batman", "Iron Man"]
for index, hero in enumerate(heroes, start=1):
    print(f"Rank #{index}: {hero}")


# ------------------------------------------
# 3. WHILE LOOP
# Repeats AS LONG AS a condition remains True.
# Great when you don't know ahead of time when it stops.
# ------------------------------------------
print("\n--- 3. while Loop (Countdown) ---")
countdown = 3

while countdown > 0:
    print(f"T-minus: {countdown}...")
    countdown -= 1  # IMPORTANT: Always update condition to avoid infinite loop!

print("Blast off! (Rocket Launched)")


# ------------------------------------------
# 4. LOOP CONTROL: break & continue
# ------------------------------------------
print("\n--- 4A. 'continue' skips to the next iteration ---")
for num in range(1, 6):
    if num == 3:
        print("Skipping 3!")
        continue
    print(f"Number: {num}")

print("\n--- 4B. 'break' stops and exits the loop immediately ---")
for num in range(1, 10):
    if num == 5:
        print("Found 5! Stopping loop.")
        break
    print(f"Searching... currently at {num}")


# ------------------------------------------
# 5. LOOP WITH 'else'
# In Python, a loop can have an 'else' block!
# It runs ONLY if the loop finishes normally without hitting a 'break'.
# ------------------------------------------
print("\n--- 5. for-else search ---")
target = 7
numbers = [1, 3, 5, 9]

for n in numbers:
    if n == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} is not in the list.")


# ------------------------------------------
# 6. WHAT CAN WE DO WITH LOOPS? (PRACTICAL EXAMPLES)
# ------------------------------------------
print("\n--- 6A. Accumulator (Summing numbers) ---")
total_sum = 0
for n in range(1, 11):  # Numbers 1 through 10
    total_sum += n
print(f"Sum of 1 through 10 = {total_sum}")

print("\n--- 6B. Filtering data ---")
scores = [45, 88, 92, 59, 74, 100]
passing_scores = []
for s in scores:
    if s >= 70:
        passing_scores.append(s)
print(f"Passing scores: {passing_scores}")

print("\n--- 6C. Nested Loops (e.g., Simple Grid or Multiplication) ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:2}", end=" ")
    print()  # Newline after each row
