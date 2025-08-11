# if-statements

# Python If Statements - GitHub Classroom Assignment

## Learning Objectives
By the end of this lesson, you will be able to:
- Understand the syntax and structure of if statements in Python
- Use comparison and logical operators in conditional expressions
- Write if, elif, and else statements
- Use `input()` to read user input and convert it to appropriate data types
- Apply conditional logic to solve real-world problems
- Debug common mistakes in conditional statements

## Lesson Overview

### What are If Statements?
If statements are fundamental control structures in programming that allow your code to make decisions. They execute different blocks of code based on whether certain conditions are true or false.

### Basic Syntax
```python
if condition:
    # Code to execute if condition is True
    statement1
    statement2
```

### If-Elif-Else Structure
```python
if condition1:
    # Execute if condition1 is True
elif condition2:
    # Execute if condition1 is False and condition2 is True
else:
    # Execute if all conditions are False
```

## Key Concepts

### 1. Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `<` : Less than
- `>` : Greater than
- `<=` : Less than or equal to
- `>=` : Greater than or equal to

### 2. Logical Operators
- `and` : Both conditions must be True
- `or` : At least one condition must be True
- `not` : Reverses the boolean value

### 3. Input and Output
Python's `input()` function allows you to interact with users:
- `input("prompt")` : Displays a prompt and returns user input as a string
- Always convert input to the appropriate type (e.g., `int()`, `float()`)
- Handle potential errors when converting input

```python
# Example: Reading and using user input
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote.")
```

### 4. Indentation
Python uses indentation (4 spaces) to define code blocks. All statements inside an if block must be indented at the same level.

## Common Mistakes to Avoid
1. Using `=` instead of `==` for comparison
2. Forgetting the colon `:` after the condition
3. Incorrect indentation
4. Using `=` in conditions instead of `==`

## Getting Started
1. Review the demonstration code in `demo.py`
2. Complete the interactive exercise in `exercise.py`
3. Test your code by running `python exercise.py`
4. Try different ages to see how your program responds
5. Compare your solution with `solution.py` when you're done

## Assignment Instructions
Your task is to create an interactive voting age checker:

1. **Prompt the user**: Ask "Enter your age: "
2. **Read input**: Use `input()` to get the user's age and convert it to an integer
3. **Check eligibility**: Use an if-else statement to check if age >= 18
4. **Display result**: Print "You can vote!" or "Too young to vote."

### Example Interaction
```
Enter your age: 25
You can vote!
```

```
Enter your age: 16
Too young to vote.
```

## Submission Instructions
1. Complete the exercise in `exercise.py` by replacing the `pass` statement
2. Test your program with different ages (try 16, 18, 25, 12)
3. Ensure your code runs without errors
4. Commit and push your changes to GitHub
5. The autograder will test your program with various inputs automatically

## Resources
- [Python Official Documentation - If Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Comparison Operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

Good luck with your assignment! 🐍
