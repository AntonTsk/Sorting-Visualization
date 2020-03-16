import pygame

import sys
from random import randint
from button import *

pygame.init()

screen_width, screen_height = 1024, 720
screen = pygame.display.set_mode((screen_width, screen_height+180))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30)
run = True
y = screen_height 
fps = 5
n = 10  #length of arr
distance = screen_width/n
width = distance - 1
arr = [randint(1, screen_height) for p in range(0, n)]
arr_sorted = sorted(arr)
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)


# Buttons
speed_up_button = button(white, 110,screen_height+60,50,20,'Up')
speed_down_button = button(white, 110,screen_height+120,50,20,'Down')
length_up_button = button(white, 265,screen_height+60,50,20,'+')
length_down_button = button(white, 265,screen_height+120,50,20,'-')
generate_arr_button = button(white, 400,screen_height+70,100,20,'Generate')
stop_button = button(white, 400,screen_height+100,100,20,'Stop')
bubble_sort_button = button(white,600,screen_height+40,100,20,'Bubble Sort')
insert_sort_button = button(white,600,screen_height+70,100,20,'Insert Sort')
choise_sort_button = button(white, 600,screen_height+100,100,20,'Choise Sort')










def massage_to_screen(msg, color, msg_width, msg_height):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [msg_width, msg_height])



a = ''
while run:
    
    screen.fill((0, 0, 0))
    
    massage_to_screen('Speed: '+str(fps), white, 50,screen_height+90)
    massage_to_screen('Length: '+str(n), white, 200,screen_height+90)

    
    speed_up_button.draw(screen)
    speed_down_button.draw(screen)
    length_up_button.draw(screen)
    length_down_button.draw(screen)
    bubble_sort_button.draw(screen)
    generate_arr_button.draw(screen)
    stop_button.draw(screen)
    insert_sort_button.draw(screen)
    choise_sort_button.draw(screen)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if speed_up_button.isOver(pos) and fps < 99:
                fps +=1
            if speed_down_button.isOver(pos) and fps>1:
                fps -= 1
            if length_up_button.isOver(pos) and n <1000:
                n+=1
                distance = screen_width/n
                width = distance - 1
                arr = [randint(1, screen_height) for p in range(0, n)]
                arr_sorted = sorted(arr)
                a = ''
            if length_down_button.isOver(pos) and n>2:
                n -= 1
                distance = screen_width/n
                width = distance - 1
                arr = [randint(1, screen_height) for p in range(0, n)]
                arr_sorted = sorted(arr)
                a = ''
            if bubble_sort_button.isOver(pos):
                a = 'buble'
                j = 1
                k = 0
            if(insert_sort_button.isOver(pos)):
                a = 'insert'
                j = 1 
                k = 0
            if(choise_sort_button.isOver(pos)):
                a = 'choise'
                j = 1 
                k = 0
            
            if generate_arr_button.isOver(pos):
                arr = [randint(1, screen_height) for p in range(0, n)]
                arr_sorted = sorted(arr)
                a = ''
            if stop_button.isOver(pos):
                a = ''

    
    if(a == 'buble'):
        
        for i in range(len(arr)):
            if i == j-1 or i == j:
                pygame.draw.rect(screen, blue, pygame.Rect(i * distance, y, width, -arr[i]))
          
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -arr[i]))

        if arr[j-1] > arr[j]:
            pygame.draw.rect(screen, red, pygame.Rect(j * distance, y, width, -arr[j]))
            pygame.draw.rect(screen, red, pygame.Rect((j-1) * distance, y, width, -arr[j-1]))

            arr[j-1], arr[j] = arr[j], arr[j-1]
        
        j += 1
        if j == len(arr)-k:
            j = 1  
            k+=1
        if(arr == arr_sorted):
            a = ''
    
    elif a == 'insert':

        for i in range(len(arr)):
            if(i == j or i == j-1):
                pygame.draw.rect(screen, blue, pygame.Rect(i * distance, y, width, -arr[i]))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -arr[i]))
        b = False
        if j > 0 and arr[j-1] >arr[j]:
            pygame.draw.rect(screen, red, pygame.Rect(j * distance, y, width, -arr[j]))
            pygame.draw.rect(screen, red, pygame.Rect((j-1) * distance, y, width, -arr[j-1]))
            arr[j-1], arr[j] = arr[j], arr[j-1]
            b = True
        j-=1
        if j == 0 or b == False:
            k+=1
            j = k
      
        if j == len(arr):
            j = 1
        if(arr == arr_sorted):
            a = ''

    elif a == 'choise':

        for i in range(len(arr)):
            if(i == j):
                pygame.draw.rect(screen, blue, pygame.Rect(i * distance, y, width, -arr[i]))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -arr[i]))
        
        if(arr[j]<arr[k]):
            pygame.draw.rect(screen, red, pygame.Rect(j * distance, y, width, -arr[j]))
            pygame.draw.rect(screen, red, pygame.Rect((k) * distance, y, width, -arr[k]))
            arr[k], arr[j] = arr[j], arr[k]
        
        j+= 1
        
        if j == len(arr):
            k+=1
            j = k
        if(arr == arr_sorted):
            a = ''
    elif(a == 'merge'):
        pass

    else:
         for i in range(len(arr)):
             pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -arr[i]))
   
   
   
    pygame.display.flip()
    clock.tick(fps)