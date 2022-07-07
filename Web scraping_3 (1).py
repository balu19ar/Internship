#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import urllib
import pathlib
import datetime


# # 1. Write a python program which searches all the product under a particular product from www.amazon.in. 
# The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search 
# for guitars.

# In[ ]:


#connect to driver
driver=webdriver.Chrome("chromedriver.exe")
driver.maximize_window()


# In[ ]:


#website url
driver.get("https://www.amazon.in/")


# In[ ]:


#search bar selection
search_bar=driver.find_element(by='id',value="twotabsearchtextbox")
#take input from user: Note press enter after entering the input to get out of loop
print("what would you like to search today?")
search_for=input()


# In[ ]:


#send the input taken
search_bar.clear()
search_bar.send_keys(search_for)
#click on search icon
search_button=driver.find_element(by='id',value="nav-search-submit-button")
search_button.click()


# # 2. In the above question, now scrape the following details of each product listed in first 3 pages of your 
# search results and save it in a data frame and csv. In case if any product has less than 3 pages in search 
# results then scrape all the products available under that product name. Details to be scraped are: "Brand 
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.
# 

# In[ ]:


URL=[]  #Empty list
for page in range(0,3):
    for i in driver.find_elements(by='xpath',value="//div[@class='a-section a-spacing-medium']//h2"):
        URL.append(i.find_element(by='xpath',value=".//a").get_attribute('href'))
    try:
        next_page=driver.find_element(by='xpath',value="//div[@class='a-text-center']/ul/li[@class='a-last']/a").get_attribute('href')
        driver.get(next_page)
        driver.refresh()   
    except:
        break   
        
#Taking the empty lists
brand_name=[]
product_name=[]
Rating=[]
no_of_ratings=[]
price=[]
returns=[]
delivery=[]
availability=[]
other_details=[]
product_url=[]
     
#We are running a for loop for the url as it changes for every page and we are extracting the product url
for i in URL:
    driver.get(i)
    product_url.append(i)
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds 
    
    #Extracting the brand name
    try:
        brand_name.append(driver.find_element(by='id',value="productTitle").text.split(' ')[0])
    except NoSuchElementException as e:
        brand_name.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds   
    
    #Extracting the product name
    try:
        string=' '  #Empty string
        for j in driver.find_element(by='id',value="productTitle").text.split(' ')[1:]:
            string=string+' '+j  #Extracting the text and appending to empty string
        product_name.append(string)  #Appending the string having the extracted text
    except NoSuchElementException as e:
            product_name.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds     
    
    #Extracting the ratings
    try:
        Rating.append(driver.find_element(by='id',value="acrPopover").get_attribute('title')) 
    except NoSuchElementException as e:
        Rating.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds 
    
    #Extracting the number of ratings
    try:
        no_of_ratings.append(driver.find_element(by='id',value="acrCustomerReviewText").text) 
    except NoSuchElementException as e:
        no_of_ratings.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds 
    
    #Extracting the price
    try:
        try:
            price.append(driver.find_element(by='id',value="priceblock_saleprice").text) 
        except:
            try:
                price.append(driver.find_element(by='id',value="priceblock_dealprice").text)
            except:
                price.append(driver.find_element(by='id',value="priceblock_ourprice").text)
    except NoSuchElementException as e:
        price.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds 
    
    #Extracting the Return/Exchange
    try:
        returns.append(driver.find_element(by='xpath',value="//div[@id='RETURNS_POLICY']").text)
    except NoSuchElementException as e:
        returns.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds 
    
    #Extracting Expected Delivery
    try:
        delivery.append(driver.find_element(by='xpath',value='//div[@id="ddmDeliveryMessage"]/b').text)
    except NoSuchElementException as e:
        delivery.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds  
    
    #Extracting the availability of headphones
    try:
        availability.append(driver.find_element(by='xpath',value="//div[@id='availability']").text)
    except NoSuchElementException as e:    
        availability.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds  
    
    #Extracting the other details available
    try:
        details=[i.text.replace('\n','---') for i in driver.find_element(by='id',value="productDetails_techSpec_section_1").find_elements_by_xpath(".//tbody")]
        other_details.append(details[0])
    except NoSuchElementException as e:     
        other_details.append("-")
    driver.implicitly_wait(3)  #Making the driver automatically wait for 3 seconds    


# In[ ]:


