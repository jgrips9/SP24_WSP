#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install pandas')
import sys
#Below you must set path to where webdriver is installed. This path will be different for you.
sys.path.insert(0,'C:\\Users\\jrg363_rs\\Downloads\\chromedriver')

#Make sure to install all packages.
#!pip install selenium
#!pip install pandas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re
import pandas as pd
import time


# In[7]:


chrome_options = webdriver.ChromeOptions()


# In[10]:


import random
from selenium.webdriver.common.by import By
 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.tripadvisor.com/Hotels-g45963-zfc5-Las_Vegas_Nevada-Hotels.html")


# In[11]:


#This gets list of all hotel links from previous code
list2 = driver.find_elements(By.XPATH, "//div[@class='rlqQt _T A']")


# In[12]:


#This code will extract the links that go directly to the URLs and store into a list. Eventaully loop through all the links.
#Extract desired information and go to the next page. You can also restrict to target the first 10 links rather than all of them. 
link = []
for i in list2:
    link.append(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))

#Clse webdriver
driver.close()


# In[15]:


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(link[0])


# In[16]:


time.sleep(5)
driver.find_element(By.XPATH, "//label[@for='ReviewRatingFilter_2']").click()
driver.find_element(By.XPATH, "//label[@for='ReviewRatingFilter_1']").click()


# In[17]:


reviewsfull = driver.find_elements(By.XPATH, "//div[@class='yJgrn']")


# In[19]:


#Loop through this. Extract that information. 
div_review = []
for i in reviewsfull:
    div_review.append(i.find_element(By.TAG_NAME, "div").text)


# In[20]:


#Example of some results
div_review[0]


# In[21]:


#Pages
pages = driver.find_elements(By.XPATH, "//div[@class='nsTKv']")


# In[22]:


pages[1].click()


# In[23]:


#Return back to same page
pages[0].click()


# In[24]:


#Automated process
#Now into loop. Traverse 3 pages. This is just my counter variable. 
#Set your starting and ending pages. 
import time
ender = 3
starter = 1
div_review = []
while starter <= ender:
    time.sleep(3)
    starter = starter + 1
    reviewsfull = driver.find_elements(By.XPATH, "//div[@class='yJgrn']")
    for i in reviewsfull:
        div_review.append(i.find_element(By.TAG_NAME, "div").text)
    pages = driver.find_elements(By.XPATH, "//div[@class='nsTKv']")
    for j in range(0, (len(pages)-1)):
        if pages[j].text == str(starter):
            pages[j].click()


# In[34]:


#Then export results. 
title = driver.find_element(By.ID, "HEADING").text
title_list = [title]*len(div_review)
data = pd.DataFrame({
    'title': title_list,
    'review': div_review
    })
data.to_csv("hotel_reviews.csv")


# In[33]:


display(data)


# In[41]:


def hotel_pages():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.tripadvisor.com/Hotels-g45963-zfc5-Las_Vegas_Nevada-Hotels.html")
    time.sleep(3)
    #This gets list of all hotel links from previous code
    list2 = driver.find_elements(By.XPATH, "//div[@class='rlqQt _T A']")
    for i in list2:
        link.append(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    #Clse webdriver
    driver.close()
    return link


# In[62]:


def hotel_reviews(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(link[0])
    time.sleep(3)
    ender = 3
    starter = 1
    while starter <= ender:
        time.sleep(3)
        starter = starter + 1
        reviewsfull = driver.find_elements(By.XPATH, "//div[@class='yJgrn']")
        for i in reviewsfull:
            div_review.append(i.find_element(By.TAG_NAME, "div").text)
        pages = driver.find_elements(By.XPATH, "//div[@class='nsTKv']")
        for j in range(0, (len(pages)-1)):
            if pages[j].text == str(starter):
                pages[j].click()
    return div_review


# In[42]:


#Now do in full Even to avoid the captcha
attempts = 6
k = 1
while k < attempts:
    k = k+1
    try:
        link = hotel_pages()
    except:
        link = hotel_pages()
    


# In[48]:


link = list(set(link))
link[0]


# In[53]:


div_review = []


# In[63]:


import time
attempts = 6
k = 1
while k < attempts:
    k = k+1
    try:
        div_review = hotel_reviews(link[0])
    except:
        div_review = hotel_reviews(link[0])


# In[74]:


len(div_review)


# In[80]:


#Then export results. 
#Drop duplicates
div_review = list(set(div_review))
url = [link[0]]*len(div_review)
data = pd.DataFrame({
    'url': url,
    'review': div_review
    })
data.to_csv("hotel_reviews.csv")


# In[81]:


display(data)


# In[ ]:




