'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.

StringsFundamentals
'''

def are_you_playing_banjo(name):
    # Implement me!
    return f'{name} plays banjo' if name[0].upper() == 'R' else f'{name} does not play banjo' 