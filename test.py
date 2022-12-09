

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep 






putanja_raf = 'https://raf.edu.rs/'

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get(putanja_raf)

osnovne_akademske_nauke = driver.find_element(By.ID, 'основне-академске-студије').click()

# print(osnovne_akademske_nauke.text)


sleep(5)

driver.quit()