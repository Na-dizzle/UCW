import random
print("Choose an option")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
choices = ["Rock", "Paper", "Scissors"]
outcome_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
player_wins = computer_wins = 0

for _ in range(30):  # Limit to prevent infinite looping
    if max(player_wins, computer_wins) >= 2:
        break
    
    try:
        player_choice_input = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
        if not player_choice_input.isdigit():
            raise ValueError
        player_choice_num = int(player_choice_input)
        if player_choice_num not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        continue
    
    player_choice = choices[player_choice_num - 1]
    computer_choice_num = random.randint(1, 3)
    computer_choice = choices[computer_choice_num - 1]
    
    print(f"You chose {player_choice.lower()}, the computer chose {computer_choice.lower()}.")
    
    result = outcome_matrix[player_choice_num - 1][computer_choice_num - 1]
    player_wins += result == 1
    computer_wins += result == -1
    print("It's a tie!" if result == 0 else "Congrats, you won!" if result == 1 else "You lost.")
    print(f"Human: {player_wins} Computer: {computer_wins}")

print("Goodbye!")

