#Function calling itself for n number of times
import sys
sys.setrecursionlimit(2000)

i = 0
def greet():
    global  i
    print("Hello ", i)
    i +=1
    greet()

greet()


print(sys.getrecursionlimit())

