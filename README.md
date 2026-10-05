# Week 6 Assignment - Future Proof With Python

## File Descriptions
- `safe_tools.py`: Contains functions that use `try/except` blocks to handle zero division, string conversion errors, and missing dictionary keys safely without crashing.
- `unbreakable.py`: Demonstrates safe user input handling to protect against runtime exceptions.

## Question Answer
**Why can the `if` check not catch `"abc"` on its own?**  
An `if` statement only evaluates conditions based on boolean logic; it cannot directly prevent or catch Python runtime execution exceptions like a `ValueError`. Converting `"abc"` to an integer using `int("abc")` raises an immediate exception that halts execution unless enclosed inside a `try / except` block.
# plp.python.week6