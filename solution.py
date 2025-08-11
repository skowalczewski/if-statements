"""
Python If Statements - Solution
===============================

This is the complete solution for the voting age exercise.
This demonstrates the proper implementation with error handling.
"""

try:
    # Prompt user for their age
    age = int(input("Enter your age: "))
    
    # Check if user is old enough to vote
    if age >= 18:
        print("You can vote!")
    else:
        print("Too young to vote.")
        
except ValueError:
    print("Please enter a valid number for your age.")
except Exception as e:
    print(f"An error occurred: {e}")