import random 


computer = random.choice([0, -1, 1])  # generates a ranodm number among these three
youstr = input("enter your choice : ")  #takes input from the user
youDict = {"s":1, "w":-1, "g": 0}  # converts input into numbers 
reverseDict = {1: "snake", -1: "water", 0 :"gun"}  #

you = youDict[youstr] # takes the input match it from the dictionary and store it into the variable "you"

print(f"your choice is {reverseDict[you]},\nand computer's choice is {reverseDict[computer]}") # prints the coices of both computer and the user

if(you==computer): # conditions by which game runs !!
    print("its a  Draw!")
else:
    if(computer == -1 and you == 1 ):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you loose!")
    elif(computer == 1 and you == -1) :
        print("you loose!")
    elif(computer == 1 and you == 0):
        print("you won!")
    elif(computer == 0 and you == 1):
        print("you loose!")
    elif(computer == 0 and you == -1):
        print("you won !")
    else:
        print("something went wrong")    # this gets print when something gets wrong
        