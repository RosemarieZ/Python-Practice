gameOver= False
while gameOver == False:
    userInput = input("Welcome to UA, are you a new student?")
    if(userInput == "yes"):
        userInput = input("Would you like a guide to your classes?")
        if(userInput == "yes"):
          userInput = input("Great Let's go! What is your quirk by the way?")
          if(userInput.isalpha()):
            userInput = input("That's so cool! What's your name?")
            if(userInput.isalpha()):
               userInput = input("Nice to meet you! My name is Midoriya Izuku, wanna be friends?")
               if(userInput == "yes"):
                   userInput = input("Great, I am so glad!")
               elif(userInput == "no"):
                   userInput = input("Oh, well okay then.")
               else:
                   print("I guess not.")
        elif(userInput == "no"):
            userInput = input("Okay, well, what is your quirk?")
            if(userInput.isalpha):
                userInput = input("That's so cool! Wanna train together one day?")
                if(userInput == "yes"):
                  userInput = input("Cool, I can't wait!")
                elif(userInput == "no"):
                     userInput = input("well, I hope we can see each other soon.")
        else:
            print("Are you okay?")
    elif(userInput == "no"):
         userInput = input("Oh, well then, are you here for a tour?")
         if(userInput == "yes"):
            userInput = input("Great let's go!")
         elif(userInput == "no"):
             userInput = input("Okay, well you should leave then.")
             gameOver = True
         else:
             print("Are you okay?")
    else:
         print("Are you shy?")