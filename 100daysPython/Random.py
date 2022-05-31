# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random as r
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
r.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.
# #Write the rest of your code below this line 👇

result = r.randint(0, 1)
if result == 1:
    print("Heads")
else:
    print('Tails')
