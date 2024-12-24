'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''
def find_short(s):
    temp = s.split(' ')[0]
    for word in s.split(' '):
        if len(word) < len(temp):
            temp = word
    else:
        return len(temp)