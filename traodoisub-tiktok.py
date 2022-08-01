
import requests, json, os, sys, json, time
from requests.structures import CaseInsensitiveDict

os.system('cls')
def loginTDS (tk, mk):
    try:
        url = "https://traodoisub.com/scr/login.php"
        data = {
            "username": tk,
            "password": mk
        }
        # get cookie with requests
        r = requests.post(url, data=data)
        if "success" in r.text:
            return r.cookies
        else:
            return False
    except:
        return False

log = loginTDS(input("Nhap user: "),input("Nhap pass: "))
if log == False:
    print("Login that bai")
    sys.exit()
else:
    cookie = log.get("PHPSESSID")
    print('Login thanh cong, cookie la: ' + cookie)

# cookie and headers
cookies = {
    'PHPSESSID': cookie
}

headers = {
    'authority': 'traodoisub.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'PHPSESSID=bd3451757cdf7d559ce2583228792b19',
    'referer': 'https://traodoisub.com/view/chtiktok/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'x-requested-with': 'XMLHttpRequest',
}


# get rq 
def getRQ(url):
    global cookies, headers
    rq = requests.get(url, cookies=cookies, headers=headers)
    return rq
# money
getI4 = getRQ("https://traodoisub.com/scr/user.php").json()
xu = getI4['xu']
idtt = getI4['idtt']
if idtt == None:
    print("Chua cau hinh tiktok")
    sys.exit()
else:
    print("Tiktok id: " + idtt)
    print("Tien xu: " + xu)
    #    print("Het job thi vao trao doi sub them roi cau hinh lai vao chay tiep")


def menu_job():
    listjob = {
        1: "Job follow",
        2: "Job tim"
    }
    for x, y in listjob.items():
        print(x, '=>', y)
    
    job = int(input("Chon job: "))
    if (job > len(listjob)):
        print("May chon ngu")
        sys.exit()
    else:
        return job

cookie_tiktok = ""

def inputinfotoctoc():
    global cookie_tiktok, xsecsdkcsrftoken
    cookie_tiktok = input("Nhap cookie tiktok: ")
    if (cookie_tiktok == "" or cookie_tiktok == None):
        print("Nhap sai cookie")
        sys.exit()

# get job tim
print("Dang lay thong tin tai khoan")
getThongtin = getRQ("https://traodoisub.com/view/setting/load.php").json()
user = getThongtin['user']
token = getThongtin['tokentds']
print("Tai khoan: " + user)
print("Token: " + token)

print('Dang lay list tai khoan tiktok')
getListtk = getRQ("https://traodoisub.com/view/chtiktok/").text
splitTr = getListtk.split('<tr class="btn-reveal-trigger">')
listIdTiktok = []
for x in splitTr:
    if ('<th class="align-middle text-center white-space-nowrap id">' in x):
        listIdTiktok.append(x.split('target="_blank">')[1].split('</a>')[0])

i = 0
while i < int(len(listIdTiktok)):
    print('[', i, ']', listIdTiktok[i])
    i += 1

stt = int(input("Nhap vao so muon cau hinh: "))
if stt > len(listIdTiktok)-1:
    print("So muon cau hinh khong hop le")
    sys.exit()
