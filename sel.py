from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import os
from urls import *

options = Options()
options.add_argument('--diable-extensions')
options.add_argument('--headless')
driver = webdriver.Chrome(DRIVER_PATH, options=options)

starting_chapter = sorted([int(x[-7:-4]) for x in os.listdir('chapters')])[-1]+1
chapter_bulk = 5

for ch_no in range(starting_chapter,starting_chapter+chapter_bulk-1):

    driver.get(TBATE_URL+f'/chapter-{ch_no}')
    try:
        chapterByte=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))

        chapter = chapterByte.find_elements_by_tag_name('p')
        with open(f'chapters\\chapter-{ch_no}.txt','w') as file:
            for p in chapter:
                file.write(p.text+'\n')

    except TimeoutException:
        continue


driver.quit()