#Checking the length of data extracted
print(len(brand_name),len(product_name),len(Rating),len(no_of_ratings),len(price),len(returns),len(delivery),
      len(availability),len(other_details),len(product_url))


# In[ ]:


amazon=pd.DataFrame({'Brand Name':brand_name,'Name of Product':product_name,'Rating':Rating,'No of Ratings':no_of_ratings,
                     'Price':price,'Return/Exchange':returns,'Expected Delivery':delivery,'Availability':availability,
                     'Other details':other_details,'Product URL':product_url})
amazon


# # 3.Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.

# In[ ]:


# Activating the chrome browser
driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(3)

# Opening the google images
url = "https://images.google.com/"
driver.get(url)


search_bar = driver.find_element(by='xpath',value='//*[@id="sbtc"]/div/div[2]/input')    # Finding the search bar using it's xpath
search_bar.send_keys("fruits")       # Inputing "fruits" keyword to search images
search_button = driver.find_element(by='xpath',value='//*[@id="sbtc"]/button')    # Finding the xpath of search button
search_button.click()        # Clicking the search button


# 500 time we scroll down by 10000 in order to generate more images on the website
for _ in range(500):
    driver.execute_script("window.scrollBy(0,10000)")
    
images = driver.find_elements(by='xpath',value='//img[@class="rg_i Q4LuWd"]')

img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
            
            
for i in range(len(img_urls)):
    if i >= 100:
        break
    print("Downloading {0} of {1} images" .format(i, 100))
    response= requests.get(img_urls[i])
    file = open(r"C:\Users\User\Desktop\Data Science\Internship_28"+str(i)+".jpg", "wb")
    file.write(response.content)


# # 4) Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[ ]:


