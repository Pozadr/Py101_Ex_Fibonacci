def fib_iter1(n):
    '''
        Function print on console screen Fibonacci sequence
        from 0 to n. 'While' loop version.

    '''
    print('\n1st solution - ''while loop.')
    a, b = 0, 1
    print('Number ', 1, ': ', a)
    i = 2
    while n > 1:
        print ('Number ', i, ': ', b)
        a, b  =  b, a + b  # multiple assignment
        n -= 1
        i += 1
    return 0
        
def fib_iter2(n):
    '''
        Function print on console screen Fibonacci sequence
        from 0 to n. 'For' loop version.        

    '''

    print('\n2nd solution - ''for loop.')    
    a, b = 0, 1
    print('Number ', 1, ': ', a)
    print('Number ', 2, ': ', b)
    for i in range(1, n - 1):
        a, b = b, a + b
        print('Number ', i + 2, ': ', b)
        
    print()  # new line '\n' 
    return 0
    

def fib_recursion(n):
    '''
        Function print on console screen Fibonacci sequence
        from 0 to n. Recursion version.        

    '''

    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


def main(args):
    while True:
        try:
            n = int(input('How many numbers of Fibonacci sequence to print? '))
            break
        except ValueError:
            print('Wrong input data. Try again.')
            continue
        
    fib_iter1(n)
    print()
    print('=' * 40)
    
    fib_iter2(n)
    print()
    print('=' * 40)
    
    print('\n3rd solution - recursion.')    
    print('Number', n, ': ', fib_recursion(n - 1))
    return 0

# Program begins in main function.
# If you run program as main file '__name__' will be written by '__main__'. Code will run after start.
# If you run program as module '__name__' will be written by '_file_name__'('__Lotto__').
# Code will not run after start. You need to call a function.    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
