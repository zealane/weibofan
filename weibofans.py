#!/usr/bin/python
# -*-coding:utf-8-*-

import json
import os
import subprocess
import sys
import time
import csv
import requests


def get_fans(uid, page, type, ck):
    '''
    根据type类型，获取指定uid的粉丝或关注人数据
    :param uid: 目标用户uid
    :param page: 分页
    :param type: 类型。0：粉丝，1：关注者
    :param ck: cookie
    :return: dict
    '''
    u = 'https://weibo.com/ajax/friendships/friends'
    p = {
        "page": page,
        "uid": uid,
    }
    if type == 0:
        p.update({
            "relate": "fans",
            "type": "fans",
            "newFollowerCount": "0"
        })
    h = {
        'authority': 'weibo.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://weibo.com/u/page/follow/2671109275?relate=fans',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': ck
    }
    r = requests.get(url=u, headers=h, params=p)
    try:
        return json.loads(r.text)
    except:
        print('执行失败，cookie可能失效')
        input()
        sys.exit(1)


def write_data(uid, fan_id, name, province, city, location, type):
    '''
    追加写入结果
    :param uid:
    :param fan_id:
    :param name:
    :param province:
    :param city:
    :param location:
    :param type:
    :return:
    '''
    os.makedirs('data', exist_ok=True)
    with open(os.path.join('data', '%s___%s.txt' % (uid, type)), 'a') as f:
        # 粉丝uid   昵称  省份代码    城市代码    所在地
        f.write('%s\t%s\t%s\t%s\t%s\t\n' % (fan_id, name, province, city, location))


def write_tocsv(row_str):
    with open ("fans.csv", "w", newline='') as csvfile:
        writer = csv.writer (csvfile)
        writer.writerows (row_str)
        #    f_fan.write(row_str)
        #    f_fan.write("\n")
    csvfile.close ()

def get_appionted_fans(uid, cookie):
    type = 0
    init_info = get_fans (uid, 1, type, cookie)

    if init_info["ok"] == 0:  # 如果无法获得粉丝列表，则返回0
        display_total_number = 0
    else:
        display_total_number = init_info["display_total_number"]
    print ('%s的粉丝数：%s'%uid % display_total_number)
    page_nums = display_total_number // 20
    if (page_nums > NP):
        page_nums = NP
    print ('分页数：%s' % page_nums)

    # 开始遍历，如果只想获取部分，可直接修改display_total_number为对应数值
    for i in range (1, page_nums):
        print ('第【%s】页' % i)
        fans_list = get_fans (uid, i, type, cookie)['users']
        for fan in fans_list:
            fan_id = fan['id']
            name = fan['name']
            str = [uid, fan['id'], fan['name']]

            row_str.append (str)
        time.sleep (0.2)
        # write_data(uid, fan_id, name, province, city, location, type)

    type = 1  # 关注者
    for k in range (0, NP):
        uid = row_str[k][1]
        print ("##########【%s】#################" % k)

        # 计算对应类型的分页
        init_info = get_fans (uid, 1, type, cookie)
        if init_info["ok"] == 0:
            display_total_number = 0
        else:
            display_total_number = init_info["total_number"]
        print ('关注数：%s' % display_total_number)

        page_nums = display_total_number // 20
        if (page_nums > NP):
            page_nums = NP
        print ('分页数：%s' % page_nums)

        # 开始遍历，如果只想获取部分，可直接修改page_nums为对应数值
        for i in range (1, page_nums):
            print ('第【%s】页' % i)
            fans_list = get_fans (uid, i, type, cookie)['users']
            for fan in fans_list:
                str = [uid, fan['id'], fan['name']]
                row_str_fan.append (str)
            time.sleep (0.2)
        write_tocsv(row_str_fan)

if __name__ == '__main__':
    NP = 20
    row_str = []        # 大V的粉丝
    row_str_fan = []    # 粉丝的关注对象
    # 获取用户输入参数
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ck = input('请输入cookie,输入完成后回车:')

    uid = '1647486362'
    get_appionted_fans(uid, ck)
    uid = '7454177482'
    get_appionted_fans (uid, ck)


    # 打开输出目录
    # subprocess.Popen(
    #     r'explorer "%s"' % (os.path.join(BASE_DIR, 'data')))
    # input('\n\n运行结束,正在打开输出目录...')