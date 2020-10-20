#rock, paper, scissors game. You play against a computer

import random
import os
import time


def converted(number):
    if number == 1:
        return 'rock'
    elif number == 2: 
        return 'paper'
    elif number == 3:
        return 'scissor'


Outcomes = {
    'rock': {'rock': 'draw', 'paper': 'lost', 'scissor': 'won'},
    'paper': {'rock': 'won', 'paper': 'draw', 'scissor': 'lost'},
    'scissor': {'rock': 'lost', 'paper': 'won', 'scissor': 'draw'}
}

Mylist = ['rock', 'paper', 'scissor']
while True:
    os.system('cls||clear')
    Bot_choice = random.choice(Mylist)
    print("Let's play ROCK PAPER SCISSOR\n\nChoose your option\n1)ROCK\n2)PAPER\n3)SCISSOR\n")

    try:
        user_choice = int(input("Enter your choice {1,2,3}=>"))
        Converted_userchoice = converted(user_choice)
        print('\n======Result======\n')
        print('==>', Outcomes[Converted_userchoice][Bot_choice], '<==')
        print('\nYour Choice:', Converted_userchoice)
        print('\nComputer Choice:', Bot_choice)
        print("========================================")
        print('please wait a few seconds, after it will automatically restart')
        time.sleep(1)
    except:
        print('Invalid arguments')
        print("please use Numeric values between 1 to 3")
        print('\nplz wait for 3 sec after it will automatically restart')
        time.sleep(3)
