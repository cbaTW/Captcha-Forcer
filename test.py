from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import func

  
# /html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input
  

op = webdriver.ChromeOptions()
op.page_load_strategy = 'normal'
# op.add_argument('--headless')
# op.add_argument('--disable-notifications')

chrome = webdriver.Chrome(options=op)

chrome.get('https://course.fcu.edu.tw/')
imgs = chrome.find_element(By.XPATH, '/html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/img')    
b64 = imgs.screenshot_as_base64

account = chrome.find_element(By.XPATH, '/html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
password = chrome.find_element(By.XPATH, '/html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input')
captcha = chrome.find_element(By.XPATH, '/html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/input')
login = chrome.find_element(By.XPATH, '/html/body/form/div[5]/div/fieldset/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/center/input')

account.send_keys('123')
password.send_keys('123')
captcha.send_keys(func.ocr(b64))
original_window = chrome.current_window_handle
time.sleep(3)

login.click()

time.sleep(2)

for window_handle in chrome.window_handles:
      if window_handle != original_window:
          chrome.switch_to.window(window_handle)
          break

# error_message = chrome.find_element(By.CSS_SELECTOR,'.longin_outter .wraning') #打錯字的人不是我>_<
# # print(error_message.text)

# if(error_message.text == '驗證碼錯誤!'):
#   print('Captcha Error! Redo')
# elif(error_message.text == '帳號不存在'):
#   print('Account Not Exist')
# elif(error_message.text == '登入錯誤超過限定次數'):
#   print('Too Many Login')
# elif(error_message.text == '密碼錯誤'):
#   print('Password Error')

  
