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
n = 10  #length of list
distance = screen_width/n
width = distance - 1
list = [randint(1, screen_height) for p in range(0, n)]
list_sorted = sorted(list)
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
generate_list_button = button(white, 400,screen_height+70,100,20,'Generate')
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
    generate_list_button.draw(screen)
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
                list = [randint(1, screen_height) for p in range(0, n)]
                list_sorted = sorted(list)
                a = ''
            if length_down_button.isOver(pos) and n>2:
                n -= 1
                distance = screen_width/n
                width = distance - 1
                list = [randint(1, screen_height) for p in range(0, n)]
                list_sorted = sorted(list)
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
            if generate_list_button.isOver(pos):
                list = [randint(1, screen_height) for p in range(0, n)]
                list_sorted = sorted(list)
                a = ''
            if stop_button.isOver(pos):
                a = ''

    
    if(a == 'buble'):
        
        for i in range(len(list)):
            if i == j-1 or i == j:
                pygame.draw.rect(screen, blue, pygame.Rect(i * distance, y, width, -list[i]))
          
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -list[i]))

        if list[j-1] > list[j]:
            pygame.draw.rect(screen, red, pygame.Rect(j * distance, y, width, -list[j]))
            pygame.draw.rect(screen, red, pygame.Rect((j-1) * distance, y, width, -list[j-1]))

            list[j-1], list[j] = list[j], list[j-1]
        
        j += 1
        print(k)
        if j == len(list)-k:
            j = 1  
            k+=1
        if(list == list_sorted):
            a = ''
    
    elif a == 'insert':

        for i in range(len(list)):
            if(i == j or i == j-1):
                pygame.draw.rect(screen, blue, pygame.Rect(i * distance, y, width, -list[i]))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -list[i]))
       
        if j > 0 and list[j-1] >list[j]:
            pygame.draw.rect(screen, red, pygame.Rect(j * distance, y, width, -list[j]))
            pygame.draw.rect(screen, red, pygame.Rect((j-1) * distance, y, width, -list[j-1]))
            list[j-1], list[j] = list[j], list[j-1]
        j-=1
        if j == 0:
            k+=1
            j = k
      
        if j == len(list):
            j = 1
        if(list == list_sorted):
            a = ''

    elif a == 'choise':

        for i in range(len(list)):
            if(i == j):
                pygame.draw.rect(screen, blue, pygame.Rect(i * distance, y, width, -list[i]))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -list[i]))
        
        if(list[j]<list[k]):
            pygame.draw.rect(screen, red, pygame.Rect(j * distance, y, width, -list[j]))
            pygame.draw.rect(screen, red, pygame.Rect((k) * distance, y, width, -list[k]))
            list[k], list[j] = list[j], list[k]
        
        j+= 1
        
        if j == len(list):
            k+=1
            j = k
        if(list == list_sorted):
            a = ''

    else:
         for i in range(len(list)):
             pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -list[i]))
   
   
   
    pygame.display.flip()
    clock.tick(fps)