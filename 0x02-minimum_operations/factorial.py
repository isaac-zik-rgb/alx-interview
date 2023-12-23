def factorial(n):
    if (n <= 1):
        return n
    i = 1
    j =1
    while (i <= n):
        j *= i 
        i +=1
    print(j)

factorial(7)