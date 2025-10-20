# test_blockconnector.py
"""
Tests for BlockConnector module.
"""

import unittest
from blockconnector import BlockConnector

class TestBlockConnector(unittest.TestCase):
    """Test cases for BlockConnector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockConnector()
        self.assertIsInstance(instance, BlockConnector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockConnector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
