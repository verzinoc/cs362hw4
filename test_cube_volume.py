import unittest
import cube_volume

class TestVolumeCalculator(unittest.TestCase):
   def test_1(self):
      result = cube_volume.calc_volume(3)
      self.assertEqual(result, 27)

   def test_2(self):
      result = cube_volume.calc_volume(-3)
      self.assertEqual(result, 0)
      
   def test_3(self):
      result = cube_volume.calc_volume(1.5)
      self.assertEqual(result, 3.375)

if __name__ == "__main__":
   unittest.main(verbosity=2)
