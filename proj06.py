word_in_list = ['d', 'o', 'o', 'o', 'o', 'o','t']
guess_letter = raw_input('Enter a letter')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guesses = 8
wordlength = int(len(word_in_list))
alphabetlength = int(len(alphabet))
y = 0
z = 0
final_word_reveal = []
for var in range(wordlength):
    if guess_letter == word_in_list[y]:
        print "\nGreat guess!"
        word_in_list.remove(str(guess_letter))
        final_word_reveal.append(str(guess_letter))
    else:
        print 'none'
        y = y + 1
    if word_in_list == []:
        print "\nYou finished the game! Hooray!"

for var2 in range(alphabetlength):
    if guess_letter == alphabet[z]:
        alphabet.remove(str(guess_letter))
    else:
        z = z + 1

y = 0
z = 0
wordlength = int(len(word_in_list))
alphabetlength = int(len(alphabet))
print "Available letters: " + str(alphabet)
print word_in_list


guess_letter = raw_input('Enter a number')



for var in range(wordlength):
    if guess_letter == word_in_list[y]:
        print "\nGreat guess!"
        word_in_list.remove(str(guess_letter))
        final_word_reveal.append(str(guess_letter))
    else:
        print 'none'
        y = y + 1
    if word_in_list == []:
        print "\nYou finished the game! Hooray!"

for var2 in range(alphabetlength):
    if guess_letter == alphabet[z]:
        alphabet.remove(str(guess_letter))
    else:
        z = z + 1

y = 0
z = 0
wordlength = int(len(word_in_list))
alphabetlength = int(len(alphabet))
print "Available letters: " + str(alphabet)
print word_in_list


# list = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'g', 'g', 'a', 'a', 'b']
# x = raw_input('enter a letter')
# listlength = int(len(list))
# y = 0
# for z in range(listlength):
#     if x == list[y]:
#         list.remove(str(x))
#         print list
#     else:
#         print 'none'
#         y = y + 1




# word_in_list = ['d', 'o', 'o', 't']
# guess_letter = raw_input('Enter a letter')
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# guesses = 8
# wordlength = int(len(word_in_list))
# y = 0
# final_word_reveal = []
# for var in range(wordlength):
#     if guess_letter == word_in_list[y]:
#         print "\nGreat guess!"
#         alphabet.remove(str(guess_letter))
#         word_in_list.remove(str(guess_letter))
#         final_word_reveal.append(str(guess_letter))
#         print "Available letters: " + str(alphabet)
#     else:
#         print 'none'
#         y = y + 1
#     if word_in_list == []:
#         print "\nYou finished the game! Hooray!"