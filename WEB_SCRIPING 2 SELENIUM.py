#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install selenium')


# In[10]:


import selenium
from selenium import webdriver
import pandas as pd
import numpy as np
import time
import warnings
warnings.filterwarnings('ignore')


# In[11]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[12]:


driver.get("https://www.naukri.com/")# opning the website
time.sleep(3)


# In[13]:


search_field_designation=driver.find_element_by_class_name("suggestor-input")
search_field_designation.send_keys("Data Analyst") # inputing the data
search_location=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[5]/div/div/div/input')
search_location.send_keys("Banglore")# inputing place
search_button=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_button.click()


# In[14]:


job_title=[]
job_location=[]
company=[]
exp=[]


# In[15]:


job_tag=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
job_tag=job_tag[0:10]
for i in job_tag:
    job_title.append(i.text)#scraping job name
job_loc=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
job_loc=job_loc[0:10]
for i in job_loc:
    job_location.append(i.text)
#job_location
comp=driver.find_elements_by_xpath("//div[@class='mt-7 companyInfo subheading lh16']")
comp=comp[0:10]
for i in comp:
    company.append(i.text.split('\n')[0])
#company
expn=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]')
expn=expn[0:10]
for i in expn:
    exp.append(i.text)
driver.close()
#exp
data=pd.DataFrame({'Job-Title':job_title, 'Job-Location':job_location,'Company_Name':company,'Experience_Required':exp})
data


# # Q 2. Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data. This task will be done in following steps:

# In[16]:


driver=webdriver.Chrome("C:\chromedriver.exe")


# In[17]:



driver.get("https://www.naukri.com/")
time.sleep(3)


# In[18]:


search_field_designation=driver.find_element_by_class_name("suggestor-input")
search_field_designation.send_keys("Data Scientist")
search_button=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_button.click()


# In[ ]:


loc_filter=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[5]/div[2]/div[3]/label/p/span[1]')
loc_filter.click()


# In[ ]:


sal_filter=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]')
sal_filter.click()


# In[ ]:


job_title=[]
job_location=[]
company=[]
exp=[]


# In[ ]:


job_tag=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
job_tag=job_tag[0:10]
for i in job_tag:
    job_title.append(i.text)
job_loc=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
job_loc=job_loc[0:10]
for i in job_loc:
    job_location.append(i.text)
#job_location
comp=driver.find_elements_by_xpath("//div[@class='mt-7 companyInfo subheading lh16']")
comp=comp[0:10]
for i in comp:
    company.append(i.text.split('\n')[0])
#company
expn=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]')
expn=expn[0:10]
for i in expn:
    exp.append(i.text)
driver.close()
#exp
data=pd.DataFrame({'Job-Title':job_title, 'Job-Location':job_location,'Company_Name':company,'Experience_Required':exp})
data


# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below

# # You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required. 
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs

# In[ ]:


driver=webdriver.Chrome("C:\chromedriver.exe")

driver.get("https://www.naukri.com/")
time.sleep(3)


# In[ ]:


search_field_designation=driver.find_element_by_class_name("suggestor-input")
search_field_designation.send_keys("Data Scientist")
search_button=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_button.click()
loc_filter=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[5]/div[2]/div[3]/label/p/span[1]')
loc_filter.click()
sal_filter=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]')
sal_filter.click()


# In[ ]:


job_title=[]
job_location=[]
company=[]
exp=[]
job_tag=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
job_tag=job_tag[0:10]
for i in job_tag:
    job_title.append(i.text)
job_loc=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
job_loc=job_loc[0:10]
for i in job_loc:
    job_location.append(i.text)
#job_location
comp=driver.find_elements_by_xpath("//div[@class='mt-7 companyInfo subheading lh16']")
comp=comp[0:10]
for i in comp:
    company.append(i.text.split('\n')[0])
#company
expn=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]')
expn=expn[0:10]
for i in expn:
    exp.append(i.text)
driver.close()
#exp
data=pd.DataFrame({'Job-Title':job_title, 'Job-Location':job_location,'Company_Name':company,'Experience_Required':exp})
data


# # Q4 : Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 
# 1.Brand
# 2.Product Description
# 3.Price The attributes which you have to scrape is ticked marked in the below image.

# In[ ]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.flipkart.com/")
time.sleep(3)


# In[ ]:


b=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
b.click()


# In[ ]:


search_tag=driver.find_element_by_class_name("_3704LK")
search_tag.send_keys("Sunglasses")


# In[ ]:


search_button=driver.find_element_by_class_name("L0Z3Pu")
search_button.click()
time.sleep(3)


# In[ ]:


# creating required list for processing
brand=[]
product_dis=[]
price=[]
discount=[]

