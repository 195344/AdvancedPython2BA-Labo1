# test_utils.py


import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3),6)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,0,0),(0,0))
        pass
    
    def test_integrate(self):
        y = 1
        self.assertEqual(utils.integrate((lambda x: 1),0,1),y)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
