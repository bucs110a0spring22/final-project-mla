https://stackoverflow.com/questions/38635419/searching-in-google-with-python
https://www.geeksforgeeks.org/performing-google-search-using-python-code/
https://developpaper.com/question/how-does-python-get-the-real-url-of-baidu-search-results/
https://github.com/Yhinner/SinaWeiboScraper

from urllib.request import urlopen
from bs4 import BeautifulSoup
from googlesearch import search

class Master_Scraper
  def Google_Scraper(query, language)
    '''if import fails'''
    except ImportError:
      print("No module named 'google' found")
    '''search'''
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
  def Yahoo_Scraper(query):
    '''similar to google'''
    
  def Bing_Scraper(query):
    '''similar to google'''
  def Naver_Scraper(query):
    '''use SerpAPI'''
  def Baidu_Scraper(query):
    '''harder because they encrypt URLs and don't have an API. need to use a '''