import pygame

class Searchbar(pygame.sprite.Sprite):
  def __init__(self,x,y,filenames):
    super()
    self.image_set = [pygame.image.load(file_name) for f in filenames]
    self.current_image = 0
    self.image = self.image_set[self.current_image]
    self.rect = self.image.get_rect
    self.rect.x = x
    self.rect.y = y 
    
    


  def Click(self):
    '''
    When clicking in the searchbar, a cursor appears and allows you to type
    '''
    if self.collides(click):
      #switch the background that shows the result
  def type(self):
    '''
    Allows user to type in the search bar
    '''
    for key in keys: 
      # use a separate if statement for each key? thinking there is a better way to do it
  
    


  

