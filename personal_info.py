#Name:Nagaraj Chitapur
#Project: Personal Information Manager
#Description:This program stores personal details,takes user input,
#validates it,and displays formatted information.

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information

# Stores your name as a string
name = "Nagaraj chitapur"

# Stores your name as a integer
age = 22

# Stores your name as a string
city = "Ilkal"

# Stores your hobby as a string
hobby = "Coding"

# Step 3: Get User Input

favorite_food = input("What's your favorite food? ")
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("        PERSONAL INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years {age_in_months} months")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()
# Step 6: Goodbye Message
# -----------------------------
print("\n" + "=" * 40)
print(" Thank you for using the program! ")
print(" Goodbye 👋")
print("=" * 40)
