from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

# 뷰티풀숩에서 일부 문자열이 일치하는 텍스트의 테그를 객체로 찾기

soup.find(text=re.compile('하하+')) # '하하' 문자열이 들어간 텍스트의 일부가 일치하면 찾아낸다

# 셀레니움에서는 re.compile 이 안통한다. 예를 들어

# driver.find_elements_by_class_name(re.compile('하하+')) -> 이렇게 하면 에러가 발생한다.

#셀레니움에서는 xpath 를 이용해서 class 의 일부 문자열 일치하면 객체를 가져오는 설정을 할 수 있다.

driver.find_elements_by_xpath("//*[contains(@class, '하하')]") #클래스 속성값의 일부가 '하하'가 일치하면 그 속성을 가져온다.
driver.find_elements_by_xpath("//*[contains(@id, '하하')]") #ID 속성값의 일부가 '하하'가 일치하면 그 속성을 가져온다.

#셀레니움에서 css selector 를 이용해서도 특정한 태그의 어떤 속성과 속성값의 일부일치하는 것을 가져올 수 있다.

 #img 태그 안에 class 속성값이 'rg_i' 가 일부만 일치하면 해당 객체를 가져오는 것이다.driver.find_elements_by_css_selector("img[class*=rg_i")