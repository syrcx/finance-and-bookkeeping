# Run with python3 fx.py

from selenium import webdriver
import time

# Install selenim
#   pip3 install -U selenium
# Grant whoami admin permission to /user/local, in order to run brew install
#   sudo chown -R $(whoami) $(brew --prefix)/*
# Install chromedriver
#   brew tap homebrew/cask
#   brew cask install chromedriver

url = 'https://www1.oanda.com/currency/converter/'

# The site had blocked robots.So needs access with user agent as a browser.
# https://stackoverflow.com/questions/37625461/why-cant-i-access-the-html-of-some-websites
# headers = {'content-type': 'application/json', 'User-agent': 'Mozilla/5.0'}

driver = webdriver.Chrome()
# WebDriver will wait until the page has fully loaded
# (that is, the “onload” event has fired) before returning control to your test or script.
# It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not
# know when it has completely loaded.
driver.get(url)

currency = {
    'CAD': 'Canadian Dollar',
    'USD': 'US Dollar',
    'GBP': 'British Pound',
    'EUR': 'Euro'
}

for want_key, want_value in currency.items():
    for base_key, base_value in currency.items():
        if want_key == base_key:
            continue

        cih_input = driver.find_element_by_id('quote_currency_input')
        cih_input.clear()
        cih_input.send_keys(want_value)
        cih_dropdown = driver.find_element_by_class_name('list_item_hover')
        cih_dropdown.click()

        ciw_input = driver.find_element_by_id('base_currency_input')
        ciw_input.clear()
        ciw_input.send_keys(base_value)
        ciw_dropdown = driver.find_element_by_class_name('list_item_hover')
        ciw_dropdown.click()

        time.sleep(1)

        rate = driver.find_element_by_id('base_amount_input').get_attribute('value')
        print("{} -> {}: {}".format(want_key, base_key, rate))

driver.close()
