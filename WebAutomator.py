from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import psutil

options = Options()
gecko = 'geckodriver.exe'


browser = webdriver.Firefox()
browser.get('http://vulgarlang.com')

submit = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/main/article/div[1]/div[1]/center/button")

submit.click()

wordList = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/main/article/div[1]/div[3]/div[1]/div[4]/ul").text

browser.close()
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == gecko:
        proc.kill()

print(wordList)
