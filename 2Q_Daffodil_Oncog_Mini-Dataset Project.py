# ============================================
# Mini-Dataset Project: Daily Step Count
# ============================================
# Scenario:
# Track daily step counts of 3 friends (Ana, Ben, Carla)
# over 5 weekdays (Monday–Friday).
#
# Rows = friends
# Columns = days
#
# Features:
# 1. Print all data
# 2. Select friend
# 3. Update data
# 4. Summarize data (BONUS: total, average, min, max)
# 5. Exit
#
# Reflection:
# I chose step counts because it’s simple and relatable.
# A 2D array organizes the data clearly: rows = friends,
# columns = days. This makes it easy to access, update,
# and calculate totals or averages for each person.

# -----------------------------
# Step 1: Define dataset (2D array)
# -----------------------------
friends = ["Ana", "Ben", "Carla"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Each row = friend, each column = weekday
steps = [
    [5000, 6000, 5500, 5800, 6200],   # Ana
    [7000, 8000, 7500, 7200, 7700],   # Ben
    [4000, 4500, 5000, 4800, 5100]    # Carla
]

# -----------------------------
# Step 2: Helper functions
# -----------------------------

def print_all_data():
    """Prints the entire dataset in table form."""
    print("\nStep Count Table")
    print("------------------------------------------------")
    print("Friend\t\t", end="")
    for day in days:
        print(f"{day[:3]}\t", end="")  # print first 3 letters of day
    print("\n------------------------------------------------")
    for i in range(len(friends)):
        print(f"{friends[i]:10}", end="\t")
        for s in steps[i]:
            print(f"{s}\t", end="")
        print()
    print("------------------------------------------------")


def select_friend():
    """Allows user to select a friend and view their data."""
    print("\nSelect a friend:")
    for i, name in enumerate(friends):
        print(f"[{i}] {name}")
    choice = int(input("Enter choice: "))
    print(f"{friends[choice]} - {steps[choice]}")


def update_data():
    """Updates a specific value in the dataset."""
    print("\nSelect a friend to update:")
    for i, name in enumerate(friends):
        print(f"[{i}] {name}")
    friend_choice = int(input("Enter choice: "))

    print("\nSelect a day:")
    for i, day in enumerate(days):
        print(f"[{i}] {day}")
    day_choice = int(input("Enter choice: "))

    new_value = int(input("Enter new step count: "))
    steps[friend_choice][day_choice] = new_value

    print(f"Updated {friends[friend_choice]} on {days[day_choice]} to {new_value} steps.")


def summarize_data():
    """Summarizes each friend's dataset (total, average, min, max)."""
    print("\nSummary of Step Counts")
    print("------------------------------------------------")
    for i in range(len(friends)):
        total = sum(steps[i])
        avg = total / len(steps[i])
        min_val = min(steps[i])
        max_val = max(steps[i])
        print(f"{friends[i]}:")
        print(f"  Total = {total} steps")
        print(f"  Average = {avg:.1f} steps/day")
        print(f"  Min = {min_val} steps")
        print(f"  Max = {max_val} steps")
        print("------------------------------------------------")

# -----------------------------
# Step 3: Main Menu Loop
# -----------------------------
while True:
    print("\n[1] Print all data")
    print("[2] Select friend")
    print("[3] Update data")
    print("[4] Summarize data")
    print("[5] Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print_all_data()
    elif choice == "2":
        select_friend()
    elif choice == "3":
        update_data()
    elif choice == "4":
        summarize_data()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
