'''The guess game '''

secret_num = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter Guess: "))
    guess_count += 1
    if guess == secret_num:
        print("You won!")
        break
else:
    print("You failed. Only 3 guesses are allowed")

