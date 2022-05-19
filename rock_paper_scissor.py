import random
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
choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

# 0 = Rock Conditions
if choice_user == 0:
  if computer_choice ==0:
    print("You chose rock")
    print(rock)
    print("computer chose rock")
    print(rock)
    print("Match Tied!")
  elif computer_choice == 1:
    print("You chose rock")
    print(rock)
    print("computer chose paper")
    print(paper)
    print("You Lose!")
  else:
    print("You chose rock")
    print(rock)
    print("computer chose scissor")
    print(scissors)
    print("You won!")
#  1 = Paper Conditions 
elif choice_user == 1:
  if computer_choice ==0:
    print("You chose paper")
    print(paper)
    print("computer chose rock")
    print(rock)
    print("You Won!")
  elif computer_choice == 1:
    print("You chose paper")
    print(paper)
    print("computer chose paper")
    print(paper)
    print("Match Tied.")
  else:
    print("You chose paper")
    print(paper)
    print("computer chose scissor")
    print(scissors)
    print("You Lost!")

# 2 = scissors conditions
elif choice_user == 2:
  if computer_choice ==0:
    print("You chose scissors")
    print(scissors)
    print("computer chose rock")
    print(rock)
    print("You Lost.")
  elif computer_choice == 1:
    print("You chose scissors")
    print(scissors)
    print("computer chose paper")
    print(paper)
    print("You Won!")
  else:
    print("You chose scissors")
    print(scissors)
    print("computer chose scissor")
    print(scissors)
    print("Match Tied")

else:
  print("Wrong input choose only one from 0,1 or 2 ")