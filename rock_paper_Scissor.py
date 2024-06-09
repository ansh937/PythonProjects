
import random
import os

# gameTools = ["rock", "paper", "scissor"]

# computer_won = 0
# user_won = 0

# while True:
#     randomTool = random.randint(0, 2)
#     # 0 is rock, 1 is paper, and 2 is scissor
#     computer_input = gameTools[randomTool]
#     user_input = input("Enter rock /paper/scissor or q to quit: ").lower()
    
#     if user_input == "q":
#         break
    
#     if user_input not in gameTools:
#         print("Please give valid input")
#         continue
    
#     print(f"Computer chose: {computer_input}")
    
#     if user_input == computer_input:
#         print("It's a tie")
#     elif (user_input == "rock" and computer_input == "scissor") or \
#         (user_input == "paper" and computer_input == "rock") or \
#         (user_input == "scissor" and computer_input == "paper"):
#         print("You won")
#         user_won += 1
#     else:
#         print("Computer won")
#         computer_won += 1

# print(f"You have won {user_won} times and the computer has won {computer_won} times")
# os.system(f"say 'You have won {user_won} times and the computer has won {computer_won} times'")





options=["rock","paper","scissor"]
user_wonnn=0
computer_wonnn=0
tie=0

while True:
  randromNumber=random.randint(0,2)
  computrt_inp=options[randromNumber]#This line uses the random integer generated in the previous line to select an element from the options list.
  user_inp=input("enter rock/aper/scissor or q to quit ")
  if user_inp.lower()=="q":
    break
  
  if user_inp not in options:
    print("please input valid word ")
    continue
  
  print("computer choose", computrt_inp)
  
  if user_inp==computrt_inp:
    print("Tie")
    tie+=1
  elif (user_inp == "rock" and computrt_inp == "scissor") or \
        (user_inp == "paper" and computrt_inp == "rock") or \
        (user_inp == "scissor" and computrt_inp == "paper"):
        print("You won")
        user_wonnn += 1 
  else:
        print("Computer won")
        computer_wonnn += 1

print(f"You have won {user_wonnn} times and the computer has won {computer_wonnn} times and the game come to the tie for {tie} times")
os.system(f"say 'You have won {user_wonnn} times and the computer has won {computer_wonnn} times and the game come to the tie for {tie} times'")
        
