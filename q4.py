'''
Q4. Call factorial function using thread.
'''

from threading import *
from time import *
from math import *
def displayFactorial(l1):
    print('Displaying factorial of all elements of the list with delay: ')
    
    for i in range(len(l1)):
        print("The factorial of {} = {}".format(l1[i],factorial(l1[i])))
        sleep(3)
        
l1=[1,2,3,4,5,6]
print('The complete list is as follows:\n{}'.format(l1))
t=Thread(target=displayFactorial,args=(l1,))
t.start()
t.join()
print('Program End')
