""" The unitest file for the clasification of Triangle"""
import unittest
from HW_01_Krupali import classifyTriangle

class clasification(unittest.TestCase): 
    def test_classifyTriangle(self):
        """test cases for triangle"""
        #Interger Values
        self.assertEqual(classifyTriangle(3,4,5),"The triangle is Scalene as well as a Right")
        self.assertEqual(classifyTriangle(1,1,1),"The Triangle is an Equilateral")
        self.assertEqual(classifyTriangle(1,2,3),"The Triangle is Scalene")
        self.assertEqual(classifyTriangle(1,1,3),"The Triangle is Isosceles")
        self.assertEqual(classifyTriangle(1,0,3),"The side cannot be 0")

        #Float values
        self.assertEqual(classifyTriangle(1.2,1.2,1.2),"The Triangle is an Equilateral")
        self.assertEqual(classifyTriangle(1.2,2,3),"The Triangle is Scalene")
        self.assertEqual(classifyTriangle(1.5,1.5,3),"The Triangle is Isosceles")
        self.assertEqual(classifyTriangle(1.3,0,3),"The side cannot be 0")

        #Integer Values
        self.assertNotEqual(classifyTriangle(3,3,5),"The triangle is Scalene as well as a Right")
        self.assertNotEqual(classifyTriangle(1,2,1),"The Triangle is an Equilateral")
        self.assertNotEqual(classifyTriangle(1,1,3),"The Triangle is Scalene")
        self.assertNotEqual(classifyTriangle(1,2,3),"The Triangle is Isosceles")

        #Float values
        self.assertNotEqual(classifyTriangle(3.5,3.5,5),"The triangle is Scalene as well as a Right")
        self.assertNotEqual(classifyTriangle(1.5,2,1.5),"The Triangle is an Equilateral")
        self.assertNotEqual(classifyTriangle(1.6,1.6,3),"The Triangle is Scalene")
        self.assertNotEqual(classifyTriangle(1.3,2,3),"The Triangle is Isosceles")

        
#start from here
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)