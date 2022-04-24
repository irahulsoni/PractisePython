#Add 2 numbers to get the next and so on:
#0 1 1 2 3 5 8 13.....
# take last number and current gives next number

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n <= 0:
        print("Number should be 1 or more")

    elif n >0 and n <= 12:
        print(a)
        print(b)
        #since we are already printing 1st and 2nd number ton left over is 3rd and so on
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

    else:
        print("Enter number between 1 and 12")

fib(int(input("Enter a number: ")))
