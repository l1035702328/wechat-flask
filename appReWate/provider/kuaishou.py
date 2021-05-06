# coding=utf-8
import requests
import re
import json
import time
import random
from ..utils import file_tool


def get_ks(url, path):
    try:
        url = url
        # 设置代理
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        }
        # 获取播放页面
        r = requests.get(url,allow_redirects=False,headers=headers)
        playurl = r.headers['location']
        print(playurl)
        url=re.findall('photo/(.*[a-z,0-9])\?',playurl)[0]
        # print(url)
        cookies=requests.utils.dict_from_cookiejar(r.cookies)
        headers={
            'Connection': 'keep-alive',
            'Accept':'*/*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
          'content-type': 'application/json',
          'Origin': 'https://video.kuaishou.com',
        'Accept-Language':'zh-CN,zh;q=0.9',
        }
        jsonUrl='https://video.kuaishou.com/graphql'
        payload={"operationName":"visionVideoDetail","variables":{"photoId":url,"page":"selected"},"query":"query visionVideoDetail($photoId: String, $type: String, $page: String) {\n  visionVideoDetail(photoId: $photoId, type: $type, page: $page) {\n    status\n    type\n    author {\n      id\n      name\n      following\n      headerUrl\n      __typename\n    }\n    photo {\n      id\n      duration\n      caption\n      likeCount\n      realLikeCount\n      coverUrl\n      photoUrl\n      liked\n      timestamp\n      expTag\n      llsid\n      __typename\n    }\n    tags {\n      type\n      name\n      __typename\n    }\n    commentLimit {\n      canAddComment\n      __typename\n    }\n    llsid\n    __typename\n  }\n}\n"}
        payload=json.dumps(payload) #格式化json对象
        r=requests.post(jsonUrl,data=payload,headers=headers,cookies=cookies)
        if r.status_code != 200:
            print("请求失败")
            exit()
        json_obj = json.loads(r.text)
        print(json_obj)
        playurl=json_obj['data']['visionVideoDetail']['photo']['photoUrl']
        print("真实地址:"+playurl)
        #切换成手机代理
        headers = {
            'user-agent': 'Android',
        }
        # # 请求要下载的url地址
        html = requests.get(playurl, headers=headers).content
        number=str(random.randint(0,65535))
        fileName=time.strftime("%Y%m%d%H%M%S", time.localtime())+'-'+number+'.mp4'
        with open(path+fileName, 'wb') as f:
            f.write(html)
            f.flush()
            f.close()
        print("下载完成！！！！")
        file_tool.updateMd5(path+fileName)
        return fileName
    except Exception as e:
        print(e)
        return 0

