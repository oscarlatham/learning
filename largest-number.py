import array as arr
from statistics import variance
from tkinter import Variable

# Create the array of numbers
numbers = arr.array('i', [3, 99, 56, 8, 5, 9, 10, 7, 78, 23, 100])

largestNumber = 0

# Loop the array of numbers
for currentNumber in numbers:
    if currentNumber > largestNumber:
        largestNumber = currentNumber

print(largestNumber)
