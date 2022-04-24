lst = [10,12,11,14,13,15,31,16,11]

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0 :
            even +=1
        else:
            odd += 1
    return even,odd

even,odd = count(lst)
print('even :  {} ,odd : {}'.format(even,odd))

lst1 = ['naveen','rahul','ted','hex','Poonam','Arpit']
def moreFive(lst1):

    total = 0
    for i in lst1:
        if len(i)>= 5:
            total +=1

    return total

totalFive = moreFive(lst1)
print("Total names more than 5 characters: {}".format(totalFive))
