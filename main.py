from selenium import webdriver

import time
import requests as rq

from func import ocr
import welcome



def file_open(file_path):
  with open(file_path, mode='r', encoding='UTF-8') as F:
    line = F.readline().strip('\n')
    while line is not None and line != '':
      # print(line)
      # print(type(line))
      line = F.readline().strip('\n')

def main():
  cmd_palette = welcome.welcome()
  with open(cmd_palette[1], mode='r', encoding='UTF-8') as F:
    # 迭代器需要先讀第一次，所以要寫兩遍，感覺有更好的寫法
    iterator = F.readline().strip('\n')

    # 單點爆破
    if cmd_palette[0] is 1:

    # elif cmd_palette[0] is 2:

    while iterator is not None and iterator != '':
      iterator = F.readline().strip('\n')
      # 單點爆破 again
      if cmd_palette[0] is 1:

 
      # elif cmd_palette[0] is 2:
  
  print(cmd_palette)
  if cmd_palette[0] is 1:

  elif cmd_palette[0] is 2:
    print(123)
  else:
    welcome.custom_error()



file_open('./lis5.txt')




# op = webdriver.ChromeOptions()
# op.page_load_strategy = 'normal'
# # op.add_argument('--headless')
# # op.add_argument("--disable-notifications")

# chrome = webdriver.Chrome(options=op)

# chrome.get("https://uat69.udnfunlife.com/spm/Cs1001.do")
# imgs = chrome.find_elements(By.TAG_NAME, "img")    
# b64 = imgs[2].screenshot_as_base64

# username = chrome.find_element(By.ID, 'dc_acno_0')
# password = chrome.find_element(By.ID, 'dc_pswd_0')
# captcha = chrome.find_element(By.ID, 'dc_vcode_0')
# login = chrome.find_element(By.CLASS_NAME, 'login_btn')

# username.send_keys('123')
# password.send_keys('123')
# captcha.send_keys(ocr(b64))
# original_window = chrome.current_window_handle
# # time.sleep(3)

# login.click()

# # time.sleep(3)

# for window_handle in chrome.window_handles:
#       if window_handle != original_window:
#           chrome.switch_to.window(window_handle)
#           break

# error_message = chrome.find_element(By.CSS_SELECTOR,".longin_outter .wraning") #打錯字的人不是我>_<
# # print(error_message.text)

# if(error_message.text == '驗證碼錯誤!'):
#   print("Captcha Error! Redo")
# elif(error_message.text == '帳號不存在'):
#   print("Account Not Exist")
# elif(error_message.text == '登入錯誤超過限定次數'):
#   print("Too Many Login")
# elif(error_message.text == '密碼錯誤'):
#   print("Password Error")

  

# time.sleep(3)


main()