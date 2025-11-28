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

# Pandas basics, series and DataFrame examples
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

# Data loading techniques demonstration
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


print("\n" + "=" * 80)
print("DATA INSPECTION")
print("=" * 80)

print("\n1. First few rows:")
print(df_students.head(3))

print("\n2. Last few rows:")
print(df_students.tail(3))

print("\n3. Basic statistics:")
print(df_students.describe())

print("\n4. Data types:")
print(df_students.dtypes)

print("\n5. Shape and dimensions:")
print(f"Shape: {df_students.shape}")
print(f"Number of rows: {len(df_students)}")
print(f"Number of columns: {len(df_students.columns)}")


print("\n" + "=" * 80)
print("HANDLING MISSING DATA")
print("=" * 80)

# Create dataset with missing values
df_missing = df_students.copy()
df_missing.loc[2, 'math_score'] = np.nan
df_missing.loc[5, 'english_score'] = np.nan
df_missing.loc[8, 'science_score'] = np.nan
df_missing.loc[10, 'attendance'] = np.nan

print("\n1. Detecting missing values:")
print(f"Total missing values:\n{df_missing.isnull().sum()}")
print(f"\nPercentage missing:\n{(df_missing.isnull().sum() / len(df_missing) * 100).round(2)}")

print("\n2. Dropping missing values:")
df_dropped = df_missing.dropna()
print(f"Shape after dropping: {df_dropped.shape}")

print("\n3. Filling missing values:")
# Fill with mean
df_filled = df_missing.copy()
df_filled['math_score'].fillna(df_filled['math_score'].mean(), inplace=True)
df_filled['english_score'].fillna(df_filled['english_score'].median(), inplace=True)
df_filled['attendance'].fillna(df_filled['attendance'].mean(), inplace=True)
print(f"Missing values after filling:\n{df_filled.isnull().sum()}")

print("\n4. Forward fill and backward fill:")
df_ffill = df_missing.fillna(method='ffill')  # Forward fill
df_bfill = df_missing.fillna(method='bfill')  # Backward fill
print("Forward fill and backward fill applied")