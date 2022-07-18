from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

installd=ChromeDriverManager().install()
driver=webdriver.Chrome(installd)
driver.get("https://www.itechdevices.ae/media/catalog/product/cache/1/image/650x/e870e2e090f1031716bf3273122f9d39/1/1/11265-05-20g.jpg")
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end")


#Using my zeus file I am not able to save the screenshot taken in the correct folder but I want to test my code with webpage with multiple products
