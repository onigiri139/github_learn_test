
# 아래는 클래스 네임으로 엘리먼트가 있는지 없는지 찾아내는 함수이다. 찾아낸 엘리먼트가 1개 이면 단일 엘리먼트로 return 하고 아니면 리스트형식으로 리턴한다.
from selenium.common.exceptions import NoSuchElementException
def check_element_by_class(*classname):
    result = []
    for element in classname:
        try:
            result.append(driver.find_element_by_class_name(element))
        except NoSuchElementException:
            pass

	if len(result) == 1:
		return result[0]
    else:
		return result


# https://discuss.appium.io/t/using-python-can-i-retrieve-a-list-of-available-elements-on-a-given-page/1315/4
elements = driver.find_elements_by_xpath("//*[not(*)]")
# //*[not(*)] means, that you are looking for element with any tag which doesn't contain any other tag, i.e. element.




# https://dejavuqa.tistory.com/198 참고


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver.exe")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


#b = driver.find_element_by_xpath('//*[@id="SE-1fd7a1be-7a80-41f2-801f-076bee122ea1"]/div/div/a/img')

iframe = driver.find_element_by_id("mainFrame")
driver.switch_to.frame(iframe)

b=driver.find_element_by_class_name("se-image-resource").get_attribute('src')

driver.find_elements_by_class_name('rg_i').get_attribute('src')

# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# chromedriver로 브라우저를 설정합니다.
driver = webdriver.Chrome('./chromedriver')

# find_element_by_ 함수를 사용해 element를 찾을때 최대 30초까지 기다립니다.
driver.implicitly_wait(30)

# 회사 메일(worksmobile) 사이트를 엽니다.
driver.get('https://mail.worksmobile.com/')

# 로그인을 위한 계정을 입력합니다.
driver.find_element_by_id('user_id').send_keys('tongchun@ngle.co.kr')

# 로그인 시작을 클릭합니다.
driver.find_element_by_id('loginStart').click()

# 비밀번호를 넣습니다.
driver.find_element_by_id('password').send_keys('123456')

# 로그인 버튼을 클릭합니다.
driver.find_element_by_id('loginBtn').click()

# 메일쓰기 버튼(링크)을 찾아 클릭합니다.
driver.find_element_by_link_text('메일쓰기').click()

# 보내는 사람을 지정합니다.
driver.find_element_by_id('toInput').send_keys('tongchun@ngle.co.kr')

# 제목을 넣습니다.
driver.find_element_by_id('subject').send_keys('selenium은 즐기고 계신가요?')

# 현재 웹페이지에서 iframe이 몇개가 있는지 변수에 넣고 확인해 봅니다.
iframes = driver.find_elements_by_tag_name('iframe')
print('현재 페이지에 iframe은 %d개가 있습니다.' % len(iframes))

# 배열로된 iframes 변수를 for문을 이용해 하나씩 확인해 봅니다.
# enumerate() 함수를 사용하면 배열의 index(순번)을 확인할 수 있습니다.
for i, iframe in enumerate(iframes):
	try:
		print('%d번째 iframe 입니다.' % i)

		# i 번째 iframe으로 변경합니다.
		driver.switch_to_frame(iframes[i])

		# 변경한 iframe 안의 소스를 확인합니다.
		print(driver.page_source)

		# 원래 frame으로 돌아옵니다.
		driver.switch_to_default_content()
	except:
		# exception이 발생했다면 원래 frame으로 돌아옵니다.
		driver.switch_to_default_content()

		# 몇 번째 frame에서 에러가 났었는지 확인합니다.
		print('pass by except : iframes[%d]' % i)

		# 다음 for문으로 넘어갑니다.
		pass

# 확인된 ifrime으로 변경합니다.
driver.switch_to_frame(iframes[1])

# 메일 본문을 작성하는 editor element를 지정합니다.
editor = driver.find_element_by_class_name('workseditor')

# editor element에 글을 작성합니다.
editor.send_keys('안녕하세요. 김동춘입니다.\nselenium은 재미 있나요?\n어려워 하지 마세요. 인생이 다 그래요. 해보면 벌거 아니에요.\n좋은하루 보내세요~')

# ifrime에서 원래 frame으로 돌아옵니다.
driver.switch_to_default_content()

# 보내기 버튼을 클릭합니다.
driver.find_element_by_id('sendBtn').click()


