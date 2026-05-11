import random

money = 10000
staff = 10
for x in range(staff):
    level = random.randint(1, 5)
    if level <= 3:
        salary = 300
    else:
        salary = 500*level
    money -= salary
    if money < 0:
        print(f'Staff {x+1} is {level} should be paid {salary}: Not enough money to pay staff!')
        break
    else:
        print(f"Staff {x+1} is {level} should be paid {salary}. Remaining money: {money}.")