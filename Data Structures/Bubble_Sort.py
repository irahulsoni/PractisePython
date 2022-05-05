# swapping the values. Check if number ahead is greater than number before and keep bringing the highest number in the last with every iteration
def sort(lis):
    # Setting the range  to go from index number [-1] to the last number[0] and going in negative order so [-1]
    for i in range(len(lis)-1, 0, -1):
        # now every time the number of iteration will go 1 down as with every iteration the greatest number comes to the end
        # So we do until i that is number of elements in list and as it's a loop it automatically deducts the iteration
        for j in range(i):
            if lis[j] > lis[j+1]:
                temp = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = temp


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)