else:
    data = {
        'iddat': listIdTiktok[stt],
    }
    response = requests.post('https://traodoisub.com/scr/tiktok_datnick.php', cookies=cookies, headers=headers, data=data)
    if (int(response.text) == 1):
        print("Cau hinh thanh cong")
    else:
        print("Cau hinh that bai")
        sys.exit()



    headers_default = CaseInsensitiveDict()

    def getInfoTIKTOK():
        global headers_default, cookie_tiktok
        url_getinfo = 'https://www.tiktok.com/@enola.bedard'
        rq = requests.get(url_getinfo, headers=headers_default).text
        json_ = json.loads(rq.split('<script id="SIGI_STATE" type="application/json">')[1].split('</script>')[0])
        defaultjson = json_['AppContext']['appContext']['user']
        uid = defaultjson['uid']
        name = defaultjson['nickName']
        uniqueId = defaultjson['uniqueId']
        region = defaultjson['region']
        print("UID: " + uid)
        print("Name: " + name)
        print("UniqueId: " + uniqueId)
        print("Region: " + region)

    def getNV (type):
        global token
        url = "https://traodoisub.com/api/?fields=" + type + "&access_token=" + token
        rq = getRQ(url).json()
        return rq['data']

    def sendNV (type, id):
        global token
        url = "https://traodoisub.com/api/coin/?type=" + type + "&id=" + id + "&access_token=" + token
        rq = getRQ(url)

    def claim (type, id):
        global token
        url = "https://traodoisub.com/api/coin/?type=" + type + "&id=" + id + "&access_token=" + token
        rq = requests.get(url).json()
        if (rq["success"] == 200):
            print('Job thanh cong: ', rq['data']['job_success'])
            print('Nhan thanh cong ', rq["data"]["msg"], ' tong xu la: ', rq["data"]["xu"])
        else:
            print('Chua du nguong')

    def getHeaderUser(url):
        global headers_default
        return requests.get(url, headers=headers_default).headers

    def followUser(id_follow, url_follow):
        global headers_default
        try:
            headers = getHeaderUser(url_follow)
            msToken = headers["Set-Cookie"].split('msToken=')[1].split(';')[0]
            urlFollow = 'https://t.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.134%20Safari%2F537.36%20Edg%2F103.0.1264.77&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id=7119768594258642434&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=5&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=1080&screen_width=1920&sec_user_id=&type=1&tz_name=Asia%2FBangkok&user_id='+id_follow+'&verifyFp=&webcast_language=vi-VN&msToken='+msToken+'&_signature='
            json = requests.post(urlFollow, headers=headers_default).json()
            if(int(json['follow_status']) == 1):
                print('Follow thanh cong', id_follow)
            else:
                print('Follow that bai', id_follow)
        except:
            print('Loi roi thang lon')

    def hearthVideo(url_video):
        global headers_default
        try:
            headers = getHeaderUser(url_video)
            msToken = headers["Set-Cookie"].split('msToken=')[1].split(';')[0]
            idVideo = url_video.split('/video/')[1].split('?')[0]
            print('idVideo: '+idVideo)
            urlHearth = 'https://t.tiktok.com/api/commit/item/digg/?aid=1988&app_language=vi-VN&app_name=tiktok_web&aweme_id='+idVideo+'&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.134%20Safari%2F537.36%20Edg%2F103.0.1264.77&channel=tiktok_web&cookie_enabled=true&device_id=7119768594258642434&device_platform=web_pc&focus_state=true&from_page=video&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=1080&screen_width=1920&type=1&tz_name=Asia%2FBangkok&verifyFp=&webcast_language=vi-VN&msToken='+msToken+'&X-Bogus=&_signature='
            json = requests.post(urlHearth, headers=headers_default).json()
            if(int(json['is_digg']) == 1):
                print('Hearth thanh cong', idVideo)
            else:
                print('Hearth that bai', idVideo)
        except:
            print('Loi roi thang lon')
    

    choice = menu_job()
    inputinfotoctoc()
    headers_default["Accept"] = "*/*"
    headers_default["Accept-Language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers_default["Connection"] = "keep-alive"
    headers_default["Content-Length"] = "0"
    headers_default["Cookie"] = cookie_tiktok
    headers_default["Origin"] = "https://www.tiktok.com"
    headers_default["Referer"] = "https://www.tiktok.com/"
    headers_default["Sec-Fetch-Dest"] = "empty"
    headers_default["Sec-Fetch-Mode"] = "cors"
    headers_default["Sec-Fetch-Site"] = "same-site"
    headers_default["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
    headers_default["content-type"] = "application/x-www-form-urlencoded"
    getInfoTIKTOK()
    while True:
        if choice == 1:
            try:
                listJob = getNV("tiktok_follow")
                if (len(listJob) > 0):
                    for x in listJob:
                        followUser(x['id'].split('_')[0], x['link'])
                        sendNV("TIKTOK_FOLLOW_CACHE", x["id"])

                    claim('TIKTOK_FOLLOW', 'TIKTOK_FOLLOW_API')
                else:
                    print('Het job roi thang lon', end="\r")
                    time.sleep(10)
            except:
                print('Het job roi thang lon', end="\r")
                time.sleep(10)

        elif choice == 2:
            csrf_cookie = cookie_tiktok.split('tt_csrf_token=')[1].split(';')[0]
            headers_default['tt-csrf-token'] = csrf_cookie
            try:
                listJob = getNV('tiktok_like')
                if (len(listJob) > 0):
                    for x in listJob:
                        hearthVideo(x['link'])
                        sendNV('TIKTOK_LIKE_CACHE', x["id"])
                    claim('TIKTOK_LIKE', 'TIKTOK_LIKE_API')
                else:
                    print('Het job roi thang lon', end="\r")
                    time.sleep(10)
            except:
                print('Het job roi thang lon', end="\r")
                time.sleep(10)
