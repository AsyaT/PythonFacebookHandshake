
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from urllib.parse import urlparse
from urllib.parse import parse_qs

import Constants
from Person import Person

def LoginIntoFacebook(browser):
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

def VisitProfilePage(browser, user_id):
	browser.get('https://www.facebook.com/profile.php?id=' + user_id)
	
	
def CreateStartUserOnProfilePage(browser,user_id):
	full_person_name = browser.find_element_by_xpath("//span[@id='fb-timeline-cover-name']/a").text
	return Person(user_id, full_person_name)
	
def ListOfFriends(browser):
	friends_container = browser.find_element_by_xpath('//ul[@class="uiList _262m _4kg"]')
	friends_list = friends_container.find_elements_by_xpath('//div[@class="uiProfileBlockContent"]//a')

	for link_element in friends_list:
		url_link_to_friend = link_element.get_attribute("data-hovercard")
		if url_link_to_friend != None :
			parsed = urlparse(url_link_to_friend)
			all_query_params = parsed.query
			qs_array = parse_qs(all_query_params)
			friend_id = qs_array['id'][0]
			print("Friend id " + friend_id)
			friend_name = link_element.text
			print("Friend name "+friend_name)
			person_2 = Person(friend_id, friend_name) 
			yield person_2
		print("---------------------")


def OpenFriendsTab(browser):
	# go to friends
	friends_tab = browser.find_element_by_xpath('//a[@data-tab-key="friends"]')
	friends_tab.click()
	
	try:
		friends_page = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, "pagelet_timeline_medley_friends")))
		print("List of friends is loaded")
		SCROLL_PAUSE_TIME = 2
		last_height = browser.execute_script("return document.body.scrollHeight")
		while True: 
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(SCROLL_PAUSE_TIME)
			new_height = browser.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
	except NoSuchElementException:
		print ("This is not friends page!")
