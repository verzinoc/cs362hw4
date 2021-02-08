import unittest
import average_list

class TestAverageList(unittest.TestCase):
   def test_1(self):
      result = average_list.calc_average([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
      self.assertEqual(result, 5)

   def test_2(self):
      result = average_list.calc_average([])
      self.assertEqual(result, 0)

   def test_3(self):
      result = average_list.calc_average([1, 10])
      self.assertEqual(result, 5.5)

if __name__ == "__main__":
   unittest.main(verbosity=2)