#Defining a function that include scrapping functions
def scrap():
    brnd=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
    for i in brnd:
        if(len(brand)==100):
            break
        else:
            brand.append(i.text)
        dis=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
        for i in dis:
            if(len(product_dis)==100):
                break
            else:
                product_dis.append(i.text)
        pri=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
        for j in pri:
            if(len(price)==100):
                break
            else:
                price.append(j.text)
        dis=driver.find_elements_by_xpath('//div[@class="_3Ay6Sb"]')
        for j in dis:
            if(len(discount)==100):
                break
            else:
                discount.append(j.text)

#now we are going to 100 sunglasses 
for i in range(0,3):
    if(i==0):
        scrap()
    elif i==1:
        driver.find_element_by_class_name("_1LKTO3").click()
        time.sleep(3)
        scrap()
    elif(i==2):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]').click()
        time.sleep(3)
        scrap()
    
# Creating one data fram using scrapped data             
Sunglass=pd.DataFrame({'Brand':brand,'Product Details':product_dis,'Price':price,'Discount':discount})
Sunglass


# In[ ]:


driver.close()


# # Q5 Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone.

# In[ ]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.flipkart.com/")
time.sleep(3)
b=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
b.click()
search_tag=driver.find_element_by_class_name("_3704LK")
search_tag.send_keys("iphone 11")


# In[ ]:


search_button=driver.find_element_by_class_name("L0Z3Pu")
search_button.click()


# In[ ]:


driver.get("https://www.flipkart.com/apple-iphone-11-white-64-gb/p/itmfc6a7091eb20b?pid=MOBFWQ6BVWVEH3XE&lid=LSTMOBFWQ6BVWVEH3XEB1SFMZ&marketplace=FLIPKART&q=iphone+11&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=ffcd465c-1c35-4a3b-8c2b-8d0bc138972c.MOBFWQ6BVWVEH3XE.SEARCH&ppt=hp&ppn=homepage&ssid=x6aouugn8w0000001654762626827&qH=f6cdfdaa9f3c23f3")


# In[ ]:


phone=driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[6]/div/a/div')
phone.click()


# In[19]:


rating=[]
review_sum=[]
review_dis=[]
j=1
def i_scrap():
    rate=driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')
    for i in rate:
        rating.append(i.text)
    review=driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')
    for i in review:
        review_sum.append(i.text)
    rdis=driver.find_elements_by_xpath('//div[@class="t-ZTKy"]')
    for i in rdis:
        review_dis.append(i.text)
#i_scrap()
next_b=driver.find_elements_by_class_name("ge-49M")
for b in next_b:
    i_scrap()
len(rating)
iphone_rating=pd.DataFrame({'Rating':rating,'Review_Summery':review_sum,'Review_Disciption':review_dis})
iphone_rating
    


# In[ ]:


driver.close()


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field. You have to scrape 4 attributes of each sneaker:
# 
# 1.Brand
# 2.Product Description
# 3.Price
# 4.Discount

# In[ ]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.flipkart.com/")
time.sleep(3)
b=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
b.click()
search_tag=driver.find_element_by_class_name("_3704LK")
search_tag.send_keys("sneakers")


# In[ ]:


time.sleep(2)
search_button=driver.find_element_by_class_name("L0Z3Pu")
search_button.click()


# In[ ]:


brand=[]
product_dis=[]
price=[]
discount=[]

#Defining a function that include scrapping functions
def scrap():
    
    brnd=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
    for i in brnd:
        if(len(brand)==100):
            break
        else:
            brand.append(i.text)
        dis=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
        for i in dis:
            if(len(product_dis)==100):
                break
            else:
                product_dis.append(i.text)
        pri=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
        for j in pri:
            if(len(price)==100):
                break
            else:
                price.append(j.text)
        dis=driver.find_elements_by_xpath('//div[@class="_3Ay6Sb"]')
        for j in dis:
            if(len(discount)==100):
                break
            else:
                discount.append(j.text)

#now we are going to 100 sunglasses 
for i in range(0,3):
    if(i==0):
        scrap()
    elif i==1:
        driver.find_element_by_class_name("_1LKTO3").click()
        time.sleep(3)
        scrap()
    elif(i==2):
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]').click()
        time.sleep(3)
        scrap()
    
# Creating one data fram using scrapped data             
sneakers=pd.DataFrame({'Brand':brand,'Product Details':product_dis,'Price':price,'Discount':discount})
sneakers


# In[ ]:


driver.close()


# # Q7: Go to the link - https://www.myntra.com/shoes Set second Price filter and Color filter to “Black”, as shown in the below image. And then scrape First 100 shoes data you get. The data should include “Brand” of the shoes , Short Shoe description, price of the shoe as shown in the below image.

# In[22]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.myntra.com/shoes")


# In[23]:


price_band=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label')
price_band.click()


# In[24]:


time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/div').click()
time.sleep(2)


# In[25]:


brand=[]
price=[]
short_dis=[]
def Shoe_scrap():
    br=driver.find_elements_by_xpath('//h3[@class="product-brand"]')
    for i in br:
        brand.append(i.text)
    pr=driver.find_elements_by_xpath('//h4[@class="product-product"]')
    for i in pr:
        short_dis.append(i.text)
    sd=driver.find_elements_by_xpath('//div[@class="product-price"]')
    for i in sd:
        price.append(i.text)
