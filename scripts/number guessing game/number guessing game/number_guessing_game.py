import random

print('Welcome to the number guessing game')


def max_range():
    while True:
        n = input('\nMaximum number? ')
        if not n.isdigit() or int(n) < 1:
            print('Please enter an integer greater than zero!')
            continue
        return int(n)


q = max_range()
secret = random.randint(1, q)


def get_num():
    while True:
        num = input(f'Enter a number from 1 to {q}: ')
        if not num.isdigit() or not (1 <= int(num) <= q):
            print(f'Maybe we should enter an integer from 1 to {q}?')
            continue
        return int(num)


def game():
    x, total = 0, 1
    while x != secret:
        x = get_num()
        if x > secret:
            print('Your number is greater than the secret number, try again')
            total += 1
            continue
        elif x < secret:
            print('Your number is less than the secret number, try again')
            total += 1
            continue
    print('You guessed it, congratulations!')
    print('Number of attempts: ' + str(total))


while True:
    game()
    print('Great game, another round?')
    ans = input('Yes(Y) if you want to continue: ')
    if ans.lower() in ('y', 'yes'):
        q = max_range()
        secret = random.randint(1, q)
        continue
    else:
        break

print('Thank you for playing the number guessing game. See you again...')
