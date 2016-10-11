#http://live.bilibili.com/liveact/ajaxGetMedalRankList?roomid=

import random
import requests
import time
import urllib
import json
import threading

##todo: 断点续查 多线程排序 免查房间 编码头问题

def PaoXunZhang(roomid):
    url = 'http://live.bilibili.com/liveact/ajaxGetMedalRankList?roomid='+ str(roomid)
    req = requests.request(url=url,method='GET')
    if(req):
        req=json.loads(req.content.decode())
        print(str(roomid))
        try:
            if(req['data']['list'][0]['medalName']):
                print(req['data']['list'][0]['medalName'])
                try:
                    output.write(req['data']['list'][0]['medalName']+','+str(roomid)+'   ')
                    output.flush()
                except Exception as e:
                    print(e);
                    logput.write(e)
                    logput.flush()
        except:
            pass

logput=open('log.txt', 'w+')
output = open('PaoXunZhang.txt', 'w+')

def main():
    ##创建线程池
    threads = []
    threadsNum=20
    for i in range(0,threadsNum):
        threads.append(threading.Thread())

    x=1000 ##起始房间号 低于1000均为假房间号
    while x<1000000: ##终止房间号
        for i in range(0,threadsNum):
            if threads[i].isAlive()==False:
                threads[i]=threading.Thread(target=PaoXunZhang,args=(x,))
                threads[i].start()
                x+=1
    sleep(30) ##超时等待


if __name__ == "__main__":
    main()