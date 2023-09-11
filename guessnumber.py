import random

while True:
    number = input("Take a number upto which you wanna guess: ")
    if number.isdigit():
        if int(number) <= 0:
            print('Please type a number greater than 0')
            continue
        number = int(number)
        break

    else:
        print('Please type a number')
        continue

random_num = random.randint(0, number)
count = 0
while True:
    count += 1
    guess = input("Guess a number? ")
    if guess.isdigit():
        guess = int(guess)

        if guess == random_num:
            print('Correct')
            print(f'You got it correct in {count} guesses. ')
            break
        
        elif guess > random_num:
            print('You guess is above the number, please guess below number')

        else:
            print('Your guess is below the number, please guess above number')
    else:
        print('Your guess is not a number. Please type a number')
        continue

print('Thank you for playing!')


