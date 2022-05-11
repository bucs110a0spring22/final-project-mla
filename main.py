import pygame
from src import controller

#import your controller

def main():
    pygame.init()
    controller.Controller()
    
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
__name__ = '__main__'
if __name__ == '__main__':

    main()

