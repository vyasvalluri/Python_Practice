import random


def handman():
    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validletters = "abcdefghijklmnopqrstuvwxyz"
    guessmade = ''
    turs = 10
    print("radom word is ..", word)
    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade :
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("you are win!!")
            break
        print("Guess the word : ", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("enter valid charcter ")
            guess = input()
        if guess not in word:
            turs = turs - 1
            printhangman(turs)
            if turs == 0:
                break

def printhangman(turns):
    if( turns == 9):
        print("9 turns left")
        print("  --------  ")
    if( turns == 8):
        print("8 turns left")
        print("  --------  ")
        print("     O      ")
    if turns == 7:
        print("7 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
    if turns == 6:
        print("6 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    /       ")
    if turns == 5:
        print("5 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 4:
        print("4 turns left")
        print("  --------  ")
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 3:
        print("3 turns left")
        print("  --------  ")
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
    if turns == 2:
        print("2 turns left")
        print("  --------  ")
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
    if turns == 1:
        print("1 turns left")
        print("Last breaths counting, Take care!")
        print("  --------  ")
        print("   \ O_|/   ")
        print("     |      ")
        print("    / \     ")
    if turns == 0:
        print("You loose")
        print("You let a kind man die")
        print("  --------  ")
        print("     O_|    ")
        print("    /|\      ")
        print("    / \     ")
        


name = input("Enter your name : ")
print("Welcome "+ str(name))
print("----------------------------")
print("try to guess the word is lessthan 10 attempts")
handman()
print()
