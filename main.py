from  follower_insta import InstaFollower

driver=InstaFollower()
driver.login()

driver.find_followers()

driver.follow()

driver.quit_browser()