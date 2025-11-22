print("Welcome to my Python program!")

# Ask the user for today's study hours
hours = input("How many hours did you study today? ")

# Convert input to float with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()  # stops the program if input is invalid

# Calculate estimated weekly study hours
weekly_hours = hours * 7

# Display the result clearly
print(f"You are on track to study {weekly_hours} hours this week.")
