# test_main.py
# Pytest test file for main.py


import pytest
import subprocess
import sys
import os

# Helper to run main.py as a subprocess with given input and capture output
def run_main_with_input(user_input):
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), 'main.py')],
        input=user_input,
        capture_output=True,
        text=True
    )
    return result.stdout

def test_grade_A():
    output = run_main_with_input('95\n')
    assert 'Your letter grade is: A' in output, "Expected 'Your letter grade is: A' in output for grade 95."
    assert 'Excellent work!' in output or 'Good job!' in output, "Expected an excellence or good job message for grade 95."

def test_grade_A_perfect():
    output = run_main_with_input('100\n')
    assert 'Your letter grade is: A' in output, "Expected 'Your letter grade is: A' in output for grade 100."
    assert 'Perfect score! Amazing work!' in output, "Expected perfect score message for grade 100."

def test_grade_B():
    output = run_main_with_input('85\n')
    assert 'Your letter grade is: B' in output, "Expected 'Your letter grade is: B' in output for grade 85."
    assert 'Good job! Keep it up!' in output, "Expected good job message for grade 85."

def test_grade_C():
    output = run_main_with_input('75\n')
    assert 'Your letter grade is: C' in output, "Expected 'Your letter grade is: C' in output for grade 75."
    assert "You're passing! Try to improve next time." in output, "Expected encouragement message for grade 75."

def test_grade_D():
    output = run_main_with_input('65\n')
    assert 'Your letter grade is: D' in output, "Expected 'Your letter grade is: D' in output for grade 65."
    assert "You're passing! Try to improve next time." in output, "Expected encouragement message for grade 65."

def test_grade_F():
    output = run_main_with_input('50\n')
    assert 'Your letter grade is: F' in output, "Expected 'Your letter grade is: F' in output for grade 50."
    assert "Don't give up! You can do better next time!" in output, "Expected support message for failing grade."

def test_invalid_grade_negative():
    output = run_main_with_input('-5\n')
    assert 'error' in output.lower() or 'invalid' in output.lower(), "Make sure to account for invalid grades!"

def test_invalid_grade_over():
    output = run_main_with_input('105\n')
    assert 'error' in output.lower() or 'invalid' in output.lower(), "Make sure to account for invalid grades!"

def test_grade_F(monkeypatch):
    output = run_main_with_input('50\n')
    assert 'Your letter grade is: F' in output, "Expected 'Your letter grade is: F' in output for grade 50."
    assert "Don't give up!" in output or 'better next time' in output, "Expected an encouragement message for failing grade."
