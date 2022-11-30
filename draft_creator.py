# this script opens draftlol, ban champions from a list, then returns the draft links in a list

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from os import path


def create_draft():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(options=options)
        browser.get('https://draftlol.dawe.gg/')
        time.sleep(0.5)  # just to let page load, shouldn't take too long
        browser.find_element('class name', 'advancedOptionsButton').click()
        time.sleep(0.5)  # let advance options load
        championSearchBox = browser.find_element('class name', 'champsFiltersSearch')
        championSearch = championSearchBox.find_element('tag name', 'input')  # get search box


        def ban_champion(champName):
            # This function will search for a champion, click it in order to ban it, then clear the search field
            # Vi and Ornn return multiple champs when searched, need exceptions
            # Note that the code used for these two could essentially be used for the whole function, but the else
            # statement should be faster than storing and looking through a list of 146 champions everytime
            if champName == 'Ornn\n':
                championSearch.send_keys(champName)
                championList = browser.find_element('class name', 'roomChampionsList').find_elements('tag name', 'img')
                for element in championList:
                    if (element.get_property('alt')+"\n") == champName:
                        browser.execute_script('arguments[0].click()', element)
            elif champName == 'Vi\n':
                championSearch.send_keys(champName)
                championList = browser.find_element('class name', 'roomChampionsList').find_elements('tag name', 'img')
                for element in championList:
                    if element.get_property('alt') == 'Vi':
                        browser.execute_script('arguments[0].click()', element)
            else:
                championSearch.send_keys(champName)
                champion = browser.find_element('class name', 'roomImgListItem')
                browser.execute_script('arguments[0].click()', champion)
            championSearch.clear()


        if path.exists('bannedchampions.txt'):
            banList = open('bannedchampions.txt', 'r')
            banArray = []
            for line in banList:
                if line != '\n':  # this is needed to ignore the empty line inserted between drafts
                    banArray.append(line)
            for name in banArray:
                ban_champion(name)
            banList.close()

        # if bannedchampions.txt exists, then an array is formed using the list and then banned
        # if the txt file is not there, a fresh draft will be made
        browser.find_element('class name', 'sendButton').click()
        time.sleep(0.5)  # After banning the champions, click the create button to create the draft and wait for it to load
        blueDraft = browser.find_element('class name', 'inputBlue').get_property('defaultValue')
        redDraft = browser.find_element('class name', 'inputRed').get_property('defaultValue')
        slicePoint = blueDraft.rindex('/')
        spectate = blueDraft[:slicePoint]
        # Get the links for the drafts, note that the spectate link is red or blue pick link before the last forward slash
        browser.close()
        return [blueDraft, redDraft, spectate]
    except Exception as e:
        print(e)
        return ['Error','Error','Please try again and ask Terry to check the error']
