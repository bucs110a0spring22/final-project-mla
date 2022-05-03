import pygame
from src import scraping
from src import searchbar 
from src import metabrowser 
# User types search criteria into the search bar and either hits the enter key or presses the search button. The screen then changes to show the results that the web scraper found. 

class Controller: 
  def __init__(self,width=500,height=500):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width,self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill(250,250,250) #makes background white, can change later if we want
    self.searchbar = pygame.sprite.Sprite(searchbar.Searchbar(250,250,"assets/searchbar.jpg"))

# Want to get rid of settings button, maybe just search through 1 or 2 browsers? Settings button seems really complicated
# If mouse clicks within search bar rectangle, allow you to type in the search bar
# If mouse clicks search button or the enter key is clicked, the webscraper runs 
    
                              