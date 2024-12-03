#test_allTests.py

import os
import requests
import pytest

# Test to check if README.md file is created
def test_readme_exists():
    # Check if the README.md file exists in the current directory
    assert os.path.isfile("README.md"), "README.md file does not exist"
