'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def array_diff(a, b):
    if b: 
        for b0 in b: # for element of b
            while b0 in a: # if still in a
                a.remove(b0) # remove from a and return it
        return a
    else: # if not b, return a
        return a
    
# A best way to aproach this problem was by using list comprehension: return [x for x in a if x not in b]