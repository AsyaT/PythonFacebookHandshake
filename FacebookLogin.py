
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import Constants

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

