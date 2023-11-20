from datetime import datetime as dt
import unittest
import time

HALF_SECOND = 0.5


class MyFullstackTests(unittest.TestCase):

    def setUp(self):
        """
        Is always used to create initial instances
        and get ready to test
        """
        self.start_time = dt.now()
        self.current_test = self.id().split(".")[-1]
        print("Sleeping 0.5 sek")
        time.sleep(HALF_SECOND)
        print(f"Starting test: {self.current_test}")

    def tearDown(self):
        self.end_time = dt.now()
        diff = self.end_time - self.start_time
        print(f"{diff} seconds:  =>   {self.id()}")

    def test_ozod(self):
        print("This is test 1")

    def test_shoxjaxon(self):
        pass

    def test_abror(self):
        pass

   # python -m unittest unit_tests.py⁡
