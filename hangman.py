import csv

file = open("words.csv", encoding='utf-8')
csvreader = csv.reader(file)
words = []

for i in csvreader:
    words.append(i[0])


def makeMan (lives):
    if lives == 5:
        return print("____\n|  |\n|\n|\n|\n|\n|\n")
    if lives == 4:
        return print("____\n|  |\n|  O\n|\n|\n|\n|\n")
    if lives == 3:
        return print("____\n|  |\n|  O\n| \|\n|  |\n|     \n|\n")
    if lives == 2:
        return print("____\n|  |\n|  O\n| \|/\n|  |\n|    \n|\n")
    if lives == 1:
        return print("____\n|  |\n|  O\n| \|/\n|  |\n| /   \n|\n")
    if lives == 0:
        return print("____\n|  |\n|  O\n| \|/\n|  |\n| / \ \n|\n")
        
def intro():
    print("Welcome to my game! This is the known to all Hangman.")
    print("RULES:")
    print("1) You must find the following word by typing the correct letters.")
    print("2) You are allowed 4 mistakes. If you make a 5th you lose.")
    print("3) The words will be between 4 and 8 letters.")
    print("4) Have fun!!!\n")


#-------------------------- The actual game -----------------------------
done = False
intro()
#while done == False:
















file.close()