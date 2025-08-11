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

# Example 10: Working with user input
print("10. User Input Examples")
print("Here are examples of how input() works with if statements:")
print()

# Example 10a: Basic input() usage
print("Example A: Reading user input")
print("Code: name = input('Enter your name: ')")
print("      if name:")
print("          print(f'Hello, {name}!')")
print("      else:")
print("          print('You didn't enter a name!')")
print()

# Example 10b: Converting input to integer
print("Example B: Converting input to integer")
print("Code: age_str = input('Enter your age: ')")
print("      age = int(age_str)")
print("      if age >= 18:")
print("          print('You can vote!')")
print("      else:")
print("          print('Too young to vote.')")
print()

# Example 10c: Input validation
print("Example C: Input validation with try-except")
print("Code: try:")
print("          age = int(input('Enter your age: '))")
print("          if age >= 18:")
print("              print('You can vote!')")
print("          else:")
print("              print('Too young to vote.')")
print("      except ValueError:")
print("          print('Please enter a valid number!')")
print()

# Example 10d: Multiple input conditions
print("Example D: Multiple input conditions")
print("Code: favorite_color = input('Enter your favorite color: ').lower()")
print("      if favorite_color == 'red' or favorite_color == 'blue':")
print("          print('Great choice! That's a primary color.')")
print("      elif favorite_color == 'green':")
print("          print('Nice! Green is the color of nature.')")
print("      else:")
print("          print('That's an interesting color choice!')")
print()

print("=== End of Demo ===")
