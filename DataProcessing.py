"""DataProcessing utilities.

This module imports NumPy and pandas. If a required dependency is missing
the module prints a short, actionable message explaining how to install it
instead of raising a raw ModuleNotFoundError when executed directly.
"""

from datetime import datetime
import sys
import warnings

warnings.filterwarnings('ignore')

try:
	import numpy as np
except Exception as exc:  # keep broad so we can show a friendly message for many import problems
	print("ERROR: Missing or broken dependency 'numpy' (needed by DataProcessing.py)")
	print("Action: install with: python -m pip install numpy")
	# re-raise so that callers (or tests) still see the original error if needed
	raise

try:
	import pandas as pd
except Exception as exc:
	print("ERROR: Missing or broken dependency 'pandas' (needed by DataProcessing.py)")
	print("Action: install with: python -m pip install pandas")
	# Provide a helpful exit with non-zero code when run as a script
	if __name__ == '__main__':
		sys.exit(1)
	# When imported, raise so importers can handle the failure explicitly
	raise


def _demo_numpy_examples() -> None:
	"""Small demo printed only when running the module as a script.

	Keeping examples inside a function and only calling it under
	`if __name__ == '__main__'` prevents side-effects when the module
	is imported from other code (and explains why you might see no
	output if you only imported the module).
	"""

	print("=" * 80)
	print("NUMPY BASICS FOR DATA PREPROCESSING")
	print("=" * 80)

	# Creating arrays
	arr = np.array([1, 2, 3, 4, 5])
	print(f"\n1. Basic array: {arr}")

	# 2D array (matrix)
	matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print(f"\n2. 2D array:\n{matrix}")

	# Array properties
	print(f"\nShape: {matrix.shape}")
	print(f"Data type: {matrix.dtype}")
	print(f"Dimensions: {matrix.ndim}")

	# Array creation functions
	zeros = np.zeros((3, 4))
	ones = np.ones((2, 3))
	random_arr = np.random.rand(3, 3)
	print(f"\n3. Zeros array:\n{zeros}")


def _demo_pandas_examples() -> None:
	print("\n" + "=" * 80)
	print("PANDAS BASICS - SERIES AND DATAFRAMES")
	print("=" * 80)

	# Creating a Series
	series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
	print(f"\n1. Pandas Series:\n{series}")

	# Creating a DataFrame
	data = {
		'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
		'Age': [28, 34, 29, 32, 45],
		'City': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo'],
		'Salary': [50000, 60000, 55000, 62000, 70000]
	}
	df = pd.DataFrame(data)
	print(f"\n2. Basic DataFrame:\n{df}")

	# DataFrame info
	print(f"\n3. DataFrame Info:")
	print(df.info())
	print(f"\nShape: {df.shape}")
	print(f"Columns: {df.columns.tolist()}")


if __name__ == '__main__':
	_demo_numpy_examples()
	_demo_pandas_examples()

print("\n" + "=" * 80)
print("DATA LOADING TECHNIQUES")
print("=" * 80)

# Create sample data for demonstration
sample_data = {
    'student_id': range(1, 21),
    'name': ['Student_' + str(i) for i in range(1, 21)],
    'math_score': np.random.randint(50, 100, 20),
    'english_score': np.random.randint(45, 95, 20),
    'science_score': np.random.randint(40, 100, 20),
    'attendance': np.random.uniform(70, 100, 20),
    'age': np.random.randint(15, 19, 20)
}
df_students = pd.DataFrame(sample_data)

print("\n1. Sample student dataset:")
print(df_students.head())

# Reading CSV (example syntax)
print("\n2. Reading data from files:")
print("# df = pd.read_csv('data.csv')")
print("# df = pd.read_excel('data.xlsx')")
print("# df = pd.read_json('data.json')")