import random

choices = ["Rock", "Paper", "Scissors"]

print("Choose an option")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

for _ in range(10):  # Limit to 10 attempts to prevent infinite looping
    try:
        player_choicenum = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
        if player_choicenum not in [1, 2, 3]:
            print("Invalid choice! Please enter a number between 1 and 3")
            continue
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3")
        continue
    
    player_choice = choices[player_choicenum - 1]
    comp_choice = random.choice(choices)
    
    print("You chose:", player_choice)
    print("The Computer chose:", comp_choice)
    
    if player_choice == comp_choice:
        print("Y'all got a tie!")
    elif (player_choice == "Rock" and comp_choice == "Scissors") or \
         (player_choice == "Paper" and comp_choice == "Rock") or \
         (player_choice == "Scissors" and comp_choice == "Paper"):
        print("Congrats, you won! Goodbye")
        break
    else:
        print("You lost, try again.")
