def custom_error():
  print('????????\nBye Bye')
  return 0

def welcome():
  cmd = int(input('歡迎使用戳戳卡布洽\n  1. 戳一個\n  2. 戳帳號+密碼\n'))
  if cmd == 1:
    wordlist_path = input('  Give me wordlist path:\n')
    xpath_1 = input('  Give me the Xpath of input\n')

    return cmd, wordlist_path, xpath_1
  elif cmd == 2:
    attack_type = int(input('  1. Fix ACCOUNT\n  2. Fix PASSWORD\n'))
    if attack_type == 1:
      wordlist_path = input('  Give me ACCOUNT wordlist\'s path\n')
      force = input('  Give me that specific PASSWORD\n')
      xpath_1 = input('  Give me the Xpath of ACCOUNT\n')
      xpath_2 = input('  Give me the Xpath of PASSWORD\n')

      # return cmd, attack_type, wordlist_path, force, xpath_1, xpath_2, xpath_captcha
    elif attack_type == 2:
      force = input('  Give me that specific ACCOUNT\n')
      wordlist_path = input('  Give me PASSWORD wordlist\'s path\n')
      xpath_1 = input('  Give me the Xpath of ACCOUNT\n')
      xpath_2 = input('  Give me the Xpath of PASSWORD\n')

      # return cmd, attack_type, wordlist_path, xpath_1, force, xpath_2
    else:
      error()
  else:
    error()
  xpath_captcha = input('  Give me the Xpath of CAPTCHA\n')

  # if cmd == 1:
  #   return cmd, wordlist_path, xpath_1, xpath_captcha
  # elif cmd == 2:
  return cmd, attack_type, wordlist_path, force, xpath_1, xpath_2, xpath_captcha