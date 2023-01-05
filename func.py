import requests as rq
import json

def ocr(b64, host):
  api_url = f"{host}/ocr/b64"
  resp = rq.post(api_url, data=b64)
  # print(f"{resp.text=}")
  return resp.text