driver=webdriver.Chrome("chromedriver.exe")
# getting the web page with the provided url
url = "https://www.flipkart.com/"
driver.get(url)
time.sleep(3)  # waiting for 3 seconds here
click_btn = driver.find_element(by='xpath',value="//div[@class='_2QfC02']//button").click()
#giving inputs to search bar
search_bar = driver.find_element(by='xpath',value="//div[@class='_3OO5Xc']//input")
search_bar.send_keys("Smartphones")
search_btn = driver.find_element(by='xpath',value="/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_btn.click()
time.sleep(5)


# In[ ]:


urls = []
for i in driver.find_elements(by='xpath',value="//a[@class='_1fQZEK']"):
    urls.append(i.get_attribute("href"))

# getting the required data inside the empty lists
brand_names = []
name = []
color = []
RAM = []
storage = []
prim_cam = []
sec_cam = []
Display_size = []
display_resolution = []
processor = []
processor_core = []
battery_cap = []
prices = []
product_url = []

# fetching battery capacity
for i in driver.find_elements(by='xpath',value="//div[@class='fMghEO']"):
    try:
        bat_cap = driver.find_element(by='xpath',value="//ul[@class='_1xgFaf']//li[4]")
        battery_cap.append(bat_cap.text)
    except NoSuchElementException:
        battery_cap.append('-')
for i in urls:
    driver.get(i)
    time.sleep(3)
    
    # fetching brand names
    try:
        br_name = driver.find_element(by='xpath',value="/html/body/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div[4]/a")
        brand_names.append(br_name.text.replace('Mobiles',''))
    except NoSuchElementException:
        brand_names.append('-')
    # fetching the smartphone names
    try:
        smt_name = driver.find_element(by='xpath',value="//h1[@class='yhB1nd']//span")
        name.append(smt_name.text)
    except NoSuchElementException:
        name.append('-')
    
    # fetching colors of smartphone
    try:
        clr = driver.find_element(by='xpath',value="//table[@class='_14cfVK']//tr[4]//td[2]")
        color.append(clr.text)
    except NoSuchElementException:
        color.append('-')
    time.sleep(2)
    
    # getting the read more button
    try:
        read_more_btn = driver.find_element(by='xpath',value="//button[@class='_2KpZ6l _1FH0tX']").click()
    except NoSuchElementException:
        pass
    time.sleep(3)
    
    # fetching the display size
    try:
        disp_size = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[2]//tr[1]//td[2]")
        Display_size.append(disp_size.text)
    except NoSuchElementException:
        Display_size.append
        
    # fetching the display resolution
    try:
        disp_res = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[2]//tr[2]//td[2]")
        display_resolution.append(disp_res.text)
    except NoSuchElementException:
        display_resolution.append('-')
        
    # fetching the processor information
    try:
        pro = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[3]//tr[2]//td[2]")
        processor.append(pro.text)
    except NoSuchElementException:
        processor.append('-')
        
    # fetching the processor and number of core details
    try:
        pro_core = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[3]//tr[3]//td[2]")
        processor_core.append(pro_core.text)
    except NoSuchElementException:
        processor_core.append('-')
        
    # fetching the storage/ROM details
    try:
        rom = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[4]//tr[1]//td[2]")
        storage.append(rom.text)
    except NoSuchElementException:
        storage.append('-')
        
    # fetching the RAM information
    try:
        ram = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[4]//tr[2]//td[2]")
        RAM.append(ram.text)
    except NoSuchElementException:
        RAM.append('-')
    time.sleep(2)
    
    # fetching the primary camera information
    try:
        p_cam = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[5]//tr[2]//td[2]")
        prim_cam.append(p_cam.text)
    except NoSuchElementException:
        prim_cam.append('-')
        
    # fetching the secondary camera information
    try:
        s_cam = driver.find_element(by='xpath',value="//div[@class='_1UhVsV']//div[5]//tr[5]//td[2]")
        sec_cam.append(s_cam.text)
    except NoSuchElementException:
        sec_cam.append('-')        
   
    # fetching the price of the smartphone
    try:
        price = driver.find_element(by='xpath',value="//div[@class='_30jeq3 _16Jk6d']")
        prices.append(price.text.replace('₹','Rs. '))
    except NoSuchElementException:
        prices.append('-')
    
    
# creating a dataframe now with the obtainined details
data = list(zip(brand_names,name,color,RAM,storage,prim_cam,sec_cam,Display_size,display_resolution,processor,
                processor_core,battery_cap,prices,urls))
df = pd.DataFrame(data, columns = ["Brand Name","Smartphone Name","Color","RAM","Storage/ROM","Primary Camera",
                                   "Secondary Camera","Display Size","Display Resolution","Processor","Processor-Core",
                                   "Battery Capacity","Price","Product Url"])
df


# In[ ]:


df.to_csv(r'C:\Users\User\Desktop\Data Science\Internship_28\smartphones.csv',index=False)


# # 5) Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[ ]:


# Activating the chrome browser
driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(2)

# opening google maps
url = "https://www.google.co.in/maps"
driver.get(url)
time.sleep(2)


search = driver.find_element(by='id',value="searchboxinput")                       # locating search bar
search.clear()                                                             # clearing search bar
time.sleep(2)
search.send_keys("Mumbai")                                                     # entering values in search bar
button = driver.find_element(by='id',value="searchbox-searchbutton")               # locating search button
button.click()                                                             # clicking search button
time.sleep(3)

try:
    url_string = driver.current_url
    print("URL Extracted: ", url_string)
    lat_lng = re.findall(r'@(.*)data',url_string)
    if len(lat_lng):
        lat_lng_list = lat_lng[0].split(",")
        if len(lat_lng_list)>=2:
            lat = lat_lng_list[0]
            lng = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(lat, lng))

except Exception as e:
        print("Error: ", str(e))


# # 6) Write a program to scrap details of all the funding deals for second quarter (i.e Jan 21 – March 21) from trak.in.

# In[ ]:


# Activating the chrome browser
driver=webdriver.Chrome("chromedriver.exe") 
time.sleep(2)

# opening trak.in
url = "https://trak.in/"
driver.get(url)
time.sleep(2)

# do click on funding deals
button = driver.find_element(by='xpath',value='//li[@id="menu-item-51510"]/a').get_attribute('href')
driver.get(button)

# Empty lists
fund_dict = {}
fund_dict['Date'] = []
fund_dict['Startup Name'] = []
fund_dict['Industry/Vertical'] = []
fund_dict['Sub-Vertical'] = []
fund_dict['Location'] = []
fund_dict['Investor'] = []
fund_dict['Investment Type'] = []
fund_dict['Amount(in USD)'] = []


