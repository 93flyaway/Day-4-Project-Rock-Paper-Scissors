rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#user choice serves as index for ASCII art list below
index = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

#failsafe
if (index != "0") and (index != "1") and (index != "2"):
  print("Invalid input. Please try again")

else:
  index = int(index)

#format the choices as a list
  choice = [rock, paper, scissors]
  user_choice = choice[index]

#randomly generate conputer choice
  computer_choice = random.choice(choice)

#determine win or loss
  if user_choice == computer_choice:
    result = "draw"
  else:
    if (user_choice == rock and computer_choice == scissors) or (user_choice == paper and computer_choice == rock) or (user_choice == scissors and computer_choice == paper):
      result = "win"
    else:
      result = "lose"

#print user choice and computer choice
  print(user_choice)
  print("Computer chose:\n" + computer_choice)

#print result
  if result == "draw":
    print("It's a draw!")
  else:
    print(f"You {result}!")