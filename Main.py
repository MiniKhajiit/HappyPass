# -*- coding: utf-8 -*-

import random

# Generates 2 random words, adj and noun, from txt files included in folder
# (My txt files are separated by a 'new line' for readability)
def getAdj():
    # Choose a random adjective from the text file
    with open("Adjectives.txt", "r") as adjTxt:
        adjFile = adjTxt.read()
    adjList = list(adjs for adjs in adjFile.split("\n"))
    adj = random.choice(adjList)
    return adj

def getNoun():
    # Choose a random noun from the text file
    with open("Fantasy.txt", "r") as nounTxt:
        nounFile = nounTxt.read()
    nounList = list(nouns for nouns in nounFile.split("\n"))
    noun = random.choice(nounList)
    return noun

# Dictionary for charcter replacements
abcReplace = {
    "a": "@",
    "b": "8",
    "c": "(",
    "e": "3",
    "f": "5",
    "g": "6",
    "h": "}{",
    "i": "!",
    "j": "]",
    "k": "1<",
    "l": "1",
    "m": "^^",
    "n": "^",
    "o": "0",
    "r": "7",
    "s": "$",
    "t": "+",
    "v": "\/",
    "w": "uu",
    "x": "%",
    "z": "2"
}
def getFiller():
    fill = random.choice(["~", "=", "*", "_", ">", "-", ".", ",", ";"])
    return fill

# Checks if the password will be able to meet length standards - bigger is better, eh?
# Concatenates the 2-3 words with a filler character from the  above list
def Words():
    noun1 = getNoun()
    adj1 = getAdj()
    fill = getFiller()
    if len(adj1) <= 3:
        adj2 = getAdj()
        cat_words = (f"{adj1}{fill}{adj2}{fill}{noun1}")
        print(cat_words)
        return cat_words
    elif len(noun1) <=3:
        noun2 = getNoun()
        cat_words = (f"{adj1}{fill}{noun1}{fill}{noun2}")
        print(cat_words)
        return cat_words
    else:
        cat_words = (f"{adj1}{fill}{noun1}")
        print(cat_words)
        return cat_words

# Checks the dictionary for a pre-prescribed character substitution to strengthen the password
# without losing the totally dank, randomly generated pass phrase
def replacer(cat_words):
    replacedList = []
    listedWords = list(cat_words)
    for letter in listedWords:
        if letter in abcReplace:
            abcR = abcReplace.get(letter)
            char_options = random.choice([letter, abcR, letter.capitalize()])
            replacedList.append(char_options)
        else:
            char_options = random.choice([letter, letter.capitalize()])
            replacedList.append(char_options)
    newString = "".join(replacedList)
    return newString
        
Password = (f"{replacer(Words())}")
print (Password)