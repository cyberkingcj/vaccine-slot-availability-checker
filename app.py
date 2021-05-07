#cyberkingcj
import time
import winsound
from request_json import *
from inputs import *
from os import system
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(path_to_chromedriver)
driver.get('https://web.whatsapp.com')
sleep(5)
x = input('Press Enter after you finish scanning the code on WhatsaApp Web')
_ = system('cls')
request_no = 0
availablility = False

while True:
    responses = request_json()
    request_no += 1
    _ = system('cls')
    print("Searching for available slots. Loop:",request_no)
    for response in responses:
        for center in response.json()['centers']:
            for session in center['sessions']:
                if session['available_capacity'] > 0 and session['min_age_limit'] == age:
                    availablility = True
    if availablility == True:
        user = driver.find_element_by_xpath('//span[@title="'+name+'"]')
        user.click()
        msgbox = driver.find_element_by_xpath('//div[@class="_2A8P4"]')
        for _ in range(pings):
            winsound.Beep(600,(interval_between_pings//2)*1000)
            msgbox.send_keys("Vaccine is available now")
            winsound.Beep(600,(interval_between_pings//2)*1000)
            msgbox.send_keys(Keys.RETURN)
    else:
        print("No slots found, Trying again in ",t," seconds\n\n\n\n\n\nTo stop this app, just close this console window")
    sleep(t)
    
