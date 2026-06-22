# test_oracledrift.py
"""
Tests for OracleDrift module.
"""

import unittest
from oracledrift import OracleDrift

class TestOracleDrift(unittest.TestCase):
    """Test cases for OracleDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleDrift()
        self.assertIsInstance(instance, OracleDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
