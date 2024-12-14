'''
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''

def filter_list(l):
    'return a new list with the strings filtered out'
    return [x for x in l if not isinstance(x, str)] #isintance checks if x is a string. if not true, it appends to list