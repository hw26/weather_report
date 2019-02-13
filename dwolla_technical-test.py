import unittest,sys,urllib
from dwolla_technical import main

def raise_HTTPError():
    raise urllib.error.HTTPError(e.url, e.code)
def raise_URLError():
    raise urllib.error.URLError(e.url, e.code)    

class TestAnswerReturn(unittest.TestCase):
    def testHouston(self):
    	__builtins__.raw_input = lambda _: 'Houston'
        main()
        output = sys.stdout.getvalue().strip()
        deg = float(output.split(" ")[3])
        self.assertAlmostEqual(deg,38.0,delta = 2)

    def testSanFrancisco(self):
    	__builtins__.raw_input = lambda _:"San Francisco"
        main()
        output = sys.stdout.getvalue().strip()
        deg = float(output.split(" ")[4])
        self.assertAlmostEqual(deg,36.0,delta = 2)

    def testAtlanta(self):
    	__builtins__.raw_input = lambda _:"Atlanta"
        main()
        output = sys.stdout.getvalue().strip()
        deg = float(output.split(" ")[3])
        self.assertAlmostEqual(deg,36.0,delta = 2)

    def testNoCity(self):
    	__builtins__.raw_input = lambda _:"xxx"
        main()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, 'city not found')




    






if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)        
