import requests
from decouple import config
import pprint

# 0. 이미지 파일
img_url = 'https://api.telegram.org/file/bot815471355:AAEXs3TbfrpoVRbYTUFHlTFzzddYjSAz_44/photos/file_2.jpg'
response = requests.get(img_url, stream=True)
img = response.raw.read()
# 1. 네이버 API 설정
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
# 2. URL 설정
naver_url = 'https://openapi.naver.com/v1/vision/celebrity'
# 3. 요청보내기! POST
headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
}

response = requests.post(naver_url, headers=headers, files={'image' : img}).json()
best = response.get('faces')[0].get('celebrity')

if best.get('confidence') > 0.02:
    text = f"{best.get('confidence')*100}만큼 {best.get('value')}만큼 닮으셨네요~~"
else:
    text ='사람 아닌듯'
print(text)
