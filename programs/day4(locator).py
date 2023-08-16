from selenium.webdriver import Chrome
from time import sleep

"""
locators
"""
"""
*in web-application before performing any action(enter, click, select, scroll etc..) we need to 
locate/find/inspect the element then we go locators.
*locating/finding/inspect the path of element in webpage is called as locator.
                        (or)
*the path of the element in html tree strcture is called as locator.

*we can find/locate a path in 8 ways  (or)   types of locators:
***************************************************************
1.id                5.linktext
2.name              6.partial linktext
3.classname         7.css selector
4.tagname           8.xpath

why locators:
=============
*before performing any action in application we need to find/locate/inspect the path of
element so we use locators.

*to find/inspect element in a webpage we use 2 methods,
1.find_element():
-----------------
*when we want to find single element then we go find_element() method.
*the return type of find_element() is "web-element". 
*there are 3 possibility in find_element(),
1.if the specified locator value is matching exactly single element.
2.if the specified locator value matching with multiple elements then find_element will return
1st matching element address.
3.if the specified locator value is not matching with any of element in web-page then it will throw
"NoSuchElement Exception". 

syntax:
-------
find_element(locator-name, locator-value)

2.find_elements():
------------------
*when we want find_multiple elements in a web-page then we go find_elements() methods.
*return type of find_elements() is list of web-elements.

syntax:
-------
find_elements(locator-name, locator-value)

how to get html code of element:
--------------------------------
*right on element in web-page --> click on inspect --> now html code will display.

web-element method:
===================
send_keys():
    *it will enter data/value into any text field.
click():
    *it will click on any web-element.

"""
# 1.id
# example on single matching element
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
username = driver.find_element("id", "a1")
username.send_keys("demo@123")
                #(or)
driver.find_element("id", "a1").send_keys("demo@123")
"""

# example on multiple matching element
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
pwd = driver.find_element("id", "a1")
pwd.send_keys("demo@123")
"""

# example on no matching element
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
pwd = driver.find_element("id", "a100")
pwd.send_keys("demo@123")
#NoSuchElementException: Message: no such element: Unable to locate element
"""

# ws to enter username, password in fb.com
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
un = driver.find_element("id", "email")
un.send_keys("demouser")
pwd = driver.find_element("id", "pass")
pwd.send_keys("demo@123")
"""

# ws to search for watch in amazon
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
src = driver.find_element("id", "twotabsearchtextbox")
src.send_keys("watch")
src_btn = driver.find_element("id", "nav-search-submit-button")
src_btn.click()
"""
#########################################################################################################################################
# 14-08-2023
# 2.name

# ws to search for watch in demowebshop
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
srch = driver.find_element("name", "q")
srch.send_keys("watch")
"""

# ws to enter usernam in irctc
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
driver.maximize_window()
driver.find_element("name", "userName").send_keys("demouser")
"""

# ws to enter rajajinagar location in swiggy.com
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.swiggy.com/")
driver.maximize_window()
driver.find_element("name", "location").send_keys("rajajinagar")
"""

"""
note:
-----
*when we right on a element in web-page if inspect opstion is not coming then, click ctrl+shift+i / F12.
"""
###############################################################################################################################
# 3.class name
# ws to click on login and enter all the details.
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.swiggy.com/")
driver.maximize_window()
driver.find_element("class name", "x4bK8").click()
driver.find_element("name", "mobile").send_keys("7876564545")
driver.find_element("class name", "a-ayg").click()
sleep(3)
driver.find_element("name", "name").send_keys("automation")
driver.find_element("id", "email").send_keys("automation@gmail.com")
driver.find_element("class name", "a-ayg").click()
"""

# ws to search for goa in flipkart booking
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.flipkart.com/travel/flights?otracker=nmenu_Flights")
driver.maximize_window()
sleep(4)
driver.find_element("class name", "_1w3ZZo._1YBGQV._2EjOJB.lZd1T6._2vegSu._2mFmU7").send_keys("goa")
"""

# ws to click on hotels in makemytrip
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element("class name", "chNavText.darkGreyText").click()
"""
"""
note:
-----
*when ever we are using class name as locator, if class name value consist of any space then replace the space with dot(.)
"""
##############################################################################################################################
# 4. tag name

# ws to click on movie in bookmyshow
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
driver.maximize_window()
driver.find_element("tag name", "a").click()
"""
# ws to click demowebshop
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("tag name", "a").click()
"""
"""
*tag name locator is not preffered in find_element() method because, find_element() will always return 1st matching element 
address.
*tag name locator is preffered in find_elements() method.
"""
############################################################################################################################################
# 15-08-2023
# 4.link text

"""
example on html code components:
--------------------------------

             attribute1                 attribute2    attribute3    attribute4
                 /                           /            /             /
<a        href="https://www.gmail.com"     id="a1"      class="c1"    name="n1">    Gmail  </a>
 |          |          |                    |   |        |      |      |     |        |
tag      attribute  attribute              an   av       an     av     an    av      text
name     name       value


