import logging
import numpy as np
def subtract(a, b):
	return a - b

def multiply(a, b):
	return a*b

def divide(a, b):
	if b == 0:
		raise ValueError("MIANOWNIK NIE MOZE SIE ROWNAC 0")
	return a/b

def calculate_mean(numbers):
	return np.mean(numbers)
if __name__ == '__main__':
	#Uruchomienie funkcji z różnych bibliotek
	logging.basicConfig(level=logging.INFO)
	logging.info("Program uruchomiony")
	
	numbers = [1,2,3,4,5]
	mean = calculate_mean(numbers)
	logging.info(f"Srednia wynosi: {mean}")

	#Przykladowe wywolania funkcji
	a = 5
	b = 2
	logging.info(f"{a} - {b} = {subtract(a,b)}")
