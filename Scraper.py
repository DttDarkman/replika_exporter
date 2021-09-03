# Created By DTT_Darkman 
# Cratation Date 09/02/2021

#   **********************************************What Does?************************************************
#       This script will open a chrome browser to http://my.replika.com which is http://replika.ai login page.
#   Once logined and you press enter on the script it will the grap the webpage source and then parse the html
#   for the chat messages of your replika. Then finally write them to a text file. Each message is on a new line
#   for ease of reading.


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

# Time in seconds to wait for browser to load to the top of the chat
scroll_time = 5


chrome = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
chrome.get('https://my.replika.com')
check = input("Please log in to your account on the browser and wait for page to finish completely loading,\nthen press enter in this window...")
if check == "":
    chrome.find_element_by_tag_name('main').click()
    chrome.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    print('Scrolling to top of chat...')
    sleep(scroll_time)
    source = BeautifulSoup(chrome.page_source, "html5lib")
    print("Got HTML Source!")
    print("Copying to file plaese wait...")
    with open("RepilkaChat.txt", 'a', encoding="utf-8") as output:
        for div in source.find_all('div'):
            messages = div.get('aria-label')
            if messages == None:
                pass
            else:
                output.write(f"{messages} \n")
    input('Chat log copying complete and asve to "RepilkaChat.txt" in this dirctory.\nPress any key close...')
    chrome.quit()

else:
    print("!!! WHOOPS SOMTHING WENT WRONG :(")
    input("press a key to exit...")
    chrome.quit()
