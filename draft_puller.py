# this script should open an existing draftlol link and find what champs are picked and banned, then store them in
# bannedchampions.txt in order to be used for draftcreator.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from os import path


def load_draft(url):
    try:
        options = Options()
        options.headless = True
        browser = webdriver.Chrome(options=options)
        browser.get(url)
        time.sleep(1)  # note that this page will take longer to load due to images
        bluePick = browser.find_element('class name', 'roomPickColumn.blue').find_elements('tag name', 'p')
        redPick = browser.find_element('class name', 'roomPickColumn.red').find_elements('tag name', 'p')
        # I noticed each pick is named under the p tag, I can pull the names of each champ from there
        blueBan = browser.find_element('class name', 'roomBanRow.blue').find_elements('tag name', 'img')
        redBan = browser.find_element('class name', 'roomBanRow.red').find_elements('tag name', 'img')
        if path.exists('bannedchampions.txt'):
            banList = open('bannedchampions.txt','a')
            banList.write('\n')
        else:
            banList = open('bannedchampions.txt', 'w')
        # If the file exists, we add a space before adding more champions. If it does not exist, we create the file
        for element in bluePick:
            banList.write(element.get_property('textContent')+'\n')
        for element in redPick:
            banList.write(element.get_property('textContent')+'\n')
        for element in blueBan:
            banList.write(element.get_property('alt')+'\n')
        for element in redBan:
            banList.write(element.get_property('alt')+'\n')
        # note that we are not expecting duplicates to occur in the list due to expecting champions to not be
        # picked/banned if they were already banned or picked in previous drafts. If this was not the case we could
        # check if the ban is already in the list but if the bot is used, this is redundant
        browser.close()
        banList.close()
        return '`Successfully updated banned champions list`'
    except Exception as e:
        print(e)
        return '`Your draft could not be processed, check the URL or ask Terry to check the error`'
