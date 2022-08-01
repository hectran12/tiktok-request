import requests
from requests.structures import CaseInsensitiveDict
url_follow = input("Nhap url follow: ")
id_follow  = input("Nhap id follow: ")
myCookie  = "<YOUR COOKIE>"
headers_default = CaseInsensitiveDict()
headers_default["Accept"] = "*/*"
headers_default["Accept-Language"] = "vi,en;q=0.9,en-US;q=0.8"
headers_default["Connection"] = "keep-alive"
headers_default["Content-Length"] = "0"
headers_default["Cookie"] = myCookie
headers_default["Origin"] = "https://www.tiktok.com"
headers_default["Referer"] = "https://www.tiktok.com/"
headers_default["Sec-Fetch-Dest"] = "empty"
headers_default["Sec-Fetch-Mode"] = "cors"
headers_default["Sec-Fetch-Site"] = "same-site"
headers_default["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
headers_default["content-type"] = "application/x-www-form-urlencoded"
def getHeaderUser():
    global headers_default, url_follow
    return requests.get(url_follow, headers=headers_default).headers
def followUser():
    global id_follow, headers_default
    headers = getHeaderUser()
    msToken = headers["Set-Cookie"].split('msToken=')[1].split(';')[0]
    urlFollow = 'https://t.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.134%20Safari%2F537.36%20Edg%2F103.0.1264.77&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id=7119768594258642434&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=5&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=1080&screen_width=1920&sec_user_id=&type=1&tz_name=Asia%2FBangkok&user_id='+id_follow+'&verifyFp=&webcast_language=vi-VN&msToken='+msToken+'&_signature='
    json = requests.post(urlFollow, headers=headers_default).json()
    print(json)
followUser()
