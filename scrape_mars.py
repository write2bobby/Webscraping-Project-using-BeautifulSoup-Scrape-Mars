from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def init_browser():
    //NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:\Users\beatl\Downloads\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars = {}
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep()

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser') 

    mars["news_title"] = soup.find('div', class_='content_title').get_text()
    
    //Return results
    print(mars["news_title"])