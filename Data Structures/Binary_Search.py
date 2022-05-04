# faster and better way to do
# we have to make sure the values are sorted

pos = -1

def Search(lis, number):
    lower = 0
    upper = len(lis) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if lis[mid] == number:
            globals()['pos'] = mid
            return True
        else:
            if lis[mid] < number:
                # since we already know it's not the mid-value, so we don't need to check it again
                lower = mid + 1
            else:
                upper = mid - 1
    return False


lis = [4, 0, 6, 8, 1, 2, 3, 10, 18, 44, 17]
number = int(input("Enter number you want to find: "))

if Search(lis, number):
    print('Found at: ' + str(pos))

else:
    print('Not in list')
