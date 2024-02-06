from selenium import webdriver
from selenium.webdriver.common.by import By

def test_lamda_test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flightradar24.com/data/airports/pnq")
    print("Title:", driver.title)
    # get element
    # element = driver.find_element(By.LINK_TEXT, "Text of Link")
    element = driver.find_element('//*[@class ="hide-mobile-only ng-binding"]')
    # get text
    print(element.text)

    driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()
# def test_lamda_test2():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.selenium.dev/")
#     print("Title:", driver.title)

