from selenium import webdriver
import chromedriver_autoinstaller

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument("window-size=1920x1080")  # 화면크기(전체화면)
option.add_argument('--disable-blink-features=AutomationControlled')

try:
    driver = webdriver.Chrome(executable_path='./86/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install("./")
    driver = webdriver.Chrome(executable_path='./86/chromedriver.exe', options=option)