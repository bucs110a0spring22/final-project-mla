# https://stackoverflow.com/questions/38635419/searching-in-google-with-python
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
# https://developpaper.com/question/how-does-python-get-the-real-url-of-baidu-search-results/
# https://github.com/Yhinner/SinaWeiboScraper

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# from googlesearch import search
import requests

class Master_Scraper:
  def google_cse_search(self,query, api_key="AIzaSyAk-p1XIJe6D7CI1BFCUQWr8FnWJJZAw5U", cse_engine_id="dfa6a9cd2b3cc6812"):
    API_KEY = api_key
    SEARCH_ENGINE_ID = cse_engine_id
    # the search query you want
   
    # using the first page
    page = 1
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    # make the API request
    data = [""]
    data = requests.get(url).json()
    # get the result items
    search_items = data.get("items")
    # iterate over 10 results found
    print(search_items)
    for i, search_item in enumerate(search_items, start=1):
        # get the page title
        title = search_item.get("title")
        # get page snippet
        snippet = search_item.get("snippet")
        # get the HTML snippet (bolded keywords)
        html_snippet = search_item.get("htmlSnippet")
        # extract the page url
        link = search_item.get("link")
        # print the results
        print("=" * 10, f"Result #{i + start - 1}", "=" * 10)
        print("Title:", title)
        print("Description:", snippet)
        print("URL:", link, "\n")
      
#def bing_search(self, query, )
  