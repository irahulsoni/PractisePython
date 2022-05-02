nums = [7,8,9,10]

for i in range(len(nums)):
    print(nums[i])

# OR
# iter to convert list to iterator
it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())

# OR
print(next(it))

# OR

for i in nums:
    print(i)
