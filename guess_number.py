import random


num_random = random.randint(1, 100)

while True:
    num_input = int(input())
    if num_random > num_input:
        print('Ваше число меньше того, что загадано')
    elif num_random < num_input:
        print('Ваше число больше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали число :)')
        break
