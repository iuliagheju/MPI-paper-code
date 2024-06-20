import unittest
from src.sorting_algorithms import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_sorting(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 34, 64, 90])

if __name__ == '__main__':
    unittest.main()
