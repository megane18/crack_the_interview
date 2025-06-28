# tests/conftest.py
import pytest
import sys
import os

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


# Common test data that might be useful across multiple test files
@pytest.fixture
def sample_strings():
    """Common string test data"""
    return {
        "empty": "",
        "single": "a",
        "unique": "abcdef",
        "duplicate": "hello",
        "palindrome": "racecar",
        "permutation_pair": ("abc", "bca"),
        "non_permutation_pair": ("abc", "def"),
    }


@pytest.fixture
def sample_arrays():
    """Common array test data"""
    return {
        "empty": [],
        "single": [1],
        "sorted": [1, 2, 3, 4, 5],
        "reverse_sorted": [5, 4, 3, 2, 1],
        "duplicates": [1, 2, 2, 3, 3, 3],
        "mixed": [3, 1, 4, 1, 5, 9, 2, 6, 5],
    }


# Configure pytest
def pytest_configure(config):
    """Configure pytest"""
    # Add custom markers
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line("markers", "edge_case: marks tests as edge cases")
