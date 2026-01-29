# python-basics-task-9
Error Handling in Python using try–except and Logging

-Description

This program demonstrates error handling in Python using try–except blocks along with the logging module.
It handles runtime errors, logs them into a file, and ensures proper program execution using else and finally.

-File Structure

error_handling.py
errors.log
README.md

- Features Implemented
	•	Uses try–except blocks
	•	Handles multiple exceptions
	•	Includes else and finally
	•	Uses Python’s logging module
	•	Saves error logs to a file
	•	Implements a custom exception class
	•	Simulates runtime errors
	•	Helps debug errors using log files

-Explanation of the Code

1️⃣ Logging Configuration

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

	•	Logs errors into errors.log
	•	Records timestamp, error level, and message

⸻

2️⃣ Custom Exception

class CustomError(Exception):
    pass

	•	Defines a user-defined exception for custom error handling

⸻

3️⃣ try–except Block

try:
    result = 10 / 0

	•	This line raises a ZeroDivisionError

⸻

4️⃣ Exception Handling

except ZeroDivisionError:
except TypeError:
except CustomError:

	•	Each exception is handled separately
	•	Error details are logged using logging.error()

⸻

5️⃣ else Block

else:
    print("result:", result)

	•	Executes only if no exception occurs

⸻

6️⃣ finally Block

finally:
    print("execution completed")

	•	Always executes, regardless of error occurrence

⸻

-Output

cannot divide by zero
execution completed


⸻

-Log File (errors.log)

The log file stores:
	•	Error type
	•	Error message
	•	Stack trace (for debugging)

Example log entry:

2026-01-29 10:30:15 - ERROR - ZeroDivisionError occurred


⸻

✅ Conclusion

This program demonstrates a complete and structured approach to:
	•	Handling runtime errors
	•	Logging errors for debugging
	•	Writing clean and reliable Python
