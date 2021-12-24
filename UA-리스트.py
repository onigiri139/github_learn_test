Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/71.0.3578.89 Mobile/15E148 Safari/605.1
Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G950N/KSU3CRJ1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.2 Chrome/63.0.3239.111 Mobile Safari/537.36

Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0;






from selenium import webdriver
import chromedriver_autoinstaller

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chromedriver_autoinstaller.get_chrome_version()} Safari/537.36")
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")

chrome_ver = chromedriver_autoinstaller.get_chrome_version()

try:
    driver = webdriver.Chrome(executable_path=f"./{chrome_ver[:2]}/chromedriver.exe", options=options)
except:
    chromedriver_autoinstaller.install('./')
    driver = webdriver.Chrome(executable_path=f"./{chrome_ver[:2]}/chromedriver.exe", options=options)

driver.implicitly_wait(10)
driver.get("https://www.naver.com")