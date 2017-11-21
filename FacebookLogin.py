from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import Constants
from Person import Person
import DatabaseProvider

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/login.php')

# insert email and password
email_field = browser.find_element_by_id("email")
email_field.send_keys(Constants.LOGIN)

password_field = browser.find_element_by_id("pass")
password_field.send_keys(Constants.PASSWORD)

submit_button = browser.find_element_by_id("loginbutton")
submit_button.submit()

try:
	top_profile_element_id = "profile_pic_header_" + Constants.ID
	profile_page = WebDriverWait(browser, 35).until(EC.presence_of_element_located((By.ID, top_profile_element_id)))
	print ("Profile page is loaded successfuly!")
except NoSuchElementException:
	print ("This is not profile page!")

# go to page of person one

start_person_id = "100009757303780"
browser.get('https://www.facebook.com/profile.php?id=' + start_person_id)
full_person_name = browser.find_element_by_xpath("//span[@id='fb-timeline-cover-name']/a").text
person_1 = Person(start_person_id, full_person_name)

print("Person 1 is " + person_1.name + " ID = " + person_1.id)

node_1 = DatabaseProvider.CreatePerson(person_1)

friends_tab = browser.find_element_by_xpath('//a[@data-tab-key="friends"]')
friends_tab.click()

person_2 = Person("", "") # TODO: find first friend
node_2 = DatabaseProvider.CreatePerson(person_2)

DatabaseProvider.MakeFriends(node_1,node_2)