Shoe_scrap()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[3]/a').click()
time.sleep(3)
Shoe_scrap()
print(len(brand),len(price),len(short_dis))
#class="pagination-number"
Shoe=pd.DataFrame({'Brand':brand,'Prodcut Discription':short_dis,'Price':price})
Shoe


# In[26]:


driver.close()


# # Q8: Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7”

# In[27]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.amazon.in/")


# In[28]:


amazon_searchtext=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
amazon_searchtext.send_keys("Laptop")
time.sleep(2)


# In[29]:


driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul[4]/li[13]/span/a/div/label/i').click()


# In[30]:


lap_title=[]
lap_pri=[]
lap_rate=[]
#def lap_scrap():
ti=driver.find_elements_by_xpath('//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
for i in ti:
    if(len(lap_title)==10):
        break
    else:
        lap_title.append(i.text)
rt=driver.find_elements_by_xpath('//div[@class="a-row a-size-small"]/span[1]')
for i in rt:
    if(len(lap_rate)==10):
        break
    else:
        lap_rate.append(i.get_attribute('aria-label'))

pr=driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
for i in pr:
    if(len(lap_pri)==10):
        break
    else:
        lap_pri.append(i.text)
print(len (lap_pri),len(lap_rate),len(lap_title))
lap=pd.DataFrame({'Lap Titile':lap_title,'Lap Price':lap_pri,'Lap Rating':lap_rate})
lap


# In[31]:


driver.close()


# # Q9: Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida 
# location. You have to scrape company name, No. of days ago when job was posted, Rating of the company. 
# This task will be done in following steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the Job option as shown in the image
# 3. After reaching to the next webpage, In place of “Search by Designations, Companies, Skills” enter
# “Data Scientist” and click on search button
# 4. You will reach to the following web page click on location and in place of “Search location” enter
# “Noida” and select location “Noida”.
# 5. Then scrape the data for the first 10 jobs results you get on the above shown page.
# 6. Finally create a dataframe of the scraped data.
# Note: All the steps required during scraping should be done through code only and not manually.

# In[34]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.ambitionbox.com/")


# In[35]:


driver.find_element_by_xpath("/html/body/div[1]/nav/nav/a[6]").click()
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/input').send_keys('Data Scientist')
driver.find_element_by_class_name("ctas-btn-medium").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]").click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input').send_keys('Noida')
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/label').click()
time.sleep(2)


# In[36]:


company=[]
no_day=[]
com_rating=[]
com=driver.find_elements_by_xpath('//div[@class="company-info"]')
for i in com:
    company.append(i.text.split('\n')[0])
    if len(com_rating)==0:
        com_rating.append(i.text.split('\n')[2])
    else:
        com_rating.append(i.text.split('\n')[1])
com_rating=com_rating[:10]
company=company[:10]
days=driver.find_elements_by_xpath('//span[@class="body-small-l"]')
for i in days:
    no_day.append(i.text.split(','))
no_day=no_day[0::2]
print(len(company),len(com_rating),len(no_day))
jobs=pd.DataFrame({'Company':company,'Company Rating':com_rating,'No of Days ago':no_day})
jobs


# In[37]:


driver.close()


# # Q10: Write a python program to scrape the salary data for Data Scientist designation.
# You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary.

# In[40]:


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.ambitionbox.com/")


# In[41]:


driver.find_element_by_xpath('/html/body/div[1]/nav/nav/a[4]').click()
driver.find_element_by_xpath('/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input').send_keys('Data Scientist')
ds=driver.find_elements_by_xpath("//div[@class='suggestion_wrap tt-suggestion tt-selectable']")
for i in ds:
    if i.text == 'Data Scientist':   
        i.click() # click on “Data Scientist”
        break  


# In[42]:


com_name=[]
no_sal=[]
exp=[]
avg_sal=[]
min_sal=[]
max_sal=[]
cn=driver.find_elements_by_xpath('//div[@class="name"]')
for i in cn:
    com_name.append(i.text.split('\n')[0])
    no_sal.append(i.text.split('\n')[1].replace('based on',""))
#com_name
#no_sal
ex=driver.find_elements_by_xpath('//div[@class="salaries sbold-list-header"]')
for i in ex:
    exp.append(i.text.split('\n')[2])
#exp
asal=driver.find_elements_by_xpath('//p[@class="averageCtc"]')
for i in asal:
    avg_sal.append(i.text)
misal=driver.find_elements_by_xpath('//div[@class="value body-medium"]')
for i in misal:
    min_sal.append(i.text)
max_sal=min_sal[1::2]
min_sal=min_sal[0::2]
Salary=pd.DataFrame({'Company Name':com_name,'Number of Salary':no_sal,'Experiance':exp,'Average Salary':avg_sal,'Minimum Salary':min_sal,'Maximum Salary':max_sal})
Salary


# In[ ]:




