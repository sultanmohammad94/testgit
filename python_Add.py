from unittest import TestCase
import unittest


class TestCalculator(TestCase):
   def test_add(self): 
    '''Test if the add operation work correclty.'''
    n1 = 5
    n2 = 10
    self.assertEqual(15, n1 + n2)
    self.assertEqual(1, False + 1)
    self.assertEqual(2,  True + 1)
    self.assertEqual(1, True + 0)
    self.assertEqual(0, False + 0)
    self.assertEqual(1, True + False)
        
    with self.assertRaises(TypeError):
        "4" + 1
        

if __name__ == "__main__":
    unittest.main()
