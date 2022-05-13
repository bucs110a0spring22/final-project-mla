import pygame

class Metabrowser(pygame.sprite.Sprite):
  def __init__(self, x, y, filename):
    '''
    Initializes data values for the metabrowser image
    '''
    self.image = pygame.image.load(filename).convert_alpha()
    self.image = pygame.transform.scale(self.image, (400, 100))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y 
  