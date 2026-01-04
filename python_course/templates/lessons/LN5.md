🧠 LN5 — Errors & Exceptions
Python Course — CyberArena Python Lab Organ

🎯 Learning Goals
By the end of this lesson, you will be able to:
if True
• 	Use , , , and 
• 	Raise your own exceptions with 
• 	Create custom exception classes
• 	Debug errors using tracebacks

🧩 1. What Are Errors?
Python has two major categories:
1. Syntax Errors
These happen before the code runs.

    print("missing colon")• 	Understand the difference between syntax errors and runtime exceptions


Python stops immediately and complains.

2. Exceptions (Runtime Errors)
These happen while the code is running.

if True
    print("missing colon")

The code is valid, but something went wrong during execution.

🧩 2. Handling Exceptions with  / 
Basic pattern:


try:
    risky_code()
except SomeError:
    handle_it()
Example:

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That wasn’t a valid number.")
🧩 3. Multiple Exceptions

try:
    x = int("hello")
except ValueError:
    print("Not a number")
except TypeError:
    print("Wrong type")

🧩 4. Catching Any Exception (use carefully)

try:
    risky()
except Exception as e:
    print("Something went wrong:", e)


This is useful for logging, debugging, or sandboxed code.

🧩 5.  and 
  else
 runs only if no exception occurs:
try:
    x = 10
except:
    print("Error")
else:
    print("No errors!")

finally always runs:

try:
    file = open("data.txt")
except FileNotFoundError:
    print("Missing file")
finally:
    print("Cleanup always happens")



🧩 6. Raising Your Own Exceptions

def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount must be positive")


🧩 7. Custom Exception Classes

class InvalidMove(Exception):
    pass

raise InvalidMove("You cannot move there")

This is how you build domain‑specific error types for agents, dashboards, or CyberArena organs.

🧩 8. Reading Tracebacks
A traceback shows:
• 	The file
• 	The line number
• 	The message
Example:
///////////////////
File "main.py", line 12, in <module>
    x = 10 / 0
ZeroDivisionError: division by zero
////////////////////////
Understanding tracebacks is a superpower for debugging.

🧪 Mini‑Exercises
1. Catch a ZeroDivisionError
Write code that divides two numbers and handles division by zero.
2. Create a custom exception

Raise it if a speed value exceeds 120.
3. Use try/except/else/finally
Wrap a file‑open operation with all four blocks.

🧠 Summary
• 	Errors stop execution
• 	Exceptions can be caught and handled
• 	 prevents crashes
• 	 runs on success
• 	 always runs
• 	You can raise your own exceptions
• 	Custom exceptions make your code cleaner and more expressive
