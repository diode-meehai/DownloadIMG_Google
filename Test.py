# https://www.youtube.com/watch?v=cImRC-AZs48
# https://pycheat.com/download_img.php

from selenium import webdriver
from bs4 import BeautifulSoup
# import requests
import urllib.request
import time
# import sys
import os
from tqdm import tqdm

# taking user input
print("What do you want to download?")
download = input()

# create folder
try:
    os.mkdir(download)
except OSError:
    print ("Creation of the directory %s failed" % download)

site = 'https://www.google.com/search?tbm=isch&q=' + download

# providing driver path
driver = webdriver.Firefox(executable_path='./FirefoxWebDriver/geckodriver.exe')

# passing site url
driver.get(site)

# if you just want to download 10-15 images then skip the while loop and just write
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


# below while loop scrolls the webpage 7 times(if available)

i = 0

while i < 10:
    # for scrolling page
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    try:
        # for clicking show more results button
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(5)
    i += 1

# parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')

# closing web browser
driver.close()

# scraping image urls with the help of image tag and class used for images
img_tags = soup.find_all("img", class_="rg_i")
#print('img_tags: ' + str(img_tags))
count = 0
for i in tqdm(img_tags):
    # print(type(i))
    # print(i)
    # if i.get('src') and i.get('data-src'):
    #     print(i['src'])
    try:
        if i.get('src'):
            # passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], './' + download + '/' + str(count) + ".jpg")
            print(i)
        elif i.get('data-src'):
            urllib.request.urlretrieve(i['data-src'], './' + download + '/' + str(count) + ".jpg")
            print(i)
        count += 1
        print("Number of images downloaded = " + str(count), end='\r')
    except Exception as e:
        pass