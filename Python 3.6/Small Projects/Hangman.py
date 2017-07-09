from random import randint
import linecache

# ============= Functions ================


def pick_word():  # chooses a word from a dictionary
    with open("sowpods.txt", "r") as file:
        numberoflines = sum(1 for _ in file)  # counts number of lines
        return linecache.getline("sowpods.txt", randint(0, numberoflines))  # random word


def check_letter(letts, lett):  # checks if input is single letter and if it has not been used before
    if not lett.isalpha() or len(lett) != 1:  # single letter
        return False
    for i in range(0, len(letts)):  # first use
        if letts[i] == lett:
            return False
    return True  # if neither of the above, return true


def check_if_letter_exists_and_place(listtocheck, listtoplace, lett):  # checks if the word contains the given letter,
    flag = False                                                       # and if so places the  places the letters on
    for i in range(0, len(listtocheck)):                               # the word list
        if listtocheck[i] == lett:
            listtoplace[i] = lett
            flag = True
    if flag:
        return listtoplace  # return changed list
    else:
        return False  # if no change, return false


def take_input():
    letter = input("Select a letter:").upper()  # take first input
    while not check_letter(letters, letter):  # if correct, proceed, if not, request input again
        letter = input("You either did not enter a letter, or you have picked it already.\n"
                       "Select again please:").upper()
    letters.append(letter)  # add to letters used
    print("Letters used:")
    print(letters)


# ============ Initialization ================
words = list(pick_word().upper())  # list that holds the word. Cannot be seen by the player.
wordguess = []  # list that begins empty, but starts forming the word when correct letters are placed. Can be seen.
letters = []  # letters that have been used.
strikes = 0  # number of letters that were not in the word. At 6 the game ends.
for c in range(0, len(words)):
    wordguess.append("_")

# ================ Main loop ==================
while True:
    print("-------------New round---------------")
    print(wordguess)

    # ======= Take input and show used letters
    take_input()

    result = check_if_letter_exists_and_place(words, wordguess, letter)
    if result is False:
        strikes = strikes + 1  # letter not in word.
    else:
        wordguess = result  # letter in word.
    if strikes == 6:
        print("You have lost...")  # game ends.
        print("The word was:%s" % ''.join(words))
        break
    print("Strikes:%d" % strikes)
    if ''.join(wordguess) == ''.join(words):
        print("You have won!!!!")  # game ends.
        break
