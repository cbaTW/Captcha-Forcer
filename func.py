import requests as rq

host = "http://127.0.0.1:9898"
file_path = "./lis5.txt"

def ocr(b64):
  api_url = f"{host}/ocr/b64"
  resp = rq.post(api_url, data=b64)
  # print(f"{resp.text=}")
  return resp.text

def file_open(file_path):
  f = open(file_path, mode='r')
  k = f.readlines()
  # print(len(k))

# file_open(file_path)