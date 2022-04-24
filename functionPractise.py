
#Simple way of passing value to function:
# def person(name,age,address,number):
#     print(name)
#     print(age)
#     print(address)
#     print(number)

# Better way than rihghting multiple variablrs:
# Using * means the variable can accept different values, can be useful in addition subtaction when we don't know about total input numbers
# Use ** when passing variable with the argument eg as follows

sumthing = 10
def person(name, **data):
    print(name)
    print(data)

# To print key and value without displaying in tuple, use items function
    for i,j in data.items():
        print(i,j)

    #Local variable even though it has the same name outside as global
    sumthing = 12
    #to change the value of global variable without changing the local value
    x = globals()['sumthing']
    globals()['sumthing'] = 11

# person('rahul',27,'Montreal',438)
person('rahul',age=27,city='Montreal',phone=438)


# in Python functions are also objects and functions that we are only using once we can do like

f = lambda a : a* a
result = f(5)
print(result)
