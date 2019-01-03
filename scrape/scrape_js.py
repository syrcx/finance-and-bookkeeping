# Run with python3 scrape_js.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import time

# Install selenim
#   pip3 install -U selenium
# Grant whoami admin permission to /user/local, in order to run brew install
#   sudo chown -R $(whoami) $(brew --prefix)/*
# Install chromedriver
#   brew tap homebrew/cask
#   brew cask install chromedriver

#url = 'http://wenshu.court.gov.cn/list/list/?sorttype=1&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E5%A4%A9%E6%B4%A5%E5%8C%BB%E8%8D%AF%E9%9B%86%E5%9B%A2'
url = 'http://wenshu.court.gov.cn/'

# The site had blocked robots.So needs access with user agent as a browser.
# https://stackoverflow.com/questions/37625461/why-cant-i-access-the-html-of-some-websites
# headers = {'content-type': 'application/json', 'User-agent': 'Mozilla/5.0'}

driver = webdriver.Chrome()
# WebDriver will wait until the page has fully loaded
# (that is, the “onload” event has fired) before returning control to your test or script.
# It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not
# know when it has completely loaded.
driver.get(url)
search_box_elem = driver.find_element_by_id('gover_search_key')
search_box_elem.click()
search_box_elem.clear()
search_box_elem.send_keys("天津医药集团")

search_button_elem = driver.find_element_by_class_name('head_search_btn')
search_button_elem.click()

# wait for searched page load
# visibility_of_element_located vs presence_of_element_located
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dataItem")))

check_all_select_elem = driver.find_element_by_id('ckall')
check_all_select_elem.click()

download_all_elem = driver.find_element_by_xpath("//div[@class='list-operate'][2]")
download_all_elem.click()

# wait 1s for the download to really initiated.
time.sleep(1)

# wait for download to finish.
def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = downloads.Manager.get().items_;
        if (items.every(e => e.state === "COMPLETE"))
        return items.map(e => e.file_url);
        """)

paths = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
print(paths)

driver.close()
