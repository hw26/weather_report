import unittest,sys
from dwolla_technical import main




class TestAnswerReturn(unittest.TestCase):
    def testHouston(self):
    	__builtins__.raw_input = lambda _: 'Houston'
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output,'Houston temprature is 43.4333333333 fahrenheit')

    def testSanFrancisco(self):
    	__builtins__.raw_input = lambda _:"San Francisco"
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, 'San Francisco temprature is 36.3055555556 fahrenheit')

    def testAtlanta(self):
    	__builtins__.raw_input = lambda _:"Atlanta"
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output,'Atlanta temprature is 37.9222222222 fahrenheit')

    def testNoCity(self):
    	__builtins__.raw_input = lambda _:"xxx"
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, 'city not found')





if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)        