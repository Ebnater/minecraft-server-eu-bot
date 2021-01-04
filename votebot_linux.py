from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import yaml
import time
import os

with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        username_file = data['username_file']
        server = data['server']
        headless = data['headless']

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

opts = Options()
def vote(User):
    print('Operating in Linux Mode')
    browser = Firefox(options=opts)
    browser.install_addon(CURR_DIR + '/uBlock0@raymondhill.net.xpi', temporary=True)
    print('Inserting uBlock')

    print('Voting for ' + User + '!');
    browser.get(server);

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

if headless == '1':
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
with open(username_file,'r') as file:
    for line in file:
        for word in line.split():
            vote(word);
