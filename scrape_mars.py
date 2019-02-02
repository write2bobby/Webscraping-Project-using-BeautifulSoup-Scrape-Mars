from splinter import Browser
from bs4 import BeautifulSoup 
import time
import pandas as pd

def init_browser():
    # Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": r"C:\Users\beatl\Downloads\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars = {}
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser') 

    mars["news_title"] = soup.find('div', class_='content_title').get_text()
    
    #Return results
    print(type(mars))

def main():
    results = scrape()

if __name__ == "__main__":
    main()    