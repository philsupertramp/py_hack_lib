# -*- coding: UTF-8 -*-
import requests
import json
import time

start = time.time()
data = {
    'X-Amz-Algorithm': str('AWS4-HMAC-SHA256'),
    'X-Amz-Credential': str('AKIAI27CU2NUYBEDEAMA/20180407/eu-central-1/s3/aws4_request'),
    'X-Amz-Date': '20180407T212344Z',
    'X-Amz-Expires': '3600',
    'X-Amz-SignedHeaders': 'host',
    'X-Amz-Signature': '5a7ed3d58a977e085542a7301f2a29e9ac7c4b527ac1ea20de2c81ff67dc0e4f'
}
data = json.dumps(data)
url = "https://s3.eu-central-1.amazonaws.com/studysmarter-mediafiles/media/3000/test/lernen.php?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAI27CU2NUYBEDEAMA/20180407/eu-central-1/s3/aws4_request&X-Amz-Date=20180407T214947Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=0f89022b75a78da8473136097de8d188e644896790f4a4085e08ed04dbbb934b"
req = requests.options('https://api.personio.de/recruiting/applicant')
print(data)
print(req)

"""
_csrf_token=7Hfgmvt2puh-fHzit5-O3m9eoPewNSJHkLizwp7ifY0
_username=s63030@beuth-hochschule.de
_password=testtesttest
"""
"https://s3.eu-central-1.amazonaws.com/studysmarter-mediafiles/media/3000/test/lernen.php?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAI27CU2NUYBEDEAMA/20180407/eu-central-1/s3/aws4_request&X-Amz-Date=20180407T214947Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=0f89022b75a78da8473136097de8d188e644896790f4a4085e08ed04dbbb934b"