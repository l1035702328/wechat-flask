# coding=utf-8
import os
import time
import random
import hashlib


def remove_file(path, time_value):
    while 1:
        try:
            time.sleep(time_value)
            if os.path.exists(path):
                os.remove(path)
                print("已删除" + path)
                break
            else:
                print("文件已被删除")
                break
        except:
            print("文件被打开")
            continue


def update_md5(file_path):
    with open(file_path, 'rb+') as fd:
        hash_v1 = hashlib.md5(fd.read()).hexdigest()
        print(hash_v1)
        fd.close()
    with open(file_path, 'ab+') as ff:
        hash_value = str(random.getrandbits(128))
        ff.write(hash_value.encode('utf-8'))
        hash_v2 = hashlib.md5(ff.read()).hexdigest()
        print(hash_v2)
        ff.close()
