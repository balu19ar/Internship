#!/usr/bin/env python
# coding: utf-8

# In[6]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException,ElementNotInteractableException
import requests
import re
import warnings as wrn
wrn.filterwarnings("ignore")


# # 1. Scrape the details of most viewed videos on YouTube from Wikipedia.
# Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos
# You need to find following details:
# A) Rank
# B) Name
# C) Artist
# D) Upload date
# E) Views

# In[7]:


driver = webdriver.Chrome('C:\chromedriver.exe')


# In[8]:


url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
driver.get(url)


# In[9]:


time.sleep(2)


# In[10]:


#Name
name = []
try :
    names = driver.find_elements(by='xpath',value="//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[2]")
    for i in names:
        name.append(i.text)
except NoSuchElementException:
    name.append('No details available')
except StaleElementReferenceException:
    name.append('No details available')
time.sleep(2)


# In[11]:


name


# In[12]:


#Rank
rank = []

try :
    rank1 = driver.find_elements(by='xpath',value="//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[1]")
    for i in rank1:
        rank.append(i.text)
except NoSuchElementException :
    rank.append('No details avilable')
except StaleElementReferenceException:
    rank.append('No details avilable')

rank


# In[13]:


#Artist
artist = []
try:
    art = driver.find_elements(by='xpath',value="//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[3]")
    for i in art:
        artist.append(i.text)
except NoSuchElementException:
    artist.append('No details available')
except StaleElementReferenceException:
    artist.append('No details available')

artist


# In[14]:


#Upload Date
upload_date = []

try:
    ud = driver.find_elements(by='xpath',value="//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[5]")
    for i in ud:
        upload_date.append(i.text)
except NoSuchElementException:
    upload_date.append('No details available')
except StaleElementReferenceException:
    upload_date.append('No details available')
    
upload_date


# In[15]:


#Views
views = []

try:
    vi = driver.find_elements(by='xpath',value="//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[4]")
    for i in vi:
        views.append(i.text)
except NoSuchElementException:
    views.append('No details available')
except StaleElementReferenceException:
    views.append('No details available')
    
views


# In[16]:


df = pd.DataFrame(
{
    'Rank'        : rank,
    'Name'        : name,
    'Artist'      : artist,
    'Upload_Date' : upload_date,
    'Views'       : views
})

df


# # 2. Scrape the details team India’s international fixtures from bcci.tv.
# Url = https://www.bcci.tv/.
# You need to find following details:
# A) Match title (I.e. 1
# st ODI)
# B) Series
# C) Place
# D) Date
# E) Time
# Note: - From bcci.tv home page you have reach to the international fixture page through code.

# In[17]:


driver=webdriver.Chrome("C:\chromedriver.exe") 
time.sleep(2)
# Opening the bcci.tv
url = "https://www.bcci.tv/"
driver.get(url)


# In[18]:


time.sleep(2)


# In[19]:


fixtures = driver.find_element(by='xpath',value="/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a")
try:
    fixtures.click()
except ElementNotInteractableException:
    driver.get(fixtures.get_attribute('href'))


# In[20]:


#Match
match = []

try:
    mat = driver.find_elements(by='xpath',value="//span[@class='matchOrderText ng-binding ng-scope']")
    for i in mat:
        match.append(i.text)
except NoSuchElementException:
    match.append('No details available')
except StaleElementReferenceException:
    match.append('No details available')
    
match


# In[21]:


match = [i.split('-')[0] for i in match]
match


# In[22]:


#Series

series = []
try:
    se = driver.find_elements(by='xpath',value="//h5[@class='fix-text']")
    for i in se:
        series.append(i.text)
except NoSuchElementException:
    series.append('No details available')
series = series[1:16:2]
series


# In[23]:


#Location
location = []
try:
    lo = driver.find_elements(by='xpath',value="//div[@class='fix-place ng-binding ng-scope'][1]/span[2]")
    for i in lo:
        location.append(i.text)
except NoSuchElementException:
    location.append('No details available')
    
location


# In[24]:


location = [i.split(',')[0] for i in location]
location


# In[25]:


#Day
day = []
try:
    d = driver.find_elements(by='xpath',value="//div[@class='match-card-left match-schedule'][1]/h5")
    for i in d:
        day.append(i.text)
except NoSuchElementException:
    day.append('No details available')
    
day


# In[26]:


#Time
time = []
try:
    ti = driver.find_elements(by='xpath',value="//div[@class='match-card-right match-schedule '][1]/h5")
    for i in ti:
        time.append(i.text)
except NoSuchElementException:
    time.append('No details available')
