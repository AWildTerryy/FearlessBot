# this script should open draftlol, ban champions from a list, then return the draft links

# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://draftlol.dawe.gg/')
time.sleep(0.5)  # just to let page load, shouldn't take too long
browser.find_element_by_class_name('advancedOptionsButton').click()
time.sleep(0.5)  # let advance options load
championSearchBox = browser.find_element_by_class_name('champsFiltersSearch')
championSearch = championSearchBox.find_element_by_tag_name('input')  # get search box


def ban_champion(champName):
    # This function will search for a champion, click it in order to ban it, then clear the search field
    championSearch.send_keys(champName)
    champion = browser.find_element_by_class_name('roomImgListItem')
    browser.execute_script('arguments[0].click()', champion)
    championSearch.clear()


test = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol',
        'Azir', 'Bard', 'Bel\'Veth', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia']

for name in test:
    ban_champion(name)

browser.find_element_by_class_name('sendButton').click()
time.sleep(0.5)  # After banning the champions, click the create button to create the draft and wait for it to load
blueDraft = browser.find_element_by_class_name('inputBlue').get_property('defaultValue')
redDraft = browser.find_element_by_class_name('inputRed').get_property('defaultValue')
slicePoint = blueDraft.rindex('/')
spectate = blueDraft[:slicePoint]
# Get the links for the drafts, note that the spectate link is red or blue pick link before the last forward slash
print(blueDraft)
print(redDraft)
print(spectate)
browser.close()
