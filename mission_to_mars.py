#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pprint
import requests
from bs4 import BeautifulSoup
from splinter import Browser
import urllib
import time


# In[3]:


executable_path = {'executable_path': r'C:\Users\beatl\Downloads\chromedriver.exe'}
browser = Browser('chrome', **executable_path)


# In[4]:


s = requests.session()
conn = s.get('https://mars.nasa.gov/news/')


# In[5]:


url = 'https://mars.nasa.gov/news/'


# In[6]:


browser.visit(url)


# In[7]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
soup


# In[8]:


news_title = soup.find('div', class_='content_title').get_text()
news_title


# In[9]:


news_paragraph = soup.find('div', class_='rollover_description_inner').get_text()
news_paragraph


# In[10]:


print(news_paragraph)


# In[18]:


# visit the JPL website and scrape the featured image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url) 
full_image = browser.find_by_id('full_image')
full_image.click()
time.sleep(1)
more_info = browser.find_link_by_partial_text('more info')
more_info.click()
time.sleep(1)
img_html = browser.html
img_soup = BeautifulSoup(img_html, 'html.parser')
img_1 = img_soup.find('figure', class_='lede').find('img')['src']
featured_img_url = f'https://www.jpl.nasa.gov{img_1}'
print(featured_img_url)


# In[13]:


# twitter url 
url = 'https://twitter.com/marswxreport?lang=en'

browser.visit(url)

soup = BeautifulSoup(browser.html, 'html.parser')

# localate the first tweet and extract text from it
mars_weather = soup.find('div', class_='js-tweet-text-container').text.split('\n')[1]
mars_weather


# In[21]:


#Mars Facts
url = 'http://space-facts.com/mars/'
df = pd.read_html(url)[0]
df.columns = ['Parameter','Value']
df.set_index('Parameter', inplace = True)
df


# In[20]:


df.to_html()


# In[15]:


hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})


# In[ ]:




