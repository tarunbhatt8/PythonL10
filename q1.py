'''
Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
'''
from threading import *
import time
def display():
    print('Starting Process...And waiting for 5 seconds\n')
    time.sleep(5)
    print('5 seconds are up.. Process End')

print('Starting Main Thread\n')
t=Thread(target=display)
t.start()
t.join()
print('Back in Main thread')
