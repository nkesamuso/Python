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