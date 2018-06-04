'''
Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
Delay goes like 2sec-4sec-6sec-8sec-10sec
'''

from threading import *
from time import *
def displayListElements(l1):
    print('Displaying all elements of the list with delay: ')
    j=0
    for i in range(2,11,2):
        print(l1[j])
        print('Going to sleep for {} seconds'.format(i))
        sleep(i)
        j+=1
        
l1=['apple','samsung','nokia','mi','motorola']
print('The complete list is as follows:\n{}'.format(l1))
t=Thread(target=displayListElements,args=(l1,))
t.start()
t.join()
print('Program End')
