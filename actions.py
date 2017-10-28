import elements
from selenium import webdriver

driver = webdriver


#Manage starting up the drivers
def getDriver(browser):
    global driver
    if browser == "Chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
        return driver
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.maximize_window()
        return driver
    else:
        print("Please select Firefox or Chrome")


def navigate(url):
    driver.get(url)


def click(element):
    element.click()


def write(element,imput):
    element.send_keys(imput)

def getEle(locator,type):
    if type == "id":
        elem = driver.find_element_by_id(locator)
        return elem
    elif type == "class":
        elem = driver.find_element_by_class_name(locator)
        return elem
    elif type == "class":
        elem = driver.find_element_by_class_name(locator)
        return elem


def exit():
    driver.quit()