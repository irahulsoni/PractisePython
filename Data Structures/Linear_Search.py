# position of number, since we are assuming we haven't found the value yet so we take it as -1, bcs it's returning false as binary
pos = -1

def Search(lis, number):
    #  with while loop

    # i = 0
    # while i in range(len(lis)):
    #     if lis[i] == number:
    #         # since pos is a global variable but calling it in the function will make it local and will not affect its value globally
    #         globals()['pos'] = i
    #         return True
    #     i += 1
    # return False

    for i in lis:
        if i == number:
            globals()['pos'] = lis.index(i)
            return True
    return False


lis = [5, 3, 6, 7, 2, 4, 9, 10, 22, 43]
n = 10

if Search(lis, n):
    print("Found " + str(n) + ' at ' + str(pos + 1))
else:
    print("It's not in the list")
    # lis.append(n)
    # print(lis)
