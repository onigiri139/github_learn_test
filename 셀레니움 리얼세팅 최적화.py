from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


# display = Display(visible=1, size=(1600, 902))
# display.start()

option = Options()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('prefs', {'credentials_enable_service': False, 'profile': {'password_manager_enabled': False}})

option.add_argument("--disable-notifications")
option.add_argument('--disable-extensions')
option.add_argument('--profile-directory=Default')
# option.add_argument("--incognito")
option.add_argument("--disable-plugins-discovery");
option.add_argument("--start-maximized")
option.add_argument("window-size=1920x1080")  # 화면크기(전체화면)
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chromedriver_autoinstaller.get_chrome_version()} Safari/537.36")


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install('./')
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

