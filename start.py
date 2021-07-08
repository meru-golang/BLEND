from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import chromedriver_binary
import random
from config import url

#ログインするための情報を取得
login_id = input("IDを入力>> ")
login_pw = input("PWを入力>> ")
#ここで指定も可能
#login_id = ""
#login_pw = ""

#chromedriverのオプション
options = Options()
#options.add_argument('--headless') #ブラウザを表示したくないならこれ使え
driver = webdriver.Chrome(options=options)

#BLENDのログイン
url_login = url.host + url.login
driver.get(url_login)
driver.find_element_by_css_selector("#login_id").send_keys(login_id)
driver.find_element_by_css_selector("#login_password").send_keys(login_pw)
driver.find_element_by_css_selector("#login_form_submit").click()
name = driver.find_element_by_css_selector("#student > div.l-side > div.profile.clearfix > a > span").text
print(name + "にログインしました！")

#体温送信
url_health = url.health
driver.get(url_health)
driver.find_element_by_css_selector("#student > div.page.clearfix > section > table > tbody > tr:nth-child(2) > td > div > div > input").send_keys("36.0")
driver.find_element_by_css_selector("#student > div.page.clearfix > div > button.submit").click()
