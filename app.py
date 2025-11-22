# ----------------------------------------
# Study Time Tracker Program
# ----------------------------------------
# This program asks how many hours you studied today,
# converts the input into a number, estimates weekly
# study hours, and displays the result.
# Includes basic error handling to prevent crashes.
# ----------------------------------------

print("Welcome to my Python program!")  # Welcome message

# Prompt the user for today's study hours
hours = input("How many hours did you study today? ")

# Convert input to float with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()  # Stop program if input is invalid

# Calculate estimated weekly study hours
weekly_hours = hours * 7

# Display results
print(f"You are on track to study {weekly_hours} hours this week.")
