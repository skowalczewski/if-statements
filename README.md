# Python If Statements - Simple Grade Checker

Welcome to your lesson on Python if statements! This is designed for absolute beginners who only know variables, `input()`, and `print()`.

## What You'll Learn

By the end of this exercise, you will understand:
- How to use `if`, `elif`, and `else` statements
- Comparison operators (`<`, `<=`, `>`, `>=`, `==`, `!=`)
- Logical operators (`and`, `or`, `not`)
- How to combine conditions

## Lesson: If Statements in Python

### What is an If Statement?

An `if` statement lets your program make decisions. It's like asking a question: "If this is true, then do this."

```python
age = 18
if age >= 18:
    print("You can vote!")
```

### Basic Structure

```python
if condition:
    # do something
elif another_condition:
    # do something else
else:
    # do this if nothing else was true
```

## Comparison Operators

These operators let you compare values:

| Operator | Meaning | Example |
|----------|---------|---------|
| `>` | Greater than | `10 > 5` is True |
| `<` | Less than | `3 < 8` is True |
| `>=` | Greater than or equal | `5 >= 5` is True |
| `<=` | Less than or equal | `4 <= 7` is True |
| `==` | Equal to | `6 == 6` is True |
| `!=` | Not equal to | `5 != 3` is True |

### Examples:

```python
score = 85

if score >= 90:
    print("Grade A!")
elif score >= 80:
    print("Grade B!")
elif score >= 70:
    print("Grade C!")
else:
    print("Grade F")
```

## Logical Operators

### AND Operator (`and`)
Both conditions must be true:

```python
grade = 85
if grade >= 80 and grade < 90:
    print("This is a B grade")
```

### OR Operator (`or`)
At least one condition must be true:

```python
grade = 105
if grade < 0 or grade > 100:
    print("Invalid grade!")
```

### NOT Operator (`not`)
Reverses true/false:

```python
is_failing = False
if not is_failing:
    print("Student is passing!")
```

## Your Exercise: Grade Checker

Your task is to complete a simple grade checker program that:

1. **Gets input** - Asks for a numeric grade
2. **Checks validity** - Makes sure grade is between 0-100
3. **Assigns letter grade** - A, B, C, D, or F
4. **Shows encouragement** - Different messages based on performance

### Grade Scale:
- **A:** 90-100
- **B:** 80-89
- **C:** 70-79  
- **D:** 60-69
- **F:** Below 60

### What You'll Use:
- ✅ Variables (like `grade = 85`)
- ✅ `input()` function to get user input
- ✅ `print()` function to show output
- ✅ `if/elif/else` statements for decisions
- ✅ Comparison operators (`>=`, `==`, etc.)
- ✅ Logical operators (`and`, `or`, `not`)

### What You DON'T Need:
- ❌ No functions (`def`)
- ❌ No loops (`for`, `while`)
- ❌ No complex programming concepts

## Getting Started

1. Open this repository in a Codespace (click the green "Code" button)
2. Look at `main.py` - it has TODO comments showing you what to do
3. Fill in the missing code step by step
4. Test your program: `python main.py`
5. Push your changes to see if it passes the tests!

## Example Run

```
📊 Welcome to the Grade Checker! 📊
Enter your numeric grade and I'll tell you the letter grade.

Enter your numeric grade: 87

Checking your grade...

Your letter grade is: B

--- Additional Messages ---
Good job! Keep it up!

Thanks for using the Grade Checker! 🎓
```

## Tips for Success

1. **Read each TODO carefully** - They tell you exactly what to do
2. **Test with different grades** - Try 95, 75, 105, -5 to see what happens
3. **Check your spacing** - Python is picky about indentation
4. **One step at a time** - Complete each TODO before moving to the next

Good luck with your first if statement program! 🎯