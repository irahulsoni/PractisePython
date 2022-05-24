# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").upper()
name2 = input("What is their name? \n").upper()
# 🚨 Don't change the code above 👆

count1 = 0
count2 = 0
for n in name1 + name2:
    if n in ['T', 'R', 'U', 'E']:
        count1 += 1

for m in name1 + name2:
    if m in ['L', 'O', 'V', 'E']:
        count2 += 1

l = [str(count1), str(count2)]

total = ''.join(l)

if int(total) <= 10 or int(total) >= 90:
    print('Your score is ' + total + ', you go together like coke and mentos.')
elif 40 <= int(total) <= 50:
    print('Your score is ' + total + ', you are alright together.')
else:
    print('Your score is ' + total + '.')
