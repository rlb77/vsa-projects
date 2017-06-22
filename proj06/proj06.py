# Name: Santosh and Rich
# Date: 6/22/17

"""
LIST OF KNOWN ERRORS:
1) A word containing the same letter several times (Ex: aardvark)
2) Program saying that player has ran out of guesses, despite that being false
3) Words less than a certain amount of letters (Ex: 5 letters) causes program to say "Out of Range"
"""

# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.


    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word_in_list = []
word = choose_word(wordlist)
for letter in word:
    word_in_list.append(letter)
print word_in_list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guesses = 0
wordlength = int(len(word_in_list))
alphabetlength = int(len(alphabet))
y = 0
z = 0
final_word_reveal = []
var3 = 0
var4 = 0
while word_in_list != []:
    guess_letter = raw_input('Guess a letter')
    for var in range(wordlength):
        if guess_letter == word_in_list[y]:
            var3 = 1
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
        else:
            y = y + 1
        if word_in_list == []:
            print
    if var3 == 1:
        guesses = guesses - 1
        var3 = 0
        print "\nGreat guess!"
    for var2 in range(alphabetlength):
        if guess_letter == alphabet[z]:
            alphabet.remove(str(guess_letter))
        else:
            z = z + 1
    if guesses == 7:
        print
        var4 = 1
        word_in_list = []
    guesses = guesses + 1
    y = 0
    z = 0
    wordlength = int(len(word_in_list))
    alphabetlength = int(len(alphabet))
    if word_in_list != []:
        print "Available letters: " + str(alphabet)
        print word_in_list
        print "You have", 8 - guesses, "guesses left."
    if word_in_list == []:
        if var4 == 0:
            print "You win"
        if var4 == 1:
            print "You lose"

            # word = 'dogg'
            # list = []
            # list1 = []
            # for letter in word:
            #     list.append(letter)
            # for letter in word:
            #     list1.append(letter)
            # print list, list1
            #
            # listlength = len(list)
            # print listlength
            #
            # letter = raw_input('enter a letter')
            #
            # y = 0
            # x = 0
            #
            # for var in range(listlength):
            #     list[x] = '_'
            #     x = x + 1
            #
            # print list, list1
            #
            # for var2 in range(listlength):
            #     if letter == list1[y]:
            #         list[y] = list1[y]
            #     y = y + 1
            # print list
            #
            # letter = raw_input('enter a letter')
            # y = 0
            # for var2 in range(listlength):
            #     if letter == list1[y]:
            #         list[y] = list1[y]
            #     y = y + 1
            # print list
            # y = 0
            # letter = raw_input('enter a letter')
            #
            # for var2 in range(listlength):
            #     if letter == list1[y]:
            #         list[y] = list1[y]
            #     y = y + 1
            # print list