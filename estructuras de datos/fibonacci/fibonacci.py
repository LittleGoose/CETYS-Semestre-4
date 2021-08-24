def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return(fibonacci_sequence(n-1)+fibonacci_sequence(n-2))  

#n = int(input("enter a number: "))
n=2

if n == 0:
    print('0')
else:
    print('Fibonacci sequence:')
    for i in range(n):
        print(fibonacci_sequence(i))