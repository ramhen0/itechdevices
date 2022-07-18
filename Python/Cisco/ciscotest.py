# this is a test file and only to be used to see if everything on other end works
# outer_iterations value  was replaced with 2 so that it only gives us first page results
# chromedriver location needs to be inside the python folder


from bs4 import BeautifulSoup
import requests
import math
import csv
from selenium import webdriver
from time import sleep
import os

url=requests.get("https://www.itechdevices.ae/cisco/cisco-memory-flash.html?p=1").text

soup = BeautifulSoup(url,'lxml')
#this is my list of lists
all_products=[]
#this is my each product list which would be inside list of lists
each_product=[]

#extract total iteration number to set the outer for loop

total = soup.find("div", class_="count-container")
number=total.find("p").text.strip()
total_number=number[-2:]
#converting the string to integer
outer_iterations=math.ceil(int(total_number)/12)+1

for x in range(1, 2):
#
#main url
    url=requests.get("https://www.itechdevices.ae/cisco/cisco-memory-flash.html?p="+str(x)).text
    soup = BeautifulSoup(url,'lxml')
    links=soup.find_all('li',class_="item")
#mid for loop to go between the 12 products on each page
    for link in links:
        print("New Product being Processed.\n")
        product_link=link.a["href"]
        inside_url=requests.get(product_link).text
        soup = BeautifulSoup(inside_url,'lxml')
    #This is so we can get the name
        product_info=soup.find("div",class_="product-primary-column product-shop grid12-5")
        product_name=product_info.h1.text

    #Now we have the name, we need to get SKU, detail and availability. Had to use soup again because they could not be found product_info
        product_detail=soup.find_all("td", class_="td-sp")
    #        print("")
    #    print(product_name)
    #append the name here to each product
        each_product.append(product_name)
        for x in range(0,3):
            product1=product_detail[x].text
    #        print(product1)
            each_product.append(product1)
    #        print("")

    # we will add the additonal information from the table by finding it and then appending into the all_products
        additonal_code=soup.find("table", class_='data-table')
        additonal_code_string=str(additonal_code)
    #this is important step, solved the problem with the excel file
        each_product.append(additonal_code_string)

        all_products.append(each_product)

    # we will add the additonal information from the table by finding it and then appending into the all_products



    #    print(all_products)
        #this solved my problem for getting individual list
        each_product=[]

    #Here I will insert the code to extract the image

        image_info= soup.find("div", class_="product-img-column grid12-4")
        #for link in links:
        ##    print(slink)
        product_image_link=image_info.a["href"]

        driver=webdriver.Chrome("C:\\Users\\Mehra\\Desktop\\Python\\chromedriver_here\\chromedriver.exe")
        driver.get(product_image_link)
        sleep(1)

        product_name=product_name.replace('"', "inch")
        current_directory=os.getcwd()
        driver.save_screenshot(current_directory+ "\\" +product_name+ ".png")
        #driver.get_screenshot_as_file(product_name+".png")
        driver.quit()
        print("end")

    '''
    #this is what I had before i changed it
            for product in product_detail:
                product1=product.text
            #print(product_detail)
                print(product1)
                counter=counter+1
                print(counter)
    '''

header= ["Name",'SKU', 'Detail', 'Availability', "Additional Info"]

#getting the current file name so that we dont need to manually update inside
file_name=os.path.basename(__file__)

with open(file_name[:-3]+'.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(all_products)
