#coding=utf-8
import re
from ..provider import douyin, kuaishou


def link_check(url, path):
    dy_url = 'https://v.douyin.com'
    ks_url = 'https://v.kuaishou.com'
    # 火山小视频
    hs_url = 'https://share.huoshan.com'
    # 微视
    ws_url = 'https://h5.weishi.qq.com'
    xhs_url = ''
    ppx_url = ''
    mp_url = ''
    if dy_url in url:
        print("调用抖音")
        # 提取链接
        url = re.findall('http.*[\x00-\xff]', url)[0].replace(' ', '')
        print(url)
        file_name = douyin.get_dy(url, path)
        return file_name
    if ks_url in url:
        print("调用快手")
        url = re.findall('http.*[\x00-\xff]', url)[0].replace(' ', '')
        file_name = kuaishou.get_ks(url, path)
        return file_name
    if hs_url in url:
        print("调用火山小视频")
        url = re.findall('http.*[\x00-\xff]\s', url)[0].replace(' ', '')
        return 0
    if ws_url in url:
        print("调用微视")
        url = re.findall('http.*[\x00-\xff]', url)[0].replace(' ', '')
        return 0
