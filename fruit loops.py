import random
while True:
    print("Hello!")
    quit = input("Want to quit? Enter Y or N: ")
    if quit == "Y" or quit == "y":
        break

print("Goodbye!")
  

while True:
    roll = random.randint(1, 6)  
    print("You rolled . . .", roll)

    redo = input("Want to roll again? Enter Y or N: ")  
    if redo == "Y" or redo == "y":  
        continue  
    else:
        break  

print("Goodbye!")  



rollst = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


for _ in range(600):
    roll = random.randint(1, 6)
    rollst[roll] += 1


for side in range(1, 7):
    count = rollst[side]
    percentage = count / 600
    print(f"Num of times {side} was rolled {count}")
    print(f"Percentage is {percentage}")

print("Goodbye!")