time


# In[27]:


df_2 = pd.DataFrame({
    'Match' : match,
    'Series': series,
    'Location' : location,
    'Day' : day,
    "Time" : time
})

df_2


# # 3. Scrape the details of selenium exception from guru99.com.
# Url = https://www.guru99.com/
# You need to find following details:
# A) Name
# B) Description
# Note: - From guru99 home page you have to reach to selenium exception handling page through code

# In[29]:


driver=webdriver.Chrome("C:\chromedriver.exe") 

# Opening the bcci.tv
url = "https://www.guru99.com/exception-handling-selenium.html"
driver.get(url)


# In[30]:


#Name

name = []
try:
    n = driver.find_elements(by='xpath',value="//table[@class='table table-striped']//td[1]")
    for i in n:
        name.append(i.text)
except NoSuchElementException:
    name.append('No details')
    
name


# In[31]:


#Description
description = []
try:
    des = driver.find_elements(by='xpath',value="//table[@class='table table-striped']//td[2]")
    for i in des:
        description.append(i.text)
except NoSuchElementException:
    description.append('No details')
    
description


# In[32]:


df_3 = pd.DataFrame({"Exception name": name, "Exception description": description})
df_3


# # 4. Scrape the details of State-wise GDP of India from statisticstime.com.
# Url = http://statisticstimes.com/
# You have to find following details:
# A) Rank
# B) State
# C) GSDP(18-19)
# D) GSDP(17-18)
# E) Share(2017)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code.

# In[38]:


driver=webdriver.Chrome("C:\chromedriver.exe") 
url ="http://statisticstimes.com/"
driver.get(url)
economy = driver.find_element(by='xpath',value='/html/body/div[2]/div[1]/div[2]/div[2]/button')
economy.click()

