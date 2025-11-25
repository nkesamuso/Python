import subprocess
import sys
import unittest


class DataProcessingImportTest(unittest.TestCase):
    def test_import_or_instruct_install(self):
        """Run a short Python command that imports DataProcessing.

        If pandas is missing the module prints a helpful installation hint
        and Python exits nonzero; if pandas is available the import should
        succeed and exit status is 0.
        """
        cmd = [sys.executable, "-c", "import importlib; importlib.import_module('DataProcessing')"]
        try:
            out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as err:
            # Non-zero exit (likely missing pandas) — confirm the printed message
            self.assertIn("install with: python -m pip install pandas", err.output)
        else:
            # Import succeeded — ensure we didn't print the missing dependency message
            self.assertNotIn("Missing or broken dependency 'pandas'", out)


if __name__ == '__main__':
    unittest.main()
