import csv
import random

file = open("words.csv", encoding='utf-8')      # read the words from a given file
csvreader = csv.reader(file)
words = []

for i in csvreader:
    words.append(i[0])

file.close()

givenletters = []
foundletters = []
lives = 6
wordToFind = words[0]
abc = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]



def makeMan():          # draw the hangman
    global lives

    if lives == 6:
        return print("____\n|  |\n|\n|\n|\n|\n|\n")
    if lives == 5:
        return print("____\n|  |\n|  O\n|\n|\n|\n|\n")
    if lives == 4:
        return print("____\n|  |\n|  O\n|  |\n|  |\n|     \n|\n")
    if lives == 3:
        return print("____\n|  |\n|  O\n| \|\n|  |\n|     \n|\n")
    if lives == 2:
        return print("____\n|  |\n|  O\n| \|/\n|  |\n|    \n|\n")
    if lives == 1:
        return print("____\n|  |\n|  O\n| \|/\n|  |\n| /   \n|\n")
    if lives == 0:
        return print("____\n|  |\n|  O\n| \|/\n|  |\n| / \ \n|\n")
        
def intro():            # print intro message
    print("Welcome to my game! This is the known to all Hangman.")
    print("RULES:")
    print("1) You must find the following word by typing the correct letters.")
    print("2) You are allowed 4 mistakes. If you make a 5th you lose.")
    print("3) The words will be between 4 and 8 letters.")
    print("4) Have fun!!!\n")


def stage():                # play each stage (round)
    makeMan()
    global lives
    global givenletters
    global foundletters

    if lives == 0:                  # check if you the player is out of lives
        return endGame(0)

    if len(givenletters) > 0:
        print("The letters you have already given are: ", end='')
        for i in givenletters:    
            print(i, end=', ')
        print("\n")

    lettersMissing = 0              # print the word and the letters that have been found
    for i in wordToFind:
        if i in foundletters:
            print(i, end = ' ')
        else: 
            lettersMissing += 1
            print("_", end = ' ')
    print("\n")

    if lettersMissing == 0:              # check  if the game has been won 
        return endGame(1)
    else:                                # read the next character
        x = input("Type a letter of your choice or type 0 to exit the game: ").lower()
        flag = False
        while flag == False:
            if x not in abc and x != "0":
                x = input("Wrong input. Please type a letter of your choice or type 0 to exit the game: ").lower()
            elif x in givenletters:
                x = input("You have already picked this letter. Please choose another letter or type 0 to exit the game: ").lower()
            elif x == "0":
                return 0
            else:
                flag = True
        
        if x in wordToFind:      # the player gave a correct letter
            foundletters.append(x)
        else:                    # the player gave a wrong letter
            lives -= 1
        givenletters.append(x)
        return 1


def newGame():      # set a new game
    global givenletters
    global foundletters
    global wordToFind
    global lives

    wordToFind = random.choice(words)            # the word the player must find
    foundletters = [wordToFind[0]]               # letters that have been given by the player and exist in the word he\she must find
    givenletters = []                            # letters already given by the player
    lives = 6
    print("New Game\n")

def endGame(result):                 # end the game
    global wordToFind
    if result == 0:
        print("YOU LOST!!!\nThe correct word was " + wordToFind)
    else:
        print("YOU WON!!!\nCONGRATULATIONS!!!")


    # check if the player wants to play again
    ans = input("Do you want to play again?\nPlease type y (YES) or any other character (NO): ").lower()
    if ans == "y":
        newGame()
        return 1
    else:
        return 0

#-------------------------- The actual game -----------------------------
intro()
newGame()
while True:
    if stage() == 0:
        break