#!/usr/bin/python
import pygame
import sys
from pygame.locals import K_ESCAPE, KEYDOWN
from colors import *
from time import sleep, time

def main():
    # Read image data
    img1 = []
    img2 = []
    y_iterate = 0
    with open('Stego_3.txt', 'rw') as fread:
        for x in fread:
            img1.append(x.strip('\n'))
    
    for y1 in img1:
        img2.append(y1.split())
   
    for zzz in img2:
        print(zzz) 
   
    # Make for size of image per the file data 444x299 
    window_size=window_width, window_height=444,299
    surface=pygame.display.set_mode(window_size,pygame.RESIZABLE)
    #surface.fill(black)
    FPS = 60
    frames = FPS / 6
    clock = pygame.time.Clock()
    yo_count = 0
    val_x = 0
    val_y = 0

    while(True):

        '''for qq in range(1,299):
            for qq2 in range(1,444):
                if img2[qq2][3] == 'white':
                    print("[{0},{1}] white {2}".format(qq2, qq, img2[qq][3]))
                    pygame.draw.rect(surface, white, (qq2, qq, 1, 1))
                elif img2[qq2][3] != 'white':
                    pygame.draw.rect(surface, black, (qq2, qq, 1, 1))
                    print("[{0},{1}] black {2}".format(qq2, qq, img2[qq][3]))
                else:
                    print("not sure...")'''

        for yo in img2:
            if img2[yo_count][3] == 'white':
                pp = str("{}".format(img2[yo_count][0]))
                pp2 = pp.strip(':')
                val_x, val_y = pp2.split(',')
                pygame.draw.rect(surface, white, (int(val_x), int(val_y), 1, 1))
            else:
                pp3 = str("{}".format(img2[yo_count][0]))
                pp4 = pp3.strip(':')
                val_x, val_y = pp4.split(',')
                pygame.draw.rect(surface, black, (int(val_x), int(val_y), 1, 1))
            yo_count+=1

        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    sys.exit()

        pygame.display.update()
        clock.tick(FPS)
        yo_count = 0

if __name__ == '__main__':
    main()
