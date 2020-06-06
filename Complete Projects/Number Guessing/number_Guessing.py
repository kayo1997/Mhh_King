import random

username = input("Please Enter Your Name: ")
print('Welcome', username)
user_number = input('Guess a Number from 0 - 100: ')

number = random.randint(0, 100)

if user_number is username:
    print('Yaay! You Won!')
else:
    print('Ouch! Try Again')
