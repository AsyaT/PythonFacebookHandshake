from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
from Person import Person
import DatabaseProvider
from urllib.parse import urlparse
from urllib.parse import parse_qs

import FacebookLogin

browser = webdriver.Firefox()
FacebookLogin.LoginIntoFacebook(browser)

# go to page of person one

start_person_id = "100000766204700"
browser.get('https://www.facebook.com/profile.php?id=' + start_person_id)
full_person_name = browser.find_element_by_xpath("//span[@id='fb-timeline-cover-name']/a").text
person_1 = Person(start_person_id, full_person_name)

print("Person 1 is " + person_1.name + " ID = " + person_1.id)

node_1 = DatabaseProvider.CreatePerson(person_1)
# go to friends
friends_tab = browser.find_element_by_xpath('//a[@data-tab-key="friends"]')
friends_tab.click()
print("Start scroll")

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print("End scroll")


try:
	friends_page = WebDriverWait(browser, 555).until(EC.presence_of_element_located((By.ID, "pagelet_timeline_medley_friends")))
	print("List of friends is loaded")
	friends_container = browser.find_element_by_xpath('//ul[@class="uiList _262m _4kg"]')
	friends_list = friends_container.find_elements_by_xpath('//div[@class="uiProfileBlockContent"]//a')

	for link_element in friends_list:
		print(link_element.get_attribute("innerHTML"))
		url_link_to_friend = link_element.get_attribute("data-hovercard")
		print(url_link_to_friend)
		if url_link_to_friend != None :
			parsed = urlparse(url_link_to_friend)
			print(parsed)
			all_query_params = parsed.query
			print("Query parameters: "+all_query_params)
			qs_array = parse_qs(all_query_params)
			print (qs_array)
			friend_id = qs_array['id'][0]
			print("Friend id " + friend_id)
			friend_name = link_element.text
			print("Friend name "+friend_name)
			person_2 = Person(friend_id, friend_name) 
			node_2 = DatabaseProvider.CreatePerson(person_2)
			DatabaseProvider.MakeFriends(node_1,node_2)
		print("---------------------")
	
except NoSuchElementException:
	print ("This is not friends page!")



browser.close()