*link text locator will work for only a element which is developed with "a" tag and some time with "span" tag.
*link text is a case senstive.
"""

# ws to click on facebook linkin dummy webpage
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
link = driver.find_element("link text", "Facebook")
link.click()
"""

# ws to click on best seller in amazon
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
link = driver.find_element("link text", "Best Sellers")
link.click()
"""

# ws to click on dream11 in demrem11 fantasycricket
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.dream11.com/fantasy-cricket")
driver.maximize_window()
link = driver.find_element("link text", "Dream11")
link.click()
"""

# ws to click on travel info and metro timings in bmrcl
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://english.bmrc.co.in/#/")
driver.maximize_window()
driver.find_element("link text", "TRAVEL INFO").click()
driver.find_element("link text", "Metro Timings").click()
"""

# ws to click on show more and click on onion in bigbasket
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
sleep(4)
driver.find_element("link text", "Show More").click()
sleep(5)
driver.find_element("link text", "Onion (Loose)").click()
"""
############################################################################################################################################
# 6.partial link text
"""
*in this locator we will specify partial/part of text present in link text.
*partial text can be part and it is case senstive.
"""
# ws to click on other lang exist in seleniumdev
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.selenium.dev/downloads/")
driver.maximize_window()
driver.find_element("partial link text", "languages").click()
"""

# ws to click on lakme product in lakme
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.lakmeindia.com/")
driver.maximize_window()
driver.find_element("partial link text", "Skin Dew Satin").click()
"""
"""
assignment question:
--------------------
https://demowebshop.tricentis.com/
ws to click on register and fill all details and register from demo webshop.

share the automation script to 
assignmentsql@gmail.com
"""
#####################################################################################################################################
# 16-08-2023
# 7.css selector
"""
*css stands for "cascading style sheet".
*basically css will be used for web-page design an decoration.
(decoration means style, font-size, font-family, height,width, bg color, etc...)
*in automation we use css selector expression for inspecting an element.

sample html code:
-----------------
<a  href="https://www.facebook.com"   id="a1"   class="c1">  facebook </a>
 |               |                       |            |         |
tag          attribute1               attribute2   attribute3  text
name

syntax on css expression:
-------------------------
tagname[attribute_name = 'attribute_value']

example on css expression:
--------------------------
a[href='https://www.facebook.com']
a[id='a1']         ->"a#a1"
a[class='c1']      ->"a.c1"

note:
-----
*if attribute name is class in css expression then replace class with dot(.)
*if attribute name is id in css expression then replace id with hash(#)

how to verify css expression:
-----------------------------
*right click on element and click on inspect now html code wil apear.
*click on ctrl+f now search for string/selector text box will appear.
*enter css expression and click on enter.
->if css expression is valid then,
    *element will be highlight
    *code will highlight in yellow color
    *count will display 1of1
->if css expression is in-valid then,
    *element will not highlight
    *code will not highlight in yellow color
    *count will display 0of0

drawbacks:
----------
*we can't write text in css expression.
*if the css expression is matches with multiple elements, then we can't inspect/get particular 
element css expression.
"""
# ws to search for chicken and click 1st link
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.licious.in/search")
driver.maximize_window()
driver.find_element("css selector", "input[class='RealSearchBar_searchbar__zap4G']").send_keys("chicken")
sleep(3)
driver.find_element("css selector", "div[class='SearchProductTile_item_description__e3i11']").click()
"""

# ws to automate on dunzo
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.dunzo.com/bangalore")
driver.maximize_window()
driver.find_element("css selector", "button[data-tip='header-business-options']").click()
driver.find_element("css selector", "div[class='sc-AxjAm StDqM sc-jbkzle-4 PCMWw']").click()
driver.find_element("css selector", "input[name='phone']").send_keys("8971272837")
driver.find_element("css selector", "input[type='email']").send_keys("automation@gmail.com")
driver.find_element("css selector", "input[type='password']").send_keys("automation@gmail.com")
driver.find_element("css selector", "svg[class='sc-Axmtr osNtE sc-fznyAO gTtLDV']").click()
driver.find_element("css selector", "button[class='sc-AxiKw KKPII sc-1q182yc-4 hpwiSq']").click()
"""
"""
assigmnet
---------
launch youtube --> search for a song --> play a song
by ussing css selector locator
"""

"""
>cd C:\\Users\\Admin\\Desktop\\pyselenium\\Selenium_M1
>git init
Initialized empty Git repository in C:/Users/Admin/Desktop/pyselenium/Selenium_M1/.git/
>git config --global user.name "sunilakash47"
>git config --global user.email "assignmentsql@gmail.com"
>git status
>git add "programs/Sample"
>git commit -m "sample file commiting"
>git log
>git push "https://github.com/sunilakash47/SELENIUM_M1.git" master
                  |--> git repository URL


how to download:
----------------
*create a folder where need to download
>cd C:\\Users\\Admin\\Desktop\\pyselenium\\new_folder
>git clone https://github.com/sunilakash47/SELENIUM_M1.git
                  |-->git repository
"""