for i in range(48,51):
    # Date
    dt = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[2]'.format(i))
    for d in dt:
        fund_dict['Date'].append(d.text)

    # Startup Name
    sn = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[3]'.format(i))
    for n in sn:
        fund_dict['Startup Name'].append(n.text)
    
    # Industry/Vertical
    ind = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[4]'.format(i))
    for n in ind:
        fund_dict['Industry/Vertical'].append(n.text)
    
    # Sub-Vertical
    sv = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[5]'.format(i))
    for s in sv:
        fund_dict['Sub-Vertical'].append(s.text)

    # Location
    loc = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[6]'.format(i))
    for l in loc:
        fund_dict['Location'].append(l.text)
    
    # Investor
    inv = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[7]'.format(i))
    for n in inv:
        fund_dict['Investor'].append(n.text)
    
    # Investment Type
    invt = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[8]'.format(i))
    for n in invt:
        fund_dict['Investment Type'].append(n.text)
    
    # Amount
    amt = driver.find_elements(by='xpath',value='//table[@id="tablepress-{}"]/tbody/tr/td[9]'.format(i))
    for a in amt:
        fund_dict['Amount(in USD)'].append(a.text)
    
fund_df = pd.DataFrame(fund_dict)
fund_df


# In[ ]:


fund_df.to_csv(r'C:\Users\User\Desktop\Data Science\Internship_28\funding_deals.csv',index=False)


# # 7) Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[ ]:


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.digit.in/top-products/best-gaming-laptops-40.html')
all_laptop_title = driver.find_elements(by='xpath',value='//div[@class="TopNumbeHeading sticky-footer"]/a')


# In[ ]:


all_name = []
for one_title in all_laptop_title:
    all_name.append(one_title.text)
    
name_series = pd.Series(all_name)
name_series


# In[ ]:


all_specs = driver.find_elements(by='xpath',value='//div[@class="Spcs-details"]')


# In[ ]:


all_spec_list = []
for one_spec in all_specs:

    os_name = one_spec.find_element(by='xpath',value='.//td[text()="OS"]/parent::*/td[3]').text
    display = one_spec.find_element(by='xpath',value='.//td[text()="Display"]/parent::*/td[3]').text
    processor = one_spec.find_element(by='xpath',value='.//td[text()="Processor"]/parent::*/td[3]').text
    memory = one_spec.find_element(by='xpath',value='.//td[text()="Memory"]/parent::*/td[3]').text
    graphics_processor = one_spec.find_element(by='xpath',value='.//td[text()="Graphics Processor"]/parent::*/td[3]').text
    
    all_spec_list.append({
        'os' : os_name,
        'display' : display,
        'processor' : processor,
        'memory' : memory,
        'graphics_processor' : graphics_processor,
    })
    
df = pd.DataFrame(all_spec_list)
df


# # 8) Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.

# In[ ]:


driver = webdriver.Chrome('chromedriver.exe')
# obtaining the web page with given url
url = 'https://www.forbes.com/'
driver.get(url)
time.sleep(3)

# clicking on the hamburger option on the left side of the page
optn = driver.find_element(by='xpath',value="//button[@class='icon--hamburger']")
optn.click()
time.sleep(1)

# now clicking on the 'Billionaires' option
bill = driver.find_element(by='xpath',value="/html/body/div[1]/header/nav/div[3]/ul/li[1]")
bill.click()
time.sleep(1)

# finally clicking on the 'World Billionaire' option after the mouse hover
world_bill = driver.find_element(by='xpath',value="/html/body/div[1]/header/nav/div[3]/ul/li[1]/div[2]/ul/li[2]/a")
world_bill.click()
time.sleep(1)


# In[ ]:


# fetching the rank
rank = []
try:
    rnk = driver.find_elements(by='xpath',value="//div[@class='rank']")
    for i in rnk:
        rank.append(i.text)
except NoSuchElementException:
    pass

# fetching the names of the billionaires
names = []
try:
    name = driver.find_elements(by='xpath',value="//div[@class='personName']")
    for i in name:
        names.append(i.text)
except NoSuchElementException:
    pass

# fetching the total net worth
net_worth = []
try:
    worth = driver.find_elements(by='xpath',value="//div[@class='netWorth']")
    for i in worth:
        net_worth.append(i.text)
except NoSuchElementException:
    pass

# fetching the age of the billionaires
Age = []
try:
    age = driver.find_elements(by='xpath',value="//div[@class='age']")
    for i in age:
        Age.append(i.text)
except NoSuchElementException:
    Age.append('-')
    
