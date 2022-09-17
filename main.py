#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import random
from concurrent.futures import ThreadPoolExecutor, wait
from time import sleep

import pytz as pytz
import requests

# 在此填写你的t参数
t = ''

# 自动闯关
def auto(n):
    global t
    print(f'🕙 闯关任务[{n}]执行中...')
    url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=0&rank_role=1&skin=1'
    headers = {
        't': t,
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/18/page-frame.html'
    }
    res = requests.get(url, headers=headers, timeout=60)
    res = json.loads(res.content)
    if res['err_code'] == 0:
        print('🥇 闯关数据刷入成功')
        return
    print('❌ 数据刷入失败：' + res['err_msg'])


# 自动话题
def huati(n):
    global t
    print(f'🕙 话题任务[{n}]执行中...')
    url = 'https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over?rank_score=1&rank_state=1&rank_time=0&rank_role=2&skin=22'
    headers = {
        't': t,
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/18/page-frame.html'
    }
    res = requests.get(url, headers=headers, timeout=60)
    res = json.loads(res.content)
    if res['err_code'] == 0:
        print('🥇 话题数据刷入成功')
        return
    print('❌ 话题数据刷入失败：' + res['err_msg'])

# 个人信息查询
def userInfo():
    global t
    url = 'https://cat-match.easygame2021.com/sheep/v1/game/personal_info'
    headers = {
        't': t,
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/18/page-frame.html'
    }
    try:
        res = requests.get(url, headers=headers, timeout=60)
        res = json.loads(res.content)
        nickName = res['data']['nick_name']
        dailyCount = res['data']['daily_count']
        todayTs = res['data']['today_ts']
        t = datetime.datetime.fromtimestamp(int(todayTs), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        print(f'♨️ 游戏用户[{nickName}] | 成功次数: {dailyCount} | 完成时间[{t}]')
    except Exception:
        print('❌ 获取用户信息异常！')


if __name__ == '__main__':
    print('🐑 了个 🐑 自动化脚本开启\n------------------------')
    # t 是线程数
    th = 1000
    executor = ThreadPoolExecutor(max_workers=th)
    n = 0
    while 1:
        n = n + 1
        try:
            all_task = [executor.submit(auto, (n))]
            all_task = [executor.submit(huati, (n))]
        except Exception as e:
            print('❌ 数据刷入失败')
            print(e)
        stime = random.randint(3, 5)
        stime = 0
        if n % th == 0:
            userInfo()
            wait(all_task)