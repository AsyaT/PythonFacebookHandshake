from selenium import webdriver

import DatabaseProvider
import FacebookActions

def RecurrentFriendsSaver(browser, current_user_id, distination_user_id):

	FacebookActions.VisitProfilePage(browser, current_user_id)
	current_person = FacebookActions.CreateStartUserOnProfilePage(browser, current_user_id)
	
	curent_user_node = DatabaseProvider.CreatePersonNode(current_person)
	
	FacebookActions.OpenFriendsTab(browser)
	f_l = FacebookActions.ListOfFriends(browser)
	
	for friend in f_l:
		friend_node = DatabaseProvider.CreatePersonNode(friend)
		DatabaseProvider.MakeFriends(curent_user_node,friend_node)
		if friend.id == distination_user_id:
			print("Distination user is found!")
			break;
		else:
			#open tab
			browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
			RecurrentFriendsSaver(friend.id, distination_user_id)


browser = webdriver.Firefox()
FacebookActions.LoginIntoFacebook(browser)

RecurrentFriendsSaver(browser,"100000766204700","888")

browser.close()
