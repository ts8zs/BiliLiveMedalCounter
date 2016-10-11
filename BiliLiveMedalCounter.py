#http://live.bilibili.com/liveact/ajaxGetMedalRankList?roomid=

import random
import requests
import time
import urllib
import json
import threading

##todo: 断点续查 排序 已有房间免查 编码头

logput = open('log.txt', 'w+')
output = open('Medal.txt', 'w+')

def CheckRoom(roomid):
    url = 'http://live.bilibili.com/liveact/ajaxGetMedalRankList?roomid='+ str(roomid)
    try:
        req = requests.request(url=url,method='GET')
    except:
        CheckRoom(roomid)
        logput.write(roomid+'出错  ')
        logput.flush()
    if(req):
        req=json.loads(req.content.decode())
        try:
            if(req['data']['list'][0]['medalName']):
                print(req['data']['list'][0]['medalName'])
                try:
                    output.write(req['data']['list'][0]['medalName']+','+str(roomid)+'   ')
                    output.flush()
                except:
                    pass
        except:
            pass



def main():
    ##创建线程池
    threads = []
    threadsNum=20
    for i in range(0,threadsNum):
        threads.append(threading.Thread())

    x=1000 ##起始房间号 低于1000均为假房间号
    while x<1000000: ##终止房间号
        for i in range(0,threadsNum): ##反复遍历线程
            if threads[i].isAlive()==False:
                threads[i]=threading.Thread(target=CheckRoom,args=(x,))
                threads[i].start()
                x+=1
    sleep(30) ##超时等待


if __name__ == "__main__":
    main()