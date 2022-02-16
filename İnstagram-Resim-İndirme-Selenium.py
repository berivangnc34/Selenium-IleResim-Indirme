#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[4]:


header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
url="https://www.instagram.com/ecoralphotography/"
response=requests.get(url,headers=header)


# In[6]:


response.text


# In[7]:


soup=BeautifulSoup(response.text,"html.parser")


# In[8]:


soup


# In[9]:


soup.find_all('a')


# In[13]:


from selenium import webdriver 


# In[51]:


DRIVER_PATH='C:/Users/Windows10/Desktop/Yeni klasör/chromedriver.exe'
driver=webdriver.Chrome(executable_path=DRIVER_PATH)


# In[52]:


driver.get('https://www.instagram.com/ecoralphotography/')


# In[53]:


driver.page_source


# In[54]:


soup=BeautifulSoup(driver.page_source,"html.parser")


# In[55]:


soup


# In[56]:


soup.find_all('a')


# In[88]:


list(enumerate(links))


    


# In[90]:


for i in soup.find_all('a',href = True) :
   if i['href'].startswith('/p'):
       print("Link Found:https://www.instagram.com/{0}".format(i['href']))
       links.append('https://www.instagram.com/'+i['href'])
   
   driver2.page_source


# In[91]:


for i,j in enumerate(links):
    driver_i=webdriver.Chrome(executable_path =DRIVER_PATH)
    driver_i(j)
    soup_i=BeautifulSoup(driver_i.page_source,"html.parser")
    image_link=soup_i.find_all('div',{'class':'eLAPa kPFhm'})[0].find_all('img')[0]['src']
    download_image(image_link)
    driver_i.quit()
    
    


# In[72]:





# In[77]:





# In[79]:


import urllib
def download_image(url,destination='D:/erhancoral/'):
    resource=urllib.request.urlopen(url)
    filename=destination+url[-8:]+'.jpg'
    output=open(filename,"wb")
    output.write(resource.read())
    output.close
    
    


# In[84]:


download_image('https://instagram.fist6-3.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/273899003_207273491586499_4956674888875872383_n.jpg?_nc_ht=instagram.fist6-3.fna.fbcdn.net&_nc_cat=107&_nc_ohc=8dmkCfS6xM0AX8kMimP&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT8zizY2O5HXfi9msyA9M7y7q_FxP8WbMyKs8V2ZAhlaxQ&oe=621232C7&_nc_sid=83d603')


# In[ ]:




