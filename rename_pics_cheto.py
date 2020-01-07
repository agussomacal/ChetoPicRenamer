# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:40:07 2017

@author: eridanus
"""
import subprocess
import pygame
from pygame.locals import *   #constantes de pygames
import sys
import os
import numpy as np

from rename_pics_cheto_lib import *


if len(sys.argv) == 1:
    print('Asumo que estas en la carpeta de las imagenes a modificar.')
    directory = os.getcwd()
    print(sys.argv)
else:
    directory = sys.argv[1]
photo_files = list(sorted(os.listdir(directory)))


###############################################################################
#                   Constantes, variables previas
###############################################################################

FPS=30

# Size of current screen:
size_pantalla = tuple(map(int, subprocess.check_output(['xrandr']).split('current')[1].split(',')[0].replace(' ', '').split('x')))
pantalla_centro = np.array(size_pantalla)/2

photo_scale = 2.0/3
photo_w = size_pantalla[0] * photo_scale
photo_h = size_pantalla[1] * photo_scale
photo_centro = [pantalla_centro[0] - (size_pantalla[0] - photo_w)/2, 
                pantalla_centro[1] + (size_pantalla[1] - photo_h)/2]

image_name_center = [photo_centro[0], 
                     (photo_centro[1]-photo_w/2)/2]
image_name_size = 72
image_name_color = (0, 50, 200)

text_box_w = size_pantalla[0] - photo_w - (size_pantalla[0]-photo_w)/2
text_box_h = 30
text_box_centro = [photo_centro[0] + photo_w/2 + text_box_w/2,
                   pantalla_centro[1]]

###############################################################################
#                   Functions
###############################################################################
def scaled_screen(size_vect, scale):
    return tuple([int(scale*coord) for coord in size_vect]) 
    
def get_centered_image_rect(image, center):
    half_h = image.get_height()//2
    half_w = image.get_width()//2
    return (center[0]-half_w, center[1]-half_h,
            center[0]+half_w, center[1]+half_h)
            

def get_photo_text(i, name='prb'):
    photo_name = photo_files[i]
    font = pygame.font.SysFont(None, image_name_size)
    format_img = photo_name.split('.')[-1]
    strtext = '{} -> {}.{}'.format(photo_name, name, format_img)
    text = font.render(strtext, True, image_name_color)    
    return text
    

def get_photo(i):
    photo_name = photo_files[i]
    photo = pygame.image.load("{}/{}".format(directory, photo_name))
    photo = pygame.transform.scale(photo, scaled_screen(size_pantalla, photo_scale))
    return photo

###############################################################################
#                   Constantes y cosas del juego
###############################################################################
pygame.init()#siempre antes de usar cualquier funcion de pygames

fpsClock=pygame.time.Clock()

screen = pygame.display.set_mode(size_pantalla, 0, 32)#para definir el tamaño de la ventana
pygame.display.set_caption("Ultra cheto pics manager.")#titulo a la ventana


#________________Musica______________________
#pygame.mixer.music.load("Binary Sunset.mp3")

#_______________Colores______________________
WHITE=(255,255,255)
DARK=(0,0,0)


###############################################################################
#                   El juego en si
###############################################################################

#pygame.mixer.music.play(-1, 0.0)


input_box = InputBox(x=text_box_centro[0], 
                     y=text_box_centro[1], w=text_box_w, 
h=text_box_h, text='write')
    
i = 0 
photo = get_photo(i) 
text = get_photo_text(i) 
while True:#loop principal del juego

    screen.fill(DARK) 

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()#sale de pygame
            sys.exit()#sale del programa

        input_box.handle_event(event)
        input_box.update()
        
        #_______________Imagenes_____________________
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and i < len(photo_files)-1:
                i += 1
            elif event.key == K_LEFT and i > 0:
                i -=1
            photo = get_photo(i) 
            text = get_photo_text(i, input_box.text)
            
    screen.blit(photo, get_centered_image_rect(photo, photo_centro))#photo.get_rect())
    screen.blit(text, get_centered_image_rect(text, image_name_center))            
    input_box.draw(screen)    
    
    pygame.display.update()
    fpsClock.tick(FPS)
    
    





























