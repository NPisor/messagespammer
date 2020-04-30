#import selenium to handle browser control with send keys to handle input

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from settings import fbemail,fbpassword

# Take in email and password from settings.py for anonimity and prompt user to spam messages to
facebookEmail = fbemail
facebookPassword = fbpassword
friendName = input("Enter a friend's name: ")
selection = input("Which file would you like to send to a friend? (AllStar-SmashMouth, or Whole New World-Aladdin): ")
sendDelay = 1;

# Open FBMessenger (navigate to chromedriver local location)
driver = webdriver.Chrome(r'C:\Users\chromedriver.exe')
driver.get('https://www.messenger.com/')
time.sleep(2)


# Login on messenger login page with given credentials
email = driver.find_element_by_id("email").send_keys(facebookEmail)
password = driver.find_element_by_id("pass").send_keys(facebookPassword)
driver.find_element_by_id("loginbutton").click()
time.sleep(3)

#Search for username of victim and open chat window
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()


text_file = []

#Check user selection to send to victim and print out word by word at 1 sec intervals
if selection == "AllStar" or "SmashMouth":
    with open('allstar.txt', "r") as f:
        for line in f.readlines():
            for word in line.split():
                insertMessage = driver.find_element_by_class_name('_1mj')
                insertMessage.send_keys(word, Keys.ENTER)
                time.sleep(sendDelay)

if selection == "Whole New World" or "Aladdin":
    with open('wholenewworld.txt', "r") as f:
        for line in f.readlines():
            for word in line.split():
                insertMessage = driver.find_element_by_class_name('_1mj')
                insertMessage.send_keys(word, Keys.ENTER)
                time.sleep(sendDelay)