import selenium
import elements
import actions

from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# create a new Firefox session
actions.getDriver("Chrome")

#testing git

# navigate to the application home page
actions.navigate(elements.Google)

actions.click(elements.search)

# enter search keyword and submit
actions.write(elements.search , "Selenium WebDriver Interview questions")

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + "searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   #print (listitem)
   i=i+1
   if(i>10):
      break

# close the browser window
actions.exit()