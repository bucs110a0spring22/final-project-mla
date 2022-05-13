import pygame
from src import masterscraper
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
    
    
  #https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
  def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    
  def gameloop(self):
    query = input("What do you want to search for? ")
    while self.state == "run":
      self.display.fill((250,250,250))
      self.display.blit(self.searchbar.image, (0,0))
      font = pygame.font.Font('freesansbold.ttf', 15)
      text = font.render(query, True, 'black')
      self.display.blit(text, (70,140))
      self.display.blit(self.metabrowser.image, (30,10))
      pygame.display.flip()
      result_text = ''
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.searchbar.rect.collidepoint(event.pos):
            print('beforeScraping')
            for scrape in [masterscraper.Googlescraper(), masterscraper.Bingscraper()]:
              result_filename = query + scrape.search_engine() + "results" + ".txt"
              search_results = scrape.search(query)
              scrape.save_results(search_results, result_filename)
              result_file_handle = open(result_filename, "r")
              search_t += f'{scrape.search_engine()} Result: \n{result_file_handle.read()}'

      pygame.display.update()
      font = pygame.font.SysFont('Arial', 4)
      self.blit_text(self.display, result_text, (0, 150), font)
              
              
                           
            '''scrape = masterscraper.Masterscraper()
            google_search_results = scrape.google_cse_search(query)
            google_result_filename = query + "google" + "results" + ".txt"
            scrape.google_save_results(google_search_results, google_result_filename)    
            bing_search_results = scrape.bing_search(query)
            bing_result_filename = query + "bing" + "results" + ".txt"
            scrape.bing_save_results(bing_search_results, bing_result_filename)'''
            
            
            
            
          


            
        
            
            
       
          
      
    