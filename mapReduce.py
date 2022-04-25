# def is_even(a):
#     return a % 2 ==0

#to use reduce we need functools because this function ins in this class
from functools import reduce

lst = [2,3,5,1,6,9,8,10,12,15,17,13,18]

# even = list(filter(is_even, lst))

# Using anonymous function/ lambda
even = list(filter(lambda n: n%2==0, lst))

# Using map function

double = list(map(lambda n: n*2 ,even))

# Using reduce: Used to get one value like add, average

sum = reduce(lambda a,b : a+b, lst )

avg = reduce(lambda a,b : a+b/2, lst)


print(even)
print(double)
print(sum)
print(avg)



