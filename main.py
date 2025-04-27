import random

print("Welcome to the Guessing Game.")
attempts = 0
while attempts == 0:
    diff = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if diff == "easy":
        attempts = 10
        break
    if diff == "hard":
        attempts = 5
        break
    else:
        print("You wrote something wrong. Try Again\n")

game = True
num = random.randint(1, 100)
while game:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > num:
        print("Too high.")
        attempts -= 1
    if guess < num:
        print("Too low")
        attempts -= 1
    if guess == num:
        print("Congrats, you win.")
        exit()
    if attempts == 0:
        print("No more attempts. You lose.")
        exit()





