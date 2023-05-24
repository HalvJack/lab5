import unittest
import numpy as np
from my_script import subtract, multiply, divide, calculate_mean

class TestMyModule(unittest.TestCase):
	def test_subtract(self):
		self.assertEqual(subtract(5,2),3)
		self.assertEqual(subtract(0,0),0)
		self.assertEqual(subtract(-10,2), -12)

	def test_multiply(self):
		self.assertEqual(multiply(5,2), 10)
		self.assertEqual(multiply(3,-5), -15)
		self.assertEqual(multiply(1,1),1)

	def test_divide(self):
		self.assertEqual(divide(5,2), 2.5)
		with self.assertRaises(ValueError):
			divide(5,0)

	def test_calculate_mean(self):
		numbers = [1,2,3,4,5]
		self.assertEqual(calculate_mean(numbers), np.mean(numbers))


if __name__ == '__main__':
	unittest.main()
