from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
def vote(User):
    browser = Firefox(options=opts)
    browser.install_addon('/home/eric/votebot/extensions/uBlock0@raymondhill.net.xpi', temporary=True)
    print('Inserting uBlock')
    #browser.find_element_by_class_name('sc-ifAKCX dvvOSu').click()
    #time.sleep(5)
    #browser.find_element_by_class_name('btn btn-primary btn-block').click()
    print('Voting for ' + User + '!');
    browser.get('Minecraft-server.eu_vote_site');
    #element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]'))
    #WebDriverWait(browser, 10000).until(element_present)
    time.sleep(5);
    if browser.find_elements_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]'):
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
        print('Accepted Cookies');

    browser.execute_script('document.body.style.MozTransform = "scale(0.5)";')
    print('Scaling to 0.5');
    time.sleep(10);

    I=browser.find_element_by_xpath('//*[@id="playername"]')
    print('Scrolling into View');
    browser.execute_script("arguments[0].scrollIntoView(true);", I)
    time.sleep(10)
    
    player=browser.find_element_by_xpath('//*[@id="playername"]')
    player.send_keys(User);
    print('Inserting Username')
    
    I=browser.find_element_by_xpath('//*[@id="captcha"]')
    print('Scrolling into View');
    browser.execute_script("arguments[0].scrollIntoView(true);", I)
    time.sleep(10);

#browser.find_element_by_xpath('/html/body/div[2]/div/main/div[6]/div/div[2]/div[2]/button').click();
    browser.find_element_by_xpath('//*[@id="captcha"]').click();
    print('Voting');
    time.sleep(10);
    c = browser.current_url
    if c == 'https://minecraft-server.eu/vote/fail/208F7':
        print('Already Voted/Failed to vote');
    else:
        print('Sucessfully voted');
    time.sleep(5);
    browser.close();
vote('Minecraft_Name');
