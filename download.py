# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


username = "jmaltby"
password = "welcome123"

# url = "https://www.laundryxpert.com/Reporting/Pages/#/reporting/company/7a9a4f45-c37e-4578-a5ea-82fbc1000c55/location/25f2309a-92ac-470c-9d36-7aa94b8c19cb/report/4553529b-df3e-4549-ac90-e00eea8b6df1"
url = "https://www.laundryxpert.com/Reporting/Pages/#/reporting/company/024de0a9-360b-4c02-b3c0-0954f9360562/location/b1c1fb4c-c0f5-4ea5-af92-6e8da4fb5b54/report"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(url)

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button.button.right").click()
# driver.find_element(By.XPATH, "//li[conains(@class, 'clearfix')][.//span[@class, 'report-title[contains(., 'Southall')]]]").click()

time.sleep(5)

driver.get('https://www.laundryxpert.com/Reporting/Pages/#/reporting/company/7a9a4f45-c37e-4578-a5ea-82fbc1000c55/location/28892925-9469-4908-93d2-5cbbb640286e/report')

driver.get('https://www.laundryxpert.com/Reporting/Pages/#/reporting/company/7a9a4f45-c37e-4578-a5ea-82fbc1000c55/location/28892925-9469-4908-93d2-5cbbb640286e/report/4553529b-df3e-4549-ac90-e00eea8b6df1')

time.sleep(8)

driver.find_element(By.CSS_SELECTOR, "button.addnew.element.right.lxp-default-export").click()

driver.find_element(By.XPATH, "//div[contains(@data-bind, 'click: ExportCsv')]").click()

# Select(driver.find_element_by_xpath('//select[contains(@data-bind,"value: customerProvince, options: availableProvinces, optionsText:")]')).select_by_value('Nunavut').click()


