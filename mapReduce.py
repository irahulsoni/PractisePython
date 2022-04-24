# def is_even(a):
#     return a % 2 ==0

lst = [2,3,5,1,6,9,8,10,12,15,17,13,18]

# even = list(filter(is_even, lst))

# Using anonymous function/ lambda
even = list(filter(lambda n: n%2==0, lst))

print(even)



