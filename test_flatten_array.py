import unittest
from flatten_array import flatten_array

#test cases for flatten_array.py
class FlattenArrayTestCases(unittest.TestCase):
    #test example given in email
    def test_example_in_email(self):
        self.assertEqual(flatten_array([[1,2,[3]],4]), [1,2,3,4])

    #test empty array
    def test_empty_array(self):
        self.assertEqual(flatten_array([]), [])

    #test array of only ints
    def test_int_array(self):
        self.assertEqual(flatten_array([1,2,3,4]), [1,2,3,4])

    #test arrays with all arrays
    def test_all_arries(self):
        self.assertEqual(flatten_array([[1,[2]], [3], [[4,5,6,[7,8]]]]), [1,2,3,4,5,6,7,8])

    #test array with both ints/arrays:
    def test_general_array(self):
        self.assertEqual(flatten_array([1, [2], [3, [[4]]], [5, 6], 7, 8]), [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()