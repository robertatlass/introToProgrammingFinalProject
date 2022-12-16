
############## open website with selenium and webdriver ###################
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By

# URL = 'https://herenow.com/results/#/races/20899/results'

# chrome_driver = "Code\Projects\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver)
# driver.get(URL)
# sleep(5)
# # spans = driver.find_element(By.TAG_NAME, "span")
# # print(type(spans))
# searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")
# print(searchresults[0].text)

# datafound = []

# for i in searchresults:
#     if len(i.text) > 0:
#         datafound.append(i.text)
#     if len(datafound) > 45:
#         break

# print(datafound)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

packed_extension_path = '/path/to/packed/extension.crx'

options = Options()
options.add_extension(packed_extension_path)
driver = webdriver.Chrome(options=options)

