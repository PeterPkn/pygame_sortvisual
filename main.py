import pygame
from pygame.locals import *
import random
import time
from datetime import datetime


WIDTH = 1300
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

starttime = datetime.now()

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quicksort")
clock = pygame.time.Clock()     ## For syncing the FPS

font = pygame.font.Font('freesansbold.ttf', 32)
compares = 0


#ARRAY to sort
length = 200
sortingArray = list(range(0,length))
for idx,elem in enumerate(sortingArray):
    sortingArray[idx] = random.random()*100

#print(sortingArray)

def swapElem(idx1, idx2, array):
    elem1 = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = elem1

def drawArray(array):
    
    rectWidth = WIDTH / len(array)
    margin = rectWidth/10

    for idx, elem in enumerate(array):
        pygame.draw.rect(screen, BLUE, pygame.Rect(idx*rectWidth+margin,HEIGHT,rectWidth-2*margin,-elem*4))


## group all the sprites together for ease of update
#all_sprites = pygame.sprite.Group()

def sorted(array):
    index = 0
    while index+1<len(array):
        if(array[index]>array[index+1]):
            return False
        index+=1
    return True



def quickSort(array, low, high):
    if low<high:
        pi = partition(array, low, high)

        quickSort(array,low, pi-1)
        quickSort(array, pi+1, high)

def partition(array, low, high):
    global compares
    pivot = array[high]
    small = low-1
    index = low
    while index <= high:
        
        if array[index]<pivot:
            small+=1
            swapElem(index, small, array)

        index+=1

        compares+=1
        
        screen.fill(WHITE)
        drawArray(sortingArray)

        text = font.render("Comps: "+str(compares)+" Time=" + str(datetime.now()-starttime), True, GREEN, BLUE)
        textRect = text.get_rect() 
        textRect.center = (300, 20)
        screen.blit(text, textRect) 

        pygame.display.flip()

        for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
    
    swapElem(small+1,high,array)
    return small+1

#quickSort(sortingArray,0,len(sortingArray)-1)

#print(sortingArray)


index = 0

## Game loop
running = True
while running:

    #BUBBLE SORT

    # print(index)
    # print(len(sortingArray))
    # if(index+1>=len(sortingArray)):
    #     index = 0

    # if(sortingArray[index]>sortingArray[index+1]):
    #     compares+=1
    #     swapElem(index, index+1, sortingArray)
    

    
    #index += 1

    #QUICK SORT

    quickSort(sortingArray,0,len(sortingArray)-1)

    if(sorted(sortingArray)):
        f = open("compStats.txt", "a")
        #f.write(str(compares)+" ")
        f.close()
        #time.sleep(2)
        compares = 0
        # sortingArray = list(range(0,length))
        # for idx,elem in enumerate(sortingArray):
        #     sortingArray[idx] = random.random()*100


    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False


    #2 Update
    #all_sprites.update()


    #3 Draw/render
    screen.fill(WHITE)

    text = font.render(str(compares), True, GREEN, BLUE)
    textRect = text.get_rect() 
    textRect.center = (50, 50)
    screen.blit(text, textRect) 

    drawArray(sortingArray)

    

    #all_sprites.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
