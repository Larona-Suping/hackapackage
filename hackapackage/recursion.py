def sum_array(array):

    '''Return sum of all items in array'''
    sum_ = 0
    for item in array:
        sum_ = sum_ + item
    return sum_


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <= 0:
        print('Enter digit greater than 0')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n < 0:
        print('Enter n that is either 0 or greater')
    elif n == 0 or n == 1:
        return 1
    elif n == 2:
        return n * (n-1)
    else:
        return n * factorial(n-1)

def reverse(word):
    n = len(word)
    if n == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]

        
