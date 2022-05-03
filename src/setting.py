import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0,0,0)

class Settingicon:
  def __init__(self, x, y, filename):
    self.image = pygame.image.load("filesname")
    self.rect = self.image.get_rect()


class Dafaultbrowser:
  #click

  #setting page appears
    
  #default browser
    #only one of the browsers can be chosen - if one button is clicked, switch to that
    
  #comparison browser
    #the option you choose as default becomes not an option here
    #at most two browsers can be chosen
    #error message when more than two are chosen
  #comparison language
  

  #when none is chosen, the message that says you need to choose something appears
  #once one option is chosen, the checkbox is checked

  #when the exit button is clicked, the setting page disappears


def main():
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  # clock = pygame.time.Clock()
  settingicon = Settingicon()
  
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      
      screen.blit(settingicon.image, settingicon.rect)
     





