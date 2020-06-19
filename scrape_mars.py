#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pymongo
import requests
from flask import Flask, render_template


# In[2]:

def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
        browser = init_browser()
        results ={}



        get_ipython().system('which chromedriver')



        # In[4]:


        #Site 1
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        html = browser.html


        # In[31]:


        response = requests.get(url)
        soup2 = BeautifulSoup(html, 'html.parser')
        soup = BeautifulSoup(response.text, 'html.parser')


        # In[42]:


        first_title = soup2.find('div', class_='bottom_gradient').text
        first_body = soup2.find('div', class_='article_teaser_body').text
        print(first_title)
        print(first_body)


        # In[44]:


        #Site 2
        url_pic = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_pic)
        html_pic = browser.html
        soup_pic = BeautifulSoup(html_pic, 'html.parser')


        # In[63]:


        image_url = soup_pic.find('article', class_='carousel_item')['style']
        image_url = image_url.split("('", 1)[1].split("')")[0]
        image_url


        # In[64]:


        #Site 3
        twitter = "https://twitter.com/marswxreport?lang=en"
        browser.visit(twitter)
        html_twitter = browser.html
        soup_twitter = BeautifulSoup(html_twitter, 'html.parser')


        # In[101]:


        #tweet = soup_twitter.find("div", class_='css-1dbjc4n r-1loqt21 r-16y2uox r-1wbh5a2 r-1ny4l3l r-1udh08x r-1j3t67a r-o7ynqc r-6416eg')
        tweet = soup_twitter.find("div", class_='css-1dbjc4n')
        print(tweet)
                                


        # In[86]:


        #Site 4
        url_4 = "https://space-facts.com/mars/"
        browser.visit(url_4)
        html_4 = browser.html
        soup_4 = BeautifulSoup(html_4, 'html.parser')


        # In[87]:


        site_4 = pd.read_html(url_4)
        #site_4


        # In[91]:


        table_df = site_4[0]
        table_df.columns = ['Desc','Metric']
        table_df.head(2)


        # In[97]:


        html_table = table_df.to_html()
        html_table = html_table.replace('\n', '')
        #html_table


        # In[98]:


        table_df.to_html('table.html')
        get_ipython().system('open table.html')


        # In[124]:


        #Site 5 - Hemisphere 1
        url_51 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
        browser.visit(url_51)
        html_51 = browser.html
        soup_51 = BeautifulSoup(html_51, 'html.parser')

        hemUrl_1 = soup_51.find('div', class_='downloads').find('a')['href']
        print(hemUrl_1)


        # In[125]:


        #Site 5 - Hemisphere 2
        url_52 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
        browser.visit(url_52)
        html_52 = browser.html
        soup_52 = BeautifulSoup(html_52, 'html.parser')

        hemUrl_2 = soup_52.find('div', class_='downloads').find('a')['href']
        print(hemUrl_2)


        # In[126]:


        #Site 5 - Hemisphere 3
        url_53 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
        browser.visit(url_53)
        html_53 = browser.html
        soup_53 = BeautifulSoup(html_53, 'html.parser')

        hemUrl_3 = soup_53.find('div', class_='downloads').find('a')['href']
        print(hemUrl_3)


        # In[127]:


        #Site 5 - Hemisphere 4
        url_54 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
        browser.visit(url_54)
        html_54 = browser.html
        soup_54 = BeautifulSoup(html_54, 'html.parser')

        hemUrl_4 = soup_54.find('div', class_='downloads').find('a')['href']
        print(hemUrl_4)


        # In[132]:


        hemisphereImages = {
                "Cerberus Hemisphere": hemUrl_1,
                "Schiaparelli Hemisphere": hemUrl_2,
                "Syrtis Major Hemisphere": hemUrl_3,
                "Valles Marineris Hemisphere": hemUrl_4
        }

        hemisphereImages

        Mars_Export = { "Report_title:": first_title,
                "Report_descr": first_body,
                "img_url": image_url,
                "tweet": tweet,
                "Metric_table": table_df,
                "Hem_1": hemUrl_1,
                "Hem_2": hemUrl_2,
                "Hem_3": hemUrl_3,
                "Hem_4": hemUrl_4
                }
        
        

         # Close the browser after scraping
        browser.quit()

        return Mars_Export



