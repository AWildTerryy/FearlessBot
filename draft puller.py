# this script should open an existing draftlol link and find what champs are picked and banned

from selenium import webdriver
import time
from os import path

browser = webdriver.Chrome()
browser.get('https://draftlol.dawe.gg/NgpQs3mu')
time.sleep(1)  # note that this page will take longer to load due to images
bluePick = browser.find_element_by_class_name('roomPickColumn.blue').find_elements_by_tag_name('p')
redPick = browser.find_element_by_class_name('roomPickColumn.red').find_elements_by_tag_name('p')
# I noticed each pick is named under the p tag, I can pull the names of each champ from there
blueBan = browser.find_element_by_class_name('roomBanRow.blue').find_elements_by_tag_name('img')
redBan = browser.find_element_by_class_name('roomBanRow.red').find_elements_by_tag_name('img')
if path.exists('bannedchampions.txt'):
    banList = open('bannedchampions.txt','a')
    banList.write('\n')
else:
    banList = open('bannedchampions.txt', 'a+')
# If the file exists, we add a space before adding more champions else we create the file
for element in bluePick:
    banList.write(element.get_property('textContent')+'\n')
for element in redPick:
    banList.write(element.get_property('textContent')+'\n')
for element in blueBan:
    banList.write(element.get_property('alt')+'\n')
for element in redBan:
    banList.write(element.get_property('alt')+'\n')
# note that we are expecting duplicates to occur in the list due to not expecting champions to be picked/banned if they
# were already banned or picked
browser.close()
banList.close()
