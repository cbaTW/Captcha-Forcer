from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def config():
  config = webdriver.ChromeOptions()
config.page_load_strategy = 'normal'
# config.add_argument('--headless')
# config.add_argument("--disable-notifications")
  # return config

def forcer(account, pswd, XPATH1, XPATH2, XPATH_CAPTCHA):
  # config()
  print(123)
  chrome = webdriver.Chrome()
  chrome.get("https://course.fcu.edu.tw/")
  
  # /html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input
  

op = webdriver.ChromeOptions()
op.page_load_strategy = 'normal'
# op.add_argument('--headless')
# op.add_argument("--disable-notifications")

chrome = webdriver.Chrome(options=op)

chrome.get("https://course.fcu.edu.tw/")
imgs = chrome.find_elements(By.TAG_NAME, "img")    
b64 = imgs[2].screenshot_as_base64

username = chrome.find_element(By.ID, 'dc_acno_0')
password = chrome.find_element(By.ID, 'dc_pswd_0')
captcha = chrome.find_element(By.ID, 'dc_vcode_0')
login = chrome.find_element(By.CLASS_NAME, 'login_btn')

username.send_keys('123')
password.send_keys('123')
captcha.send_keys(ocr(b64))
original_window = chrome.current_window_handle
# time.sleep(3)

login.click()

# time.sleep(3)

for window_handle in chrome.window_handles:
      if window_handle != original_window:
          chrome.switch_to.window(window_handle)
          break

error_message = chrome.find_element(By.CSS_SELECTOR,".longin_outter .wraning") #打錯字的人不是我>_<
# print(error_message.text)

if(error_message.text == '驗證碼錯誤!'):
  print("Captcha Error! Redo")
elif(error_message.text == '帳號不存在'):
  print("Account Not Exist")
elif(error_message.text == '登入錯誤超過限定次數'):
  print("Too Many Login")
elif(error_message.text == '密碼錯誤'):
  print("Password Error")

  

time.sleep(3)