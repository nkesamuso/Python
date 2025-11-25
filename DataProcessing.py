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
