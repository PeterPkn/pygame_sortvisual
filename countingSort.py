import random
from datetime import datetime
import sys


sys.setrecursionlimit(4000)

length = 20000
sortingArray = [0]*length
for idx,elem in enumerate(sortingArray):
    sortingArray[idx] = random.randint(0,9)

#print(sortingArray)

def swapElem(idx1, idx2, array):
    elem1 = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = elem1

def quickSort(array, low, high):
    if low<high:
        pi = partition(array, low, high)

        quickSort(array,low, pi-1)
        quickSort(array, pi+1, high)

def partition(array, low, high):
    
    pivot = array[high]
    small = low-1
    index = low
    while index <= high:
        
        if array[index]<pivot:
            small+=1
            swapElem(index, small, array)

        index+=1
    swapElem(small+1,high,array)
    return small+1


def countingSort(array):
    numCount = [0]*len(array)

    for elem in array:
        numCount[elem] += 1
    
    array = []
    
    for idx,elem in enumerate(numCount):
        for x in range(0,elem):
            #print("X "+str(x)+ " idx " + str(idx)+ " elem "+str(elem))
            array.append(idx)
    #print(array)

    return array


def sorted(array):
    index = 0
    while index+1<len(array):
        if(array[index]>array[index+1]):
            return False
        index+=1
    return True

print("start")
start = datetime.now()

sortingArray = countingSort(sortingArray)
#quickSort(sortingArray,0,len(sortingArray)-1)
done = datetime.now()-start
print("END")
print("Time taken: " + str(done))


print(sorted(sortingArray))
