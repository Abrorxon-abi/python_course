import unittest
from tests.main import random_fn as fn


class TestUnitTesting(unittest.TestCase):
    
    def test_random_function(self):
        result = fn()
        assert result == 'hello wor!'