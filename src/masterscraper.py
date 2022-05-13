# https://stackoverflow.com/questions/38635419/searching-in-google-with-python
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
# https://developpaper.com/question/how-does-python-get-the-real-url-of-baidu-search-results/
# https://github.com/Yhinner/SinaWeiboScraper

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# from googlesearch import search
import requests
import pprint


class Basescraper(object):
  def __init__(self):
    pass

  def search(self, query):
    pass

  def save_results(self, results, filename):
    pass

  def search_engine(self):
    pass

  # def process_results(self, results):
  #   pass

class Googlescraper(Basescraper):
  def __init__(self, api_key="AIzaSyAk-p1XIJe6D7CI1BFCUQWr8FnWJJZAw5U", cse_engine_id="dfa6a9cd2b3cc6812"):
    super().__init__()
    self.API_KEY = api_key
    self.SEARCH_ENGINE_ID = cse_engine_id

  
  def search(self, query):
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={self.API_KEY}&cx={self.SEARCH_ENGINE_ID}&q={query}&start={start}"
    data = requests.get(url).json()
    return data

  def save_results(self, results, filename):
    results_file_handle = open(filename, "w")
    for i, search_item in enumerate(results['items'], start=1):
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        link = search_item.get("link")
        results_file_handle.write("=" * 10 + f"Result #{i}" + "=" * 10+"\n")
        results_file_handle.write("Title:" + title +"\n")
        results_file_handle.write("Description:" + snippet +"\n" )
        results_file_handle.write("URL:" + link + "\n")
    results_file_handle.close()
    
  def search_engine(self):
    return 'google'

class Bingscraper(Basescraper):
  def __init__(self, api_key = '80ed6b5369ca47f8b88508924f36cd72'):
    super().__init__()
    self.API_KEY = api_key
  
  def search(self, query):
      search_url = "https://api.bing.microsoft.com/v7.0/search"
      headers = {"Ocp-Apim-Subscription-Key": self.API_KEY}
      params = {
        "q": query,
        "textDecorations": True,
        "textFormat": "HTML",
        "answerCount": 10}
        # get response
      data = requests.get(search_url, headers=headers, params=params).json()
      # pprint.pprint(data)
      # print(len(data))
      return data

  def save_results(self, results, filename):
    results_file_handle = open(filename, "w")
    for i, search_item in enumerate(results['webPages']['value'], start=1):
        title = search_item.get("name")
        snippet = search_item.get("snippet")
        link = search_item.get("url")
        results_file_handle.write("=" * 10 + f"Result #{i}" + "=" * 10+"\n")
        results_file_handle.write("Title:" + title +"\n")
        results_file_handle.write("Description:" + snippet +"\n" )
        results_file_handle.write("URL:" + link + "\n")

  def search_engine(self):
    return 'bing'


    
class Masterscraper:
  def google_cse_search(self, query, api_key="AIzaSyAk-p1XIJe6D7CI1BFCUQWr8FnWJJZAw5U", cse_engine_id="dfa6a9cd2b3cc6812"):
    API_KEY = api_key
    SEARCH_ENGINE_ID = cse_engine_id
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    data = requests.get(url).json()
    return data
    
  def bing_search(self, query):
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    subscription_key = '80ed6b5369ca47f8b88508924f36cd72'
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {
      "q": query,
      "textDecorations": True,
      "textFormat": "HTML",
      "answerCount": 10}
      # get response
    data = requests.get(search_url, headers=headers, params=params).json()
    # pprint.pprint(data)
    # print(len(data))
    return data

  def save_raw(self, results, filename):
    file_handle = open(filename, 'w')
    file_handle.write(pprint.pformat(results))  
    
  def google_save_results(self, results, filename):
    results_file_handle = open(filename, "w")
    for i, search_item in enumerate(results['items']
, start=1):
        title = search_item.get("title")
        snippet = search_item.get("snippet")
        link = search_item.get("link")
        results_file_handle.write("=" * 10 + f"Result #{i}" + "=" * 10+"\n")
        results_file_handle.write("Title:" + title +"\n")
        results_file_handle.write("Description:" + snippet +"\n" )
        results_file_handle.write("URL:" + link + "\n")
  
  def bing_save_results(self, results, filename):
    results_file_handle = open(filename, "w")
    for i, search_item in enumerate(results['webPages']['value'], start=1):
        title = search_item.get("name")
        snippet = search_item.get("snippet")
        link = search_item.get("url")
        results_file_handle.write("=" * 10 + f"Result #{i}" + "=" * 10+"\n")
        results_file_handle.write("Title:" + title +"\n")
        results_file_handle.write("Description:" + snippet +"\n" )
        results_file_handle.write("URL:" + link + "\n")

    
 