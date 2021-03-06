#Name - Bhavay Aggarwal	
#Roll Number - 2018384
#Section - B
#Group - 1

import unittest
from lab4 import second_max
from lab4 import admission
from lab4 import triangleType
from lab4 import validSides
from lab4 import characterCheck

class testpoint(unittest.TestCase):
	def test_ques1(self):
		""" check 2nd maximum """
		self.assertEqual(second_max(7,5,3,9),7)
		self.assertEqual(second_max(-1,-2,-3,-4),-2)
		self.assertEqual(second_max(-1,20,-30,100),20)
	
	def test_ques2(self):
		""" check admission elligibility """
		self.assertEqual(admission(75,79,86,65),-1)
		self.assertEqual(admission(80,79,83,80),-1)
		self.assertEqual(admission(65,79,63,81),-1)
		self.assertEqual(admission(80,80,80,78),-1)
		
	def test_ques3(self):
		""" check triangle type """
		self.assertEqual(triangleType(5,6,9),1)
		self.assertEqual(triangleType(6,7,7),2)
		self.assertEqual(triangleType(5,2,5),2)
		self.assertEqual(triangleType(3,4,2),1)
	
	def test_ques4(self):
		""" check valid sides of triangle """
		self.assertEqual(validSides(3,3,3),True)
		self.assertEqual(validSides(4,4,8),False)
		self.assertEqual(validSides(8,4,4),False)
		self.assertEqual(validSides(3,5,2),False)

	def test_ques5(self):
		""" check character type """
		self.assertEqual(characterCheck("$"),1)
		self.assertEqual(characterCheck("z"),3)
		self.assertEqual(characterCheck("0"),2)
	

if __name__=='__main__':
	unittest.main()
