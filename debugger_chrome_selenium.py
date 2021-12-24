# https://klonic.tistory.com/76

# chrome.exe --remote-debugging-port=9222 --user-data-dir="경로지정"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "./87/chromedriver.exe" # Your Chrome Driver path

driver = webdriver.Chrome(chrome_driver, options=chrome_options)


driver.get('https://www.naver.com')
driver.get('https://sbbam8.com/')