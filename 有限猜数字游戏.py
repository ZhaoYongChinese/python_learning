import random

num = random.randint(1, 100)
chance = 5
print("Welcome to the Number Guessing Game!")
chance_now = 0
while chance_now < chance:
    guess = int(input("Please enter your guess (1-100): "))
    chance_now += 1
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {num} in {chance_now} attempts!")
        break
else:
    print(f"Game over! You've used all {chance} chances. The number was {num}.")