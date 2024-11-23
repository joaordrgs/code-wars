# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u'] # Determine the vowels to look for
    return sum(1 for n in list(sentence) if n.lower() in vowels) # Sum 1 to every lower char in the setence if encountered in the vowels list