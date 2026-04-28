import random

num = random.randint(1, 100)
flag = True
chance_cost = 0
while flag:
    guess = int(input("Please enter your guess (1-100): "))
    chance_cost += 1
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {num} in {chance_cost} attempts!")
        flag = False