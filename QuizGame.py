gameOver = False
while gameOver == False:
    print("Welcome to the Nintendo game show.")
    print("First Question, When was Nintendo founded?")
    userInput = input("A)1999 B)1845 C)1776 D)1889\n")
    if(userInput == "1889"):
        userInput = input("Corret! Next Question, Where did Mario first appear?")
    elif(userInput == "1999"):
        print("Wrong, you lose")
    elif(userInput == "1845"):
        print("Wrong, you lose")
    elif(userInput == "1776"):
        pprint("Wrong, you lose")