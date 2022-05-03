# We import thread from threading to create more threads other than just main thread
from threading import *
# Sleep methord is used to slow down the
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

t1 = hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

# Having main thread performing it's action in the last

t1.join()
t2.join()

print("Bye")
