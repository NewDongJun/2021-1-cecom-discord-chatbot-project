#2
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe" , options=options)
driver.implicitly_wait(3)

#3
learningx = 'https://ocs.cau.ac.kr/index.php?module=xn_commonsi&act=dispXn_commonsiMobileLogin&return_url=https%3A%2F%2Focs.cau.ac.kr%2Findex.php%3Fmodule%3Dxn_sso2013%26act%3DprocXn_sso2013ExternalLoginCallback%26return_url%3Dhttps%253A%252F%252Feclass3.cau.ac.kr%252F%252Flearningx%252Flogin%26from%3Dweb_redirect%26login_type%3Dsso%26sso_only%3Dtrue&auto_login=true&sso_only=true&cvs_lgn='
driver.get(learningx)

cauid = input("아이디를 입력해 주세요")
caupassword = input("비밀번호를 입력해 주세요")


driver.find_element_by_id('login_user_id').send_keys(cauid)
driver.find_element_by_id('login_user_password').send_keys(caupassword)

#로그인 하기(로그인 버튼 누르기)
try:
    driver.find_element_by_xpath("""//*[@id="login_wapper"]/div[1]/div[4]/a""").click()
    #//*[@id="login_wapper"]/div[1]/div[4]/a/
except:
    alert = driver.switch_to.alert
    alert.accept()
    print('Alert Occurred')
    pass

try:
    driver.find_element_by_class_name('login_box').click()
except:
    alert = driver.switch_to.alert
    alert.accept()
    print('Wait for a second...')
    time.sleep(2)
    pass

driver.get("https://eclass3.cau.ac.kr/")

try:
    driver.find_element_by_class_name('login_box').click()
except:
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    pass
print(driver.current_url)

#5
#Subject Name List
subname = driver.find_element_by_xpath("""//*[@id="DashboardCard_Container"]/div""")
subname = subname.find_elements_by_class_name("ic-DashboardCard")
subnamelst = list()
for n in subname:
    subnamelst.append(n.get_attribute("aria-label"))
print(subnamelst, "\n\n")

#Subject Number List
subnum = driver.find_element_by_xpath("""//*[@id="DashboardCard_Container"]/div""")
subnum = subnum.find_elements_by_class_name('ic-DashboardCard')
subnumlst = list()
for n in subnum:
    subnumlst.append(n.get_attribute("data-reactid")[4:])
print(subnumlst, "\n\n")

#Subject Dictionary

subdic = dict(zip(subnamelst, subnumlst))
print(subdic)


#6
asslinklst = list()
for val in subdic.values():
    asslinklst.append("https://eclass3.cau.ac.kr/courses/"+val+"/assignments")

for linkx in asslinklst:
    driver.get(linkx)
    driver.find_elements_by_class_name("assignment sort-disabled search_show")
