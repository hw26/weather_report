import unittest
from dwolla_technical import main




class TestAnswerReturn(unittest.TestCase):
    def testHouston(self):
    	__builtins__.raw_input = lambda _: 'Houston'
        self.assertEqual(main(),'Houston temprature is 43.4333333333 fahrenheit')

    def testSanFrancisco(self):
    	__builtins__.raw_input = lambda _:"San Francisco"
        self.assertEqual(main(), 'San Francisco temprature is 36.3055555556 fahrenheit')

    def testAtlanta(self):
    	__builtins__.raw_input = lambda _:"Atlanta"
        self.assertEqual(main(),'Atlanta temprature is 37.9222222222 fahrenheit')

    def testNoCity(self):
    	__builtins__.raw_input = lambda _:"xxx"
        self.assertEqual(main(), 'city not found')





if __name__ == '__main__':
    unittest.main()        