# fetching the citizenship of the billionaires
citizenship = []
try:
    cit = driver.find_elements(by='xpath',value="//div[@class='countryOfCitizenship']")
    for i in cit:
        citizenship.append(i.text)
except NoSuchElementException:
    citizenship.append('-')
    
# fetching the source of incomes for the billionaires
source = []
try:
    src = driver.find_elements(by='xpath',value="//div[@class='source-column']")
    for i in src:
        source.append(i.text)
except NoSuchElementException:
    source.append('-')
    
# fetching the industry in which the billionaires are prominent
industry = []
try:
    ind = driver.find_elements(by='xpath',value="//div[@class='category']")
    for i in ind:
        industry.append(i.text)
except NoSuchElementException:
    industry.append('-')
    
# now creating a dataframe from all the collected information
data = list(zip(rank,names,net_worth,Age,citizenship,source,industry))
df = pd.DataFrame(data, columns = ["Rank", "Name", "Net worth", "Age", "Citizenship", "Source","Industry"])
df


# # 9) Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted from any YouTube Video.

# In[ ]:


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.youtube.com/watch?v=kTJczUoc26U')
import pandas as pd
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import urllib
import pathlib
import datetime


# In[ ]:


def wait_for_page_load(xpath_url):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, xpath_url))
        WebDriverWait(driver, 5).until(element_present)
    except TimeoutException:
        pass
    except NoSuchElementException:
        print("Element not found")
wait_for_page_load('//ytd-comment-thread-renderer')

# Loading all comments
i = 1 
while True:
    i += 500
    driver.execute_script(f"window.scrollTo(0, {i});")
        
    all_box = driver.find_elements(by='xpath',value='//ytd-comment-thread-renderer')
    
    sleep(1)
    
    if len(all_box) > 500:
        break


# In[ ]:


def wait_for_page_load(xpath_url):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, xpath_url))
        WebDriverWait(driver, 5).until(element_present)
    except TimeoutException:
        pass
    except NoSuchElementException:
        print("Element not found")
wait_for_page_load('//ytd-comment-thread-renderer')

# Loading all comments
i = 1 
while True:
    i += 500
    driver.execute_script(f"window.scrollTo(0, {i});")
        
    all_box = driver.find_elements(by='xpath',value='//ytd-comment-thread-renderer')
    
    sleep(1)
    
    if len(all_box) > 500:
        break


# # 10) Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms from price, facilities and property description.

# In[ ]:


driver = webdriver.Chrome('chromedriver.exe')
# obtaining the web page from the given url
driver.get('https://www.hostelworld.com/s?q=London,%20England&country=England&city=London&type=city&id=3')
final_list = []
page_urls = []


while True:
    sleep(5)
    wait_for_page_load('//div[@class="property-card" and @data-v-62f28bda=""]')
    all_boxs = driver.find_elements(by='xpath',value='//div[@class="property-card" and @data-v-62f28bda=""]')
    for one_box in all_boxs:
        hostel_name = one_box.find_element(by='xpath',value='.//h2/a').text
        distance_from_city = one_box.find_element(by='xpath',value='.//a/span').text
        try:
            ratings = one_box.find_element(by='xpath',value='.//div[contains(@class,"score")]').text
        except:
            ratings = 'No rating'
            
        total_reviews = one_box.find_element(by='xpath',value='.//div[contains(@class,"reviews")]').text
        overall_reviews = one_box.find_element(by='xpath',value='.//div[contains(@class,"keyword")]').text
        privates_from_price = one_box.find_elements(by='xpath',value='.//div[contains(@class,"prices-col")]/a/div')[0].text
        dorms_from_price  = one_box.find_elements(by='xpath',value='.//div[contains(@class,"prices-col")]/a/div')[1].text
        facilities = one_box.find_element(by='xpath',value='.//div[contains(@class,"facilities")]').text.split('\n')
        
        page_url = one_box.find_element(by='xpath',value='.//h2/a').get_attribute('href')
        page_urls.append(page_url)

        final_list.append({
            'hostel_name' : hostel_name,
            'distance_from_city' : distance_from_city,
            'ratings' : ratings,
            'total_reviews' : total_reviews,
            'overall_reviews' : overall_reviews,
            'privates_from_price' : privates_from_price,
            'dorms_from_price' : dorms_from_price,
            'facilities' : facilities,

        })

df = pd.DataFrame(final_list)
df


# In[ ]:




