import random
from datetime import datetime


length = 100000000
sortingArray = list(range(0,length))
for idx,elem in enumerate(sortingArray):
    sortingArray[idx] = random.randint(0,9)

#print(sortingArray)



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
done = datetime.now()-start
print("END")
print("Time taken: " + str(done))


print(sorted(sortingArray))
