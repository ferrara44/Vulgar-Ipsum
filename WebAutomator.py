from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import psutil

options = Options()
gecko = 'geckodriver.exe'

options.add_argument('-headless')
browser = webdriver.Firefox(options=options)
print("Firefox Initialized successfully")
browser.get('http://vulgarlang.com')
print("Accessing VulgarLang")
submit = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/main/article/div[1]/div[1]/center/button")
print("Button Found")
submit.click()
print("Button Clicked")
wordList = browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/main/article/div[1]/div[3]/div[1]/div[4]/ul").text
print("WordList Copied")
browser.close()
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == gecko:
        proc.kill()

print(wordList)
