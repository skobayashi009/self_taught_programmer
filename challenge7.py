ans = [8, 9]

print('')
print('This is a guessing game.')
print('')
print('If you want to quit, type "q".')

while True:
    n = input('Put an any integer less than 10.')
    if n == 'q':
        break
    try:
        if int(n) in ans:
            print('You win')
            break
        print('Wrong number!')
        print('')
    except:
        print('Put an INTEGER!!')
        print('')

