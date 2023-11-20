from unittest import TestCase, main
from calculator import calculator as fn


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(fn('2 + 2'), 4)

    def test_minus(self):
        self.assertEqual(fn('8 - 3'), 5)
    
    def test_multy(self):
        self.assertEqual(fn('4 * 4'), 16)
    
    def test_devide(self):
        self.assertEqual(fn('10 / 5'), 2)
        
    def test_no_operator(self):
        with self.assertRaises(ValueError) as error:
            fn('qwe')
        self.assertEqual('expression must have one operator +-*/', error.exception.args[0])
        
    def test_many_operator(self):
        with self.assertRaises(ValueError) as error:
            fn('2 + 2 + 2')
        self.assertEqual('expression must have two integers and one operator', error.exception.args[0])

if __name__ == '__main__':
    main()
