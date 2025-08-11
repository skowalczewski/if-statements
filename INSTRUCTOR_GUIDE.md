# Instructor Guide - Python If Statements Assignment

## Overview
This assignment teaches students fundamental if-statement concepts through an interactive voting age checker program. Students will learn to use `input()`, type conversion, and conditional logic.

## Assignment Structure

### Files Overview
- `exercise.py` - Student template with `pass` statement to replace
- `solution.py` - Complete working solution with error handling
- `demo.py` - Comprehensive examples including input() usage
- `README.md` - Student instructions and examples
- `.github/classroom/autograding.json` - Automated testing configuration

## New Input/Output Testing Approach

This assignment uses input/output testing instead of function-based testing to make it more interactive and beginner-friendly.

### Benefits
- More engaging for students
- Mirrors real-world program interaction
- Easier to understand for beginners
- Teaches proper input handling
- Demonstrates practical applications

### Test Cases
The autograder tests four scenarios:
1. Age 16 → "Too young to vote."
2. Age 18 → "You can vote!"
3. Age 25 → "You can vote!"
4. Age 12 → "Too young to vote."

Each test case provides input via `echo` and checks for expected output strings.

## Grading Criteria

### Automated Testing (100 points total)
- **Test 1** (25 points): Age 16 - Correctly identifies as too young
- **Test 2** (25 points): Age 18 - Correctly identifies as eligible
- **Test 3** (25 points): Age 25 - Correctly identifies as eligible
- **Test 4** (25 points): Age 12 - Correctly identifies as too young

### Manual Review Checklist
- [ ] Uses `input()` with correct prompt: "Enter your age: "
- [ ] Converts input to integer using `int()`
- [ ] Uses if-else statement (not just if)
- [ ] Correct comparison operator (`>=` 18)
- [ ] Exact output messages: "You can vote!" and "Too young to vote."
- [ ] Code is properly indented
- [ ] Removed the `pass` statement

## Common Student Mistakes

### 1. Incorrect Prompt Text
**Mistake**: `input("Enter age: ")` or `input("Age: ")`
**Correct**: `input("Enter your age: ")`

### 2. Forgetting Type Conversion
**Mistake**: `age = input("Enter your age: ")`
**Correct**: `age = int(input("Enter your age: "))`

### 3. Wrong Comparison Operator
**Mistake**: `if age > 18:` (excludes 18-year-olds)
**Correct**: `if age >= 18:`

### 4. Incorrect Output Messages
**Mistake**: `print("You can vote")` or `print("Too young")`
**Correct**: `print("You can vote!")` and `print("Too young to vote.")`

### 5. Missing else Statement
**Mistake**: Only using `if` without `else`
**Correct**: Using complete `if-else` structure

## Testing the Assignment Manually

### Method 1: Direct Execution
```bash
cd assignment-directory
python exercise.py
# Enter test ages: 16, 18, 25, 12
```

### Method 2: Automated Input
```bash
echo "16" | python exercise.py
echo "18" | python exercise.py
echo "25" | python exercise.py
echo "12" | python exercise.py
```

### Expected Outputs
- Input "16" → Output contains "Too young to vote."
- Input "18" → Output contains "You can vote!"
- Input "25" → Output contains "You can vote!"
- Input "12" → Output contains "Too young to vote."

## Student Support

### Hints for Struggling Students
1. Start by writing the `input()` line first
2. Test the input by printing it back: `print(f"You entered: {age}")`
3. Add the if-else structure step by step
4. Test with the boundary case (age 18) specifically

### Extension Activities
For advanced students:
- Add error handling with try-except
- Extend to include more voting requirements (citizenship, registration)
- Create a more complex age-based classification system

## Common Questions

**Q: Why input/output testing instead of functions?**
A: It's more intuitive for beginners and teaches practical programming skills.

**Q: What if students add extra features?**
A: As long as core functionality works and tests pass, extra features are fine.

**Q: How strict is the output matching?**
A: Tests use "included" comparison, so exact punctuation and capitalization matter.

**Q: Should students handle invalid input?**
A: Not required for basic assignment, but shown in solution.py as good practice.

## Troubleshooting

### Autograder Issues
- Ensure student hasn't changed required output messages
- Check that `exercise.py` exists and is executable
- Verify no infinite loops or input blocking

### Common Runtime Errors
- `ValueError`: Student forgot `int()` conversion and entered non-numeric input
- `NameError`: Student misspelled variable names
- `IndentationError`: Incorrect indentation in if-else blocks

This assignment provides a solid foundation in conditional logic while teaching essential input/output skills.