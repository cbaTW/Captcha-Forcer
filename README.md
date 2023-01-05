# 戳戳卡布洽

## OCR server with DOCKER

Port 會開在 9898

```shell
git clone https://github.com/sml2h3/ocr_api_server.git

cd ocr_api_server

docker build -t ocr_server:v1 .

docker run -p 9898:9898 -d ocr_server:v1

```

THEN, run test.py

wordlist 需使用絕對路徑！