india = driver.find_element(by='xpath',value='/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
india.click()
Rank1 = []
State = []
GSDP1 = []
GSDP2  = []
Share = []
GDP_billion = []
try: # Scraping Rank
    for i in driver.find_elements(by='xpath',value="//table[@class='display dataTable']/tbody/tr/td[1]"):
        Rank1.append(i.text)
except NoSuchElementException as e:
    print("No such element present")
Rank1


# In[ ]:


try: # Scraping Name
    for i in driver.find_elements(by='xpath',value="//table[@class='display dataTable']/tbody/tr/td[2]"):
        State.append(i.text)
except NoSuchElementException as e:
    print("No such element present")
State


# In[ ]:


try: # Scraping GSDP1
    for i in driver.find_elements(by='xpath',value="//table[@class='display dataTable']/tbody/tr/td[3]"):
        GSDP1.append(i.text)
except NoSuchElementException as e:
    print("-")
GSDP1


# In[ ]:


try: # Scraping GSDP2
    for i in driver.find_elements(by='xpath',value="//table[@class='display dataTable']/tbody/tr/td[4]"):
        GSDP2.append(i.text)
except NoSuchElementException as e:
    print("-")

try: # Scraping share
    for i in driver.find_elements(by='xpath',value="//table[@class='display dataTable']/tbody/tr/td[5]"):
        Share.append(i.text)
except NoSuchElementException as e:
    print("-")    
    
try: # Scraping GDP billion
    for i in driver.find_elements(by='xpath',value="//table[@class='display dataTable']/tbody/tr/td[6]"):
        GDP_billion.append(i.text)
except NoSuchElementException as e:
    print("-")


# In[ ]:


df_4 = pd.DataFrame({
    'Rank' : Rank1,
    'State' : State,
    'GSDP1' : GSDP1,
    'GSDP2' : GSDP2,
    'Share' : Share,
    'GDP_billion' : GDP_billion
})

df_4


# # 5. Scrape the details of trending repositories on Github.com.
# Url = https://github.com/
# You have to find the following details:
# A) Repository title
# B) Repository description
# C) Contributors count
# D) Language used

# In[39]:


driver=webdriver.Chrome("C:\chromedriver.exe") 
url ="https://github.com/"
driver.get(url)


# In[40]:


explore = driver.find_element(by='xpath',value="/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details")
explore.click()
trending = driver.find_element(by='xpath',value="/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details/div/ul/li[5]/a")
trending


# In[ ]:


Repository = []
Repository_des = []
Contributors = []
Language = []


# In[ ]:


try: # Scraping repository
    for i in driver.find_elements(by='xpath',value="//h1[@class='h3 lh-condensed']/a"):
        Repository.append(i.text)
except NoSuchElementException as e:
    print("-")
Repository = Repository[:19]
Repository


# In[43]:


try: # Scraping Repository description
    for i in driver.find_elements(by='xpath',value="//p[@class='col-9 color-fg-muted my-1 pr-4']"):
        Repository_des.append(i.text)
except NoSuchElementException as e:
    print("-")
Repository_des = Repository_des[:19]
Repository_des


# In[44]:


try: # Scraping Contributors count
    for i in driver.find_elements(by='xpath',value="//*[@id='js-pjax-container']/div[3]/div/div[2]/article/div[2]/a[2]"):
        Contributors.append(i.text)
except NoSuchElementException as e:
    print("-")
Contributors = Contributors[:19]
Contributors


# In[47]:


try: # Scraping language
    for i in driver.find_elements(by='xpath',value="//span[@class='d-inline-block ml-0 mr-3']"):
        Language.append(i.text)
except NoSuchElementException as e:
    print("-")
Language = Language[:19]
Language


# In[48]:


df_5 = pd.DataFrame({
    'Repository' : Repository,
    'Repository_des': Repository_des,
    'Contributors' : Contributors,
    'Language' : Language
})
df_5


# # 6. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/
# You have to find the following details:
# A) Song name
# B) Artist name
# C) Last week rank
# D) Peak rank
# E) Weeks on board
# Note: - From the home page you have to click on the charts option then hot 100-page link through code

# In[49]:


driver = webdriver.Chrome("C:\chromedriver.exe") 
url = "https://www.billboard.com/"
page = requests.get(url)
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
hot_100 = driver.find_element(by='xpath',value='/html/body/div[3]/header/div[2]/div/nav/ul/li[1]/a')
try:
    hot_100.click()
except ElementNotInteractableException:
    driver.get(hot_100.get_attribute('href'))
#Scraping First Song writtern in  Bold letters
first_song = []

try :
    first = driver.find_elements(by='xpath',value="//h3[@class='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet']")
    for f in first:
        first_song.append(f.text)
except NoSuchElementException:
    first_song.append('No details available')
    
first_song


# In[50]:


#scraping song names
song_name=[]
try:
    names=driver.find_elements(by='xpath',value="//h3[@class='c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only']")
    for i in names:
        song_name.append(i.text)
except NoSuchElementException:       #handling no such element exception
    song_name.append('No details available')

len(song_name)


# In[51]:


#Combining first_song and song_name
Song_Name = first_song + song_name

len(Song_Name)


# In[52]:


#Last Week
last_week = []
try:
    last = driver.find_elements(by='xpath',value="//li[@class='lrv-u-width-100p']/ul/li[4]/span")
    for i in last:
        last_week.append(i.text)
except NoSuchElementException:
    last_week.append('No details')
last_week

len(last_week)


# In[53]:


#Peak Pos

peak_pos = []
try:
    peak = driver.find_elements(by='xpath',value="//li[@class='lrv-u-width-100p']/ul/li[5]/span")
    for i in peak:
        peak_pos.append(i.text)
except NoSuchElementException:
    peak_pos.append('No details')
    
len(peak_pos)


# In[54]:


#Weeks on Board

weeks_on_board = []
try:
    week = driver.find_elements(by='xpath',value="//li[@class='lrv-u-width-100p']/ul/li[6]/span")
    for i in week:
        weeks_on_board.append(i.text)
except NoSuchElementException:
    weeks_on_board.append('No details')
len(weeks_on_board)


# In[55]:


#artist
artist = []
try:
    ar = driver.find_elements(by='xpath',value="//li[@class='lrv-u-width-100p']/ul/li[1]/span[1]")
    for i in ar:
        artist.append(i.text)
except NoSuchElementException:
    artist.append('No details')


# In[56]:


len(artist)


# In[57]:


# Creating data frame
Songs=pd.DataFrame({"SONG NAME":Song_Name,"ARTIST":artist, "LAST WEEK RANK":last_week,
                    "PEAK RANK":peak_pos, "WEEK ON BORD":weeks_on_board})

Songs


# # 7. Scrape the details of Data science recruiters from naukri.com. Url = https://www.naukri.com/
# You have to find the following details:
# A) Name
# B) Designation
# C) Company
# D) Skills they hire for
# E) Location
# Note: - From naukri.com homepage click on the recruiters option and the on the search pane type Data science and click on search. All this should be done through code

# In[58]:


driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://www.naukri.com/data-science-recruiters')
#clicking on recuriters link

recuriters_link = driver.find_element(by='xpath',value="/html/body/div[1]/div/ul/li[2]/a/div")
recuriters_link.click()
#type data Science

ds = driver.find_element(by='xpath',value="//div[@class='inpWrap']/input")
ds.send_keys("Data Science")
#Clicking on search button

search = driver.find_element(by='xpath',value="//button[@class='qsbSrch blueBtn']")
search.click()
#Scrapping Names

Names = []
try:
    n = driver.find_elements(by='xpath',value="//span[@class='fl ellipsis']")
    for i in n:
        Names.append(i.text)
except NoSuchElementException:
    Names.append('--')

print(Names)
print(len(Names))


# In[59]:


#Scrapping Designation

designation = []
try:
    desi = driver.find_elements(by='xpath',value="//span[@class='ellipsis clr']")
    for i in desi:
        designation.append(i.text)
except NoSuchElementException:
    designation.append('--')
print(designation)
print(len(designation))


# In[60]:


# Scrapping Company

company = []
try:
    com = driver.find_elements(by='xpath',value="//div[@class='vcard']//p[1]/a[2]")
    for i in com:
        company.append(i.text)
except NoSuchElementException:
    company.append('--')
print(company)
print(len(company))


# In[61]:


#Scrapping Skills they hire for
skills_they_hire_for = []
try:
    s = driver.find_elements(by='xpath',value="//div[@class='hireSec highlightable']")
    for i in s:
        skills_they_hire_for.append(i.text)
except NoSuchElementException:
    skills_they_hire_for.append('--')
print(skills_they_hire_for)
print(len(skills_they_hire_for))


# In[62]:


# Scrapping Location
location = []
try:
    loc = driver.find_elements(by='xpath',value="//div[@class='vcard']/p[1]/span[2]")
    for i in loc:
        location.append(i.text)
except NoSuchElementException:
    location.append('--')
print(location)


# In[63]:


len(location)


# In[64]:


Data_Science = pd.DataFrame({
    'Name' : Names,
    'Designation' : designation,
    'Company' : company,
    'Skills' : skills_they_hire_for,
    'Location' : location
})

Data_Science


# # 8. Scrape the details of Highest selling novels.
# Url = https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey- compare/
# You have to find the following details:
# A) Book name
# B) Author name
# C) Volumes sold
# D) Publisher
# E) Genre

# In[65]:


driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")
#Scrapping Book Name
book_name = []
try:
    bn = driver.find_elements(by='xpath',value="//table[@class='in-article sortable']/tbody/tr/td[2]")
    for i in bn:
        book_name.append(i.text)
except NoSuchElementException:
    book_name.append('---')
book_name
print(len(book_name))


# In[66]:


#Scrapping author name
author_name = []
try:
    an = driver.find_elements(by='xpath',value="//table[@class='in-article sortable']/tbody/tr/td[3]")
    for i in an:
        author_name.append(i.text)
except NoSuchElementException:
    author_name.append('--')
print(author_name)
print(len(author_name))


# In[67]:


#Scrapping Volume Sales
volume = []
try:
    vol = driver.find_elements(by='xpath',value="//table[@class='in-article sortable']/tbody/tr/td[4]")
    for i in vol:
        volume.append(i.text)
except NoSuchElementException:
    volume.append('--')
print(volume)
print(len(volume))


# In[68]:


#Scrapping Publisher
publisher = []
try:
    pub = driver.find_elements(by='xpath',value="//table[@class='in-article sortable']/tbody/tr/td[5]")
    for i in pub:
        publisher.append(i.text)
except NoSuchElementException:
    publisher.append('--')
print(publisher)
print(len(publisher))


# In[69]:


#Scrapping Genre
genre = []
try:
    gen = driver.find_elements(by='xpath',value="//table[@class='in-article sortable']/tbody/tr/td[6]")
    for i in gen:
        genre.append(i.text)
except NoSuchElementException:
    genre.append('--')
print(genre)
print(len(genre))


# In[70]:


highest_selling_novels = pd.DataFrame(
{
    'Book Name'    : book_name,
    'Author Name'  : author_name,
    'Volume Sales' : volume,
    'Publisher'    : publisher,
    'Genre'        : genre
})


# In[71]:


highest_selling_novels


# # 9. Scrape the details most watched tv series of all time from imdb.com. Url = https://www.imdb.com/list/ls095964455/
# You have to find the following details:
# A) Name
# B) Year span
# C) Genre
# D) Run time
# E) Ratings
# F) Votes

# In[72]:


driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get("https://www.imdb.com/list/ls095964455/")
#Scrapping Name
Name = []
try:
    m = driver.find_elements(by='xpath',value="//div[@class='lister-item-content']/h3/a")
    for i in m:
        Name.append(i.text)
except NoSuchElementException:
    Name.append('--')
print(Name)
print(len(Name))


# In[73]:


#Year Span
year_span = []
try:
    year = driver.find_elements(by='xpath',value="//div[@class='lister-item-content']/h3/span[2]")
    for i in year:
        year_span.append(i.text)
except NoSuchElementException:
    year_span.append('--')
print(year_span)
print(len(year_span))


# In[74]:


#Genre
Genre = []
try:
    g = driver.find_elements(by='xpath',value="//div[@class='lister-item-content']/p/span[5]")
    for i in g:
        Genre.append(i.text)
except NoSuchElementException:
    Genre.append('--')
print(Genre)
print(len(Genre))


# In[75]:


#Run-Time
run_time = []
try:
    rt = driver.find_elements(by='xpath',value="//div[@class='lister-item-content']/p/span[3]")
    for i in rt:
        run_time.append(i.text)
except NoSuchElementException:
    run_time.append('--')
print(run_time)
print(len(run_time))


# In[76]:


#Ratings
ratings = []
try:
    rate = driver.find_elements(by='xpath',value="//div[@class='lister-item-content']/div/div/span[2]")
    for i in rate:
        ratings.append(i.text)
except NoSuchElementException:
    ratings.append('--')
print(ratings)
print(len(ratings))


# In[77]:


#votes
votes = []
try:
    vote = driver.find_elements(by='xpath',value="//div[@class='lister-item-content']/p[4]/span[2]")
    for i in vote:
        votes.append(i.text)
except NoSuchElementException:
    votes.append('--')
print(votes)
print(len(votes))


# In[78]:


Imdb = pd.DataFrame(
{
    'Name' : Name,
    'Year Span' : year_span,
    'Genre' : Genre,
    'Run time' : run_time,
    'Ratings' : ratings,
    'Votes' : votes
})
Imdb


# # 10. Details of Datasets from UCI machine learning repositories. Url = https://archive.ics.uci.edu/
# You have to find the following details:
# A) Dataset name
# B) Data type
# C) Task
# D) Attribute type
# E) No of instances
# F) No of attribute
# G) Year
# Note: - from the home page you have to go to the ShowAllDataset page through code.

# In[79]:


driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get("https://archive.ics.uci.edu/ml/index.php")
respository=driver.find_element(by='xpath',value="//span[@class='normal']/b/a")
respository.click()
#Dataset Name
dataset_name = []
try:
    dn = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[2]/p/b/a")
    for i in dn:
        dataset_name.append(i.text)
except NoSuchElementException:
    dataset_name.append('--')
print(dataset_name)
print(len(dataset_name))


# In[80]:


#Data Type
data_type = []
try:
    dt = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[2]")
    for i in dt:
        data_type.append(i.text)
except NoSuchElementException:
    data_type.append('--')
#data_type.remove('Data Types')
len(data_type)


# In[81]:


print(data_type)


# In[ ]:


#Task
task = []
try:
    ta = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[3]")
    for i in ta:
        task.append(i.text)
except NoSuchElementException:
    task.append('--')
len(task)


# In[ ]:


print(task)


# In[ ]:


#Attribute type
attribute_type = []
try:
    att = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[4]")
    for i in att:
        attribute_type.append(i.text)
except NoSuchElementException:
    attribute_type.append('--')
attribute_type.remove('Attribute Types')
print(attribute_type)


# In[ ]:


#No of instances
no_of_instances = []
try:
    no = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[5]")
    for i in no:
        no_of_instances.append(i.text)
except NoSuchElementException:
    no_of_instances.append('--')
no_of_instances.remove('# Instances')
print(no_of_instances)


# In[ ]:


#No of attribute
no_of_attribute = []
try:
    p = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[6]")
    for i in p:
        no_of_attribute.append(i.text)
except NoSuchElementException:
    no_of_attribute.append('--')
no_of_attribute.remove('# Attributes')
print(no_of_attribute)


# In[ ]:


#Year
Year = []
try:
    y = driver.find_elements(by='xpath',value="/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td[7]")
    for i in y:
        Year.append(i.text)
except NoSuchElementException:
    Year.append('--')
Year.remove('Year')
print(Year)


# In[ ]:


Datasets = pd.DataFrame(
{
    'Dataset name' : dataset_name,
    'Data type' : data_type,
    'Task' : task,
    'Attribute type' : attribute_type,
    'No of instances' : no_of_instances,
    'No of attribute' : no_of_attribute,
    'Year'  : Year
})
Datasets

