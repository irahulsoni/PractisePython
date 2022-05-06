# Better than bubble sort
def sort(lis):
    for i in range(5):
        mid = i
        # to reduce the size of unsorted list
        for j in range(i, 6):
            if lis[j] < lis[mid]:
                mid = j

        temp = lis[i]
        lis[i] = lis[mid]
        lis[mid] = temp

        print(lis)


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)
