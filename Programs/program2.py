import random

print('I am thinking of a number betweem 1 to 20.')
secret_number = random.randint(1,20)

for guess_taken in range(1,6):
    print('Take a guess')
    user_input = int(input())

    if user_input < secret_number:
        print('YOur guess is too low')
    elif user_input > secret_number:
        print('Your guess is too high')
    else:
        break
if user_input == secret_number:
    print('Good job! You have guessed it corretly. ', end='')
    print('You have guessed my number in ' + str(guess_taken) + ' guesses.')
else:
    print('Nope! The number I was thinking of was ' + str(secret_number))
