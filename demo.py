"""
Python If Statements - Demonstration Code
==========================================

This file contains examples demonstrating various uses of if statements in Python.
Study these examples to understand how conditional logic works.
"""

print("=== Python If Statements Demo ===\n")

# Example 1: Basic if statement
print("1. Basic If Statement")
age = 18
if age >= 18:
    print(f"Age {age}: You are an adult!")
print()

# Example 2: If-else statement
print("2. If-Else Statement")
temperature = 75
if temperature > 80:
    print(f"Temperature {temperature}°F: It's hot outside!")
else:
    print(f"Temperature {temperature}°F: It's not too hot.")
print()

# Example 3: If-elif-else statement
print("3. If-Elif-Else Statement")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score}: Your grade is {grade}")
print()

# Example 4: Multiple conditions with 'and'
print("4. Multiple Conditions with 'and'")
username = "student"
password = "secret123"
if username == "student" and password == "secret123":
    print("Login successful!")
else:
    print("Invalid credentials!")
print()

# Example 5: Multiple conditions with 'or'
print("5. Multiple Conditions with 'or'")
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print(f"{day}: It's the weekend!")
else:
    print(f"{day}: It's a weekday.")
print()

# Example 6: Using 'not' operator
print("6. Using 'not' Operator")
is_raining = False
if not is_raining:
    print("It's not raining. Great day for a walk!")
else:
    print("It's raining. Better stay inside.")
print()

# Example 7: Nested if statements
print("7. Nested If Statements")
weather = "sunny"
temperature = 75
if weather == "sunny":
    if temperature > 70:
        print("Perfect weather for outdoor activities!")
    else:
        print("Sunny but a bit chilly.")
else:
    print("Not the best weather for outdoor activities.")
print()

# Example 8: Checking if a number is in a range
print("8. Number in Range")
number = 25
if 10 <= number <= 50:
    print(f"{number} is between 10 and 50 (inclusive)")
else:
    print(f"{number} is not between 10 and 50")
print()

# Example 9: Checking membership with 'in'
print("9. Checking Membership")
favorite_color = "blue"
primary_colors = ["red", "blue", "yellow"]
if favorite_color in primary_colors:
    print(f"{favorite_color} is a primary color!")
else:
    print(f"{favorite_color} is not a primary color.")
print()

# Example 10: Working with user input (commented out for demo)
print("10. User Input Example (commented out)")
print("# Uncomment the following lines to test with user input:")
print("# name = input('Enter your name: ')")
print("# if name:")
print("#     print(f'Hello, {name}!')")
print("# else:")
print("#     print('You didn't enter a name!')")
print()

print("=== End of Demo ===")
