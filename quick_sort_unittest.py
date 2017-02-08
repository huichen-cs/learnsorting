import unittest

from quick_sort_concept import quick_sort

class QuickSortTest(unittest.TestCase):


    def test_quick_sort_random_1(self):
        data = [4, 1, 10, 4, 4, 3, 9, 4, 1, 9]
        expected = [1, 1, 3, 4, 4, 4, 4, 9, 9, 10]
        output = quick_sort(data)
        self.assertEqual(expected, output)
        
    def test_quick_sort_random_2(self):    
        data = [10, 3, 10, 9, 7, 9, 6, 2, 7, 7]
        expected = [2, 3, 6, 7, 7, 7, 9, 9, 10, 10]
        output = quick_sort(data)
        self.assertEqual(expected, output)
        
    def test_quick_sort_sorted_asc(self):     
        data = [2, 3, 6, 7, 7, 7, 9, 9, 10, 10]
        expected = [2, 3, 6, 7, 7, 7, 9, 9, 10, 10]
        output = quick_sort(data)
        self.assertEqual(expected, output)

    def test_quick_sort_sorted_des(self):     
        data = [10, 10, 9, 9, 7, 7, 7, 6, 3, 2]
        expected = [2, 3, 6, 7, 7, 7, 9, 9, 10, 10]
        output = quick_sort(data)
        self.assertEqual(expected, output)        

if __name__ == "__main__":
    unittest.main()