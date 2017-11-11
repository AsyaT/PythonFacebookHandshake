from selenium import webdriver
import Constants

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/login.php')

# insert email and password
email_field = browser.find_element_by_id("email")
email_field.send_keys(Constants.LOGIN);

password_field = browser.find_element_by_id("pass")
password_field.send_keys(Constants.PASSWORD);

submit_button = browser.find_element_by_id("loginbutton");
submit_button.submit();

# go to page of person 1

