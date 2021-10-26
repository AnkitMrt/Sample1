import unittest
import script

class Testing(unittest.TestCase):
  def test_divBy3(self):
    self.assertAlmostEqual(script.div3(222),True)
    self.assertAlmostEqual(script.div3(19),False)
 
if __name__=='__main__':
  unittest.main()
