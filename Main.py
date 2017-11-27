from selenium import webdriver

import DatabaseProvider
import FacebookActions

browser = webdriver.Firefox()
FacebookActions.LoginIntoFacebook(browser)

start_person_id = "100000766204700"

FacebookActions.VisitProfilePage(browser, start_person_id)
node_1 = DatabaseProvider.CreatePersonNode(FacebookActions.CreateStartUserOnProfilePage(browser, start_person_id))

FacebookActions.OpenFriendsTab(browser)

friends_list = FacebookActions.ListOfFriends(browser)
for friend in friends_list:
	friend_node = DatabaseProvider.CreatePersonNode(friend)
	DatabaseProvider.MakeFriends(node_1,friend_node)
	

browser.close()
