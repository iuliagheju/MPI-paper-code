import unittest
from src.sorting_algorithms import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_sorting(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        insertion_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

if __name__ == '__main__':
    unittest.main()
