from random import randint 

t = ["Yes", "No", "Try Asking Agian", "I don't think so", "Neither", "Nothing", "Maybe Someday"]

computer = t[randint(0,6)]

player = False

while player == False:
   userInput = input("I am the magic Conch Shell, Ask me a question.\n")
   print(computer)
   player = False
   computer = t[randint(0,6)]