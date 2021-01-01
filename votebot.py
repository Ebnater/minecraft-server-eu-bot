from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
def vote(User):
    browser = Firefox(options=opts) #Open Browser
    print('Voting for ' + User + '!');
    browser.get('https://minecraft-server.eu/index/vote...' + User); #Vote Page for Minecraft Server
    time.sleep(5);
    if browser.find_elements_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]'):       #Cookie request
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
        print('Accepted Cookies');

    I=browser.find_element_by_xpath('//*[@id="captcha"]') #Scrolling to Vote Button
    print('Scrolling into View');
    browser.execute_script("arguments[0].scrollIntoView(true);", I)
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="captcha"]').click();
    print('Voting');
    time.sleep(10);
    c = browser.current_url
    if c == 'https://minecraft-server.eu/vote/fail/...': #Fail Page for Mineraft Server
        print('Already Voted/Failed to vote');
    else:
        print('Sucessfully voted');
    time.sleep(5);
    browser.close();
vote('Notch'); #Vote Command
