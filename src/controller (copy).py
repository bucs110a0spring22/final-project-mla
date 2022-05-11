import pygame
from src import scraping
from src import searchbar 
from src import metabrowser 
# User types search criteria into the search bar and either hits the enter key or presses the search button. The screen then changes to show the results that the web scraper found. 

class Controller: 
  def __init__(self,width=500,height=500):
    self.width = width
    self.height = height
    self.display = pygame.display.set_mode((self.width,self.height))
    self.searchbar = searchbar.Searchbar(0,0,"assets/searchbar.jpg")
    self.state = "run"
    
    
    self.metabrowser = metabrowser.Metabrowser(250,100, "assets/metabrowser.jpg")
    self.gameloop()
    
    

  
    
  def gameloop(self):
    query = str(input("What do you want to search for? "))
    while self.state == "run":
    
   #code for showing text on screen,display text on screen, when the box is clicked, run the scraper
    
      
            
            #move to the result page
      self.display.fill((250,250,250))
      self.display.blit(self.searchbar.image, (0,0))
      font = pygame.font.Font('freesansbold.ttf', 15)
      text = font.render(query, True, 'black')
      self.display.blit(text, (70,140))
      self.display.blit(self.metabrowser.image, (30,10))
      
      pygame.display.flip()


      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.searchbar.rect.collidepoint(event.pos):
            scrape = scraping.Master_Scraper()
            scrape.google_cse_search(query)


            
            # self.display.flip()
            # self.display.blit(self.textboxes.image, (0,0))
            # 
            
        # if event.type == pygame.K_RETURN:
        #   print("scraper")
            # scraping.Master_Scraper(query)
            
            
       
          
      
    