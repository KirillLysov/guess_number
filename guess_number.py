import random

# Комментарий 2

num_random = random.randint(1, 1000)

while True:
    num_input = int(input())
    if num_random > num_input:
        print('Твое число меньше того, что загадано')
    elif num_random < num_input:
        print('Твое число больше того, что загадано')
    else:
        print('Отличная интуиция! Ты угадал число :)')
        break
