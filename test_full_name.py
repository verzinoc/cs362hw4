import unittest
import full_name

class TestFullName(unittest.TestCase):
   def test_1(self):
      result = full_name.generate_name("Tony", "Stark")
      self.assertEqual(result, "Tony Stark")

   def test_2(self):
      result = full_name.generate_name("Neymar", "da Silva Santos Junior")
      self.assertEqual(result, "Neymar da Silva Santos Junior")
   
   def test_3(self):
      result = full_name.generate_name("Cher", "")
      self.assertEqual(result, "Cher")

if __name__ == "__main__":
   unittest.main(verbosity=2)
