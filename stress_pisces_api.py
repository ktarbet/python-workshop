#!/usr/bin/env python
# usage: stress test PiscesAPI
#
import datetime
import urllib.parse
import urllib.request
from multiprocessing import Process

#http://lrgs2/pn-bin/api/daily?list=jck af&start=2012-01-01&end=2012-12-31
url = 'http://lrgs2/pn-bin/api/daily'
#url = 'http://localhost:60804/daily'

def func(tag):
    t1 = datetime.datetime(2010,1,1)
    t1 = t1 + datetime.timedelta(days=1)
    t2 = t1 + datetime.timedelta(days=10)
    i=0
    while i< 20:
       
        values = {'list': 'jck',
            'start': t1.strftime('%Y-%m-%d'),
            'end': t2.strftime('%Y-%m-%d') }

        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(url, data.encode('utf-8'))
        res = urllib.request.urlopen(req) 
        the_page = res.read()
        print (tag,' ',i,' ', len(the_page))
        i = i+1


if __name__ == '__main__':
    p1 = Process(target=func('proc1'))
    p1.start()
    p2 = Process(target=func('proc2'))
    p2.start()