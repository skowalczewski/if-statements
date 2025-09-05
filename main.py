#!/usr/bin/env python3
"""
Python If Statements Exercise: Simple Grade Checker

Complete this grade checker program using only:
- Variables
- input() function  
- print() function
- if/elif/else statements
- Comparison operators (<, <=, >, >=, ==, !=)
- Logical operators (and, or, not)

No functions or loops needed - just basic programming!
"""

print("📊 Welcome to the Grade Checker! 📊")
print("Enter your numeric grade and I'll tell you the letter grade.")
print()

# Get the grade from the user
grade = float(input("Enter your numeric grade: "))

print()
print("Checking your grade...")
print()

# TODO 1: Check for invalid grades
# Use 'or' to check if grade is less than 0 OR greater than 100
# If the grade is invalid, print an error message
# Example: if grade < 0 or grade > 100:

# YOUR CODE HERE


# TODO 2: Check for grade A (90 and above)
# Use >= to check if grade is 90 or higher
# If true, print "Your letter grade is: A"

# YOUR CODE HERE


# TODO 3: Check for grade B (80 to 89) 
# Use >= to check if grade is 80 or higher
# If true, print "Your letter grade is: B"

# YOUR CODE HERE


# TODO 4: Check for grade C (70 to 79)
# Use >= to check if grade is 70 or higher  
# If true, print "Your letter grade is: C"

# YOUR CODE HERE


# TODO 5: Check for grade D (60 to 69)
# Use >= to check if grade is 60 or higher
# If true, print "Your letter grade is: D"

# YOUR CODE HERE


# TODO 6: Handle grade F (below 60)
# Use else to handle any remaining grades
# Print "Your letter grade is: F"

# YOUR CODE HERE


print()
print("--- Additional Messages ---")

# TODO 7: Special message for perfect score
# Use == to check if grade equals exactly 100
# If true, print "Perfect score! Amazing work!"

# YOUR CODE HERE


# TODO 8: Excellence message  
# Use >= and != together with 'and'
# Check if grade >= 95 AND grade != 100
# If true, print "Excellent work!"

# YOUR CODE HERE


# TODO 9: Good job message
# Use >= and < together with 'and'  
# Check if grade >= 80 AND grade < 95
# If true, print "Good job! Keep it up!"

# YOUR CODE HERE


# TODO 10: Encouragement message
# Use >= and < together with 'and'
# Check if grade >= 60 AND grade < 80  
# If true, print "You're passing! Try to improve next time."

# YOUR CODE HERE


# TODO 11: Support message
# Use < to check if grade is less than 60
# Use 'and' to also check that grade >= 0 (valid grade)
# If true, print "Don't give up! You can do better next time!"

# YOUR CODE HERE


print()
print("Thanks for using the Grade Checker! 🎓")
