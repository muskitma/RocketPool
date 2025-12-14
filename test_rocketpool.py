# test_rocketpool.py
"""
Tests for RocketPool module.
"""

import unittest
from rocketpool import RocketPool

class TestRocketPool(unittest.TestCase):
    """Test cases for RocketPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RocketPool()
        self.assertIsInstance(instance, RocketPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RocketPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
