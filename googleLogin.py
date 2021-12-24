from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import pyperclip
import subprocess
from time import sleep


import shutil, os
try:
    shutil.rmtree(r"c:\chrometemp")
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')


# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install('./')
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

driver.get('https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
sleep(2)


id = 'apple5sagua@gmail.com'
pw = 'qnwkehlwk'

pyperclip.copy(id)
sleep(0.5)
subprocess.Popen(r'googlelogin1.exe')
sleep(0.5)

while 1:
    sleep(1)
    if '비밀번호 표시' in driver.page_source:
        break

pyperclip.copy(pw)
sleep(0.5)
subprocess.Popen(r'googlelogin2.exe')
sleep(0.5)

driver.maximize_window()
driver.get('https://www.naver.com')
