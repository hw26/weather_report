import unittest
from dwolla_technical import main




class TestAnswerReturn(unittest.TestCase):
    def testHouston(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'Houston'
        self.assertEqual(main(), 'Houston temprature is 43.4333333333 fahrenheit')
        __builtins__.raw_input = original_raw_input

    def testSanFrancisco(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'San Francisco'
        self.assertEqual(main(), 'San Francisco temprature is 36.3055555556 fahrenheit')
        __builtins__.raw_input = original_raw_input

    def testAtlanta(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'Atlanta'
        self.assertEqual(main(), 'Atlanta temprature is 37.9222222222 fahrenheit')
        __builtins__.raw_input = original_raw_input

    def testNoCity(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'no'
        self.assertEqual(main(), 'city not found')
        __builtins__.raw_input = original_raw_input



if __name__ == '__main__':
    unittest.main()        