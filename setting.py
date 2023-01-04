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
def set(mode):
  if(mode == 1):
    url = input("\n測試的 URL:") or "https://netid.fcu.edu.tw/Apps/fpsw.aspx"
    input_xpath = input("爆破欄位的 Xpath:") or "/html/body/div/div[2]/div[1]/div/div/div/form/div[3]/div[2]/div/input"
    input_wordlist = input("爆破的 wordlist:") or "./test.txt"
    captcha_img_xpath = input("captcha圖片的 Xpath:") or "/html/body/div/div[2]/div[1]/div/div/div/form/div[3]/div[3]/div/a/img"
    captcha_input_xpath = input("captcha輸入的 Xpath:") or "/html/body/div/div[2]/div[1]/div/div/div/form/div[3]/div[3]/div/input"
    enter_xpath = input("送出鍵的 Xpath:") or "/html/body/div/div[2]/div[1]/div/div/div/form/div[3]/p/input"
    success_box_xpath = input("成功欄位的 Xpath:") or "/html/body/div/div[2]/div[1]/div/div/div/form/div[3]/span[2]"
    success_flag = input("成功欄位的 flag:") or "- 系統會將您的NID新密碼寄到啟用帳號時留下的備用Email信箱，若需變更請至個人綜合資料維護修改。"
    retry_box_path = input("重試欄位 Xpath:") or "/html/body/div/div[2]/div[1]/div/div/div/form/div[3]/span[2]"
    retry_flag = input("重試欄位 flag:") or "驗證碼錯誤，請重新輸入！"
    
    return(url, input_xpath, input_wordlist, captcha_img_xpath, captcha_input_xpath, enter_xpath, success_box_xpath, retry_box_path, success_flag, retry_flag)

  elif(mode == 2):
    print("TODO")

  elif(mode == 3):
    print("**結束程式***")