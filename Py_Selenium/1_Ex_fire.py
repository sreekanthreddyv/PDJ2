from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# Enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview Questions")
search_field.submit()

# get the list of elements which are displayed after the search
# curently on result page using find_elements_by_class_name method
lists = driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print("Found {} searches.".format(len(lists)))

for listitem in lists:
	print(listitem)
# close the browser window
driver.quit()