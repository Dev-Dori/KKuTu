from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.get("https://kkutu.io/?server=0")

def now():
    element = driver.find_element_by_class_name("jjoDisplayBar")
    return element.text[1] #:element.text.index("\n")

