'''
Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between
'''
from threading import *
from time import *
def display():
    print('Print 1-10 in interval of 1 second')
    for i in range(1,11):
        sleep(1)
        print(i)

t=Thread(target=display)
t.start()
