from time import sleep
from selenium.webdriver import Chrome

from main import FireFox

"""
launch empty browser:
=====================
*to launch any empty browser developer as written code inside a browser specific class.
*if we create an object for browser specific class then an empty browser will be launched/opened.
*each browser class constructor will accept 1 argument that is, path of driver executable file. 

*we can specify driver executable path in 2 ways,
1.absolute path:
    *it is a path from root to child.
    (usually will wil not preffered this bcz when we give a code with absolute path, a path
    will vary from machine to machine so chances of code will fail)
2.relative path:
    *it is a shortest/optimized path.
    *. --> 1st dot(.) indicate current file/location
    *. --> 2nd dot(.) will move to project level
    */ --> indicate it will navigate to child
"""
# write a script to launch empty chrome browser
# launching empty chrome browser with absolute path
# c = Chrome(executable_path=r"C:\Users\Admin\Desktop\pyselenium\Selenium_M1\drivers\chromedriver.exe")

# launching empty chrome browser with relative path
# c = Chrome(executable_path="../drivers/chromedriver.exe")
################################################################################################################
from selenium.webdriver import Edge

# write script to launch empty edge browser
# launching empty edge browser with absolute path
# e = Edge(executable_path=r"C:\Users\Admin\Desktop\pyselenium\Selenium_M1\drivers\msedgedriver.exe")

# launching empty edge browser with absolute path
# e = Edge(executable_path="../drivers/msedgedriver.exe")

##########################################################################################################
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# write a script to launch empty firefox browser
# way1:
# f = Firefox(executable_path=r"C:\Users\Admin\Desktop\pyselenium\Selenium_M1\drivers\geckodriver.exe")
# the above if it is not working then follow the below code.

# way2:
# o = Options()
# o.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"   #this is a path of firefox exe file in "C" drive
# f = Firefox(executable_path=r"../drivers/geckodriver.exe", options=o) #this is a path of drivere executable files in 'drivers' folder in pycharm

##############################################################################################################################
# 09-08-2023

# driver = Chrome(executable_path="../drivers/chromedriver.exe")
"""
*driver is a reference variable, which holds chrome class object.
*in simple words 'driver' is a variable which hold launched browser address.
"""
"""
closing browser methods:
========================
*to close browser we have 2 methods,
1.close():
    *it will close only the current window/tab.

2.quit():
    *it will close entire browser.
"""
# ws to close the current tab/window
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.close()

# ws to close entire browser
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.quit()
########################################################################################################
"""
get():
    *to enter URL we use get() method.
    *it will accept both secured(https) and non-secured(http) protocols urls.
    *it will wait until page get's load.
"""
# ws to enter fb.com and close a browser
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("http://www.fb.com")
# driver.close()

# ws to enter/launch ajio.com and close a browser
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.close()

# example on with http/https protocol urls
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("www.insta.com")
# driver.close()
# selenium.common.exceptions.InvalidArgumentException: Message: invalid argument

##################################################################################################################
"""
browser commands:
=================
1.forward()
    *to click on forward arrow in browser we use forward() method.
2.back():
    *to click on backward arrow in browser we use back() method.
3.refresh():
    *to click on refresh in browser we use refresh() method.
"""
# ws to perform backward, forward and refresh action in browser
# driver = Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.google.com")
# driver.back()       #click backword arrow
# driver.forward()    #click forward arrow
# driver.refresh()    #refresh a page
# driver.close()