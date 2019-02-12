import unittest
from dwolla_technical import main,get_temprature




class TestAnswerReturn(unittest.TestCase):
    def testHouston(self):

        self.assertEqual(get_temprature("Houston"),'Houston temprature is 43.4333333333 fahrenheit')

    def testSanFrancisco(self):

        self.assertEqual(get_temprature("San Francisco"), 'San Francisco temprature is 36.3055555556 fahrenheit')

    def testAtlanta(self):
        self.assertEqual(get_temprature("Atlanta"),'Atlanta temprature is 37.9222222222 fahrenheit')

    def testNoCity(self):
        self.assertEqual(get_temprature("xxx"), 'city not found')





if __name__ == '__main__':
    unittest.main()        