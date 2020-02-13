# test_utils.py


import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3),6)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(0,1,-1),1)
        pass
    
    def test_integrate(self):
        self.assertEqual(utils.integrate(1,0,1),1)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
