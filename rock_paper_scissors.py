import asciiart
import random
rpc = [asciiart.rock, asciiart.paper, asciiart.scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
print (rpc[int(user_choice)])

print("Computer chose:")
computer_choice = random.randint(0,2)
print(rpc[computer_choice])

if int(user_choice) == computer_choice:
  print("It's a tie")
elif int(user_choice) == 0 and computer_choice == 1:
  print("Paper beats rock. You lose.")
elif int(user_choice) == 0 and computer_choice == 2:
  print("Rock beats scissors. You win.")
elif int(user_choice) == 1 and computer_choice == 0:
  print("Paper beats rock. You win.")
elif int(user_choice) == 1 and computer_choice == 2:
  print("Scissors beats paper. You lose.")
elif int(user_choice) == 2 and computer_choice == 0:
  print("Rock beats scissors. You lose.")
elif int(user_choice) == 2 and computer_choice == 1:
  print("Scissors beats paper. You win.")
