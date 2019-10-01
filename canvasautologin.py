from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

usernameString = ''
passwordString = ''
cap = DesiredCapabilities().CHROME
cap["marionette"] = False

browser = webdriver.Chrome(desired_capabilities=cap, executable_path=r"/Users//Documents/chromedriver")
browser.get("https://canvas.njit.edu")
loginToCanvas = browser.find_element_by_xpath('/html/body/div[1]/div[1]/header/div[2]/div/nav/div/ul/li[2]/a')
loginToCanvas.click()
username = browser.find_element_by_id('username')
username.send_keys(usernameString)
password = browser.find_element_by_id('password')
password.send_keys(passwordString)

loginButton = browser.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[3]/button')
loginButton.click()