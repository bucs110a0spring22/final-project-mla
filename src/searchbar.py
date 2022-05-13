import pygame

class Searchbar(pygame.sprite.Sprite):
  def __init__(self,x,y,filename):
    '''
    Initializes data values for the search bar image
    '''
    self.image = pygame.image.load(filename).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y 
    
    



  
    


  

