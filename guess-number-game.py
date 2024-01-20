import random

random_number = random.randint(1, 100)

while True:
    user_input = input("what do you think the number is: ")
    user_number = int(user_input)
    if random_number == user_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif random_number < user_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
