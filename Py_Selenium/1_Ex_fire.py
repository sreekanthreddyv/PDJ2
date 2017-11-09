# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # create a new Firefox session
# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.maximize_window()

# # Navigate to the application home page
# driver.get("http://www.google.com")

# # get the search textbox
# search_field = driver.find_element_by_id("lst-ib")
# search_field.clear()

# # Enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview Questions")
# search_field.submit()

# # get the list of elements which are displayed after the search
# # curently on result page using find_elements_by_class_name method
# lists = driver.find_elements_by_class_name("_Rm")

# # get the number of elements found
# print("Found {} searches.".format(len(lists)))

# for listitem in lists:
# 	print(listitem)
# # close the browser window
# driver.quit()
import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://www.google.com/")
        inst.driver.title

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("Selenium Webdriver interview questions")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, len(lists))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.send_keys("Python class")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, len(list_new))

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()


# Test Suite Creation
import unittest
from SeleniumPythonRefactorTestCase import SearchText
from SeleniumPythonMultipleTests import HomePageTest

# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
