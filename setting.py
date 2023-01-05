import json

#模式設定
def mode_set():
  while(1):
    mode = int(input('***歡迎使用戳戳卡布洽***\n  1. 戳一個\n  2. 戳帳號+密碼\n  3. 結束\n\n使用模式:'))

    if(mode == 1):
      return mode

    elif(mode == 2):
      print("\n***未完成！***\n")
      continue

    elif(mode == 3):
      return mode

    else:
      print("\n***輸入錯誤，重新輸入！***\n")
      continue

#攻擊設定
def set(mode, default_path):
  with open(default_path, mode='r', encoding='UTF-8') as f:
    default = json.load(f)
  if(mode == 1):
    url = input("\n測試的 URL:") or default["target_url"]
    input_xpath = input("爆破欄位的 Xpath:") or default["input"]["xpath"]
    input_wordlist = input("爆破的 wordlist:") or default["input"]["wordlist"]
    captcha_img_xpath = input("captcha圖片的 Xpath:") or default["captcha"]["img_xpath"]
    captcha_input_xpath = input("captcha輸入的 Xpath:") or default["captcha"]["input_xpath"]
    enter_xpath = input("送出鍵的 Xpath:") or default["enter_xpath"]
    success_box_xpath = input("成功欄位的 Xpath:") or default["success_box"]["xpath"]
    success_flag = input("成功欄位的 flag:") or default["success_box"]["flag"]
    retry_box_path = input("重試欄位 Xpath:") or default["retry_box"]["xpath"]
    retry_flag = input("重試欄位 flag:") or default["retry_box"]["flag"]
    
    return(url, input_xpath, input_wordlist, captcha_img_xpath, captcha_input_xpath, enter_xpath, success_box_xpath, retry_box_path, success_flag, retry_flag)

  elif(mode == 2):
    print("TODO")

  elif(mode == 3):
    print("**結束程式***")
