import random

number = random.randrange(100)

print (f"Guess the number!")

while True:
    guess = input ("Please input your guess.")
    try:
        guess_num = int(guess)
    except:
        print ("Inpyt Number:")
        continue

    if guess_num < number:
        print ("Too small!")
    elif guess_num > number:
        print ("Too big!")
    else:
        print ("You win!")
        break

