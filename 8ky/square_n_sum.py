'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because
'''

def square_sum(numbers):
    #your code here
    return sum(n**2 for n in numbers)