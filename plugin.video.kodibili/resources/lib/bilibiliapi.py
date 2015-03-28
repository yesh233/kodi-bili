# -*- coding: utf-8 -*-

__author__ = 'yesh233'

import requests
import hashlib
import json
import urllib
import bilibili
from xml.dom import minidom
import time


class BiliBiliAPI(object):
    __app_key = '85eb6835b0a1034e'
    __secret_key = '2ad42749773c441109bdc0191257a664'
    __ver = '0.98.72'
    __ua = 'Biligrab / ' + __ver + ' (cnbeining@gmail.com)'
    __headers = {'User-Agent': __ua}
    __api_url = 'http://api.bilibili.com/'
    __cid_url = 'http://interface.bilibili.com/playurl'
    __play_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

    @staticmethod
    def __string_sign(string):
        return unicode(hashlib.md5(unicode(string)).hexdigest())

    @staticmethod
    def __calc_sign(params):
        return BiliBiliAPI.__string_sign('&'.join([unicode(name) + '=' +
                                                   urllib.quote(unicode(params[name]).encode('utf-8'))
                                                   for name in sorted(params)]) +
                                         BiliBiliAPI.__secret_key)

    @staticmethod
    def __calc_params(params):
        params['appkey'] = BiliBiliAPI.__app_key
        params['sign'] = BiliBiliAPI.__calc_sign(params)
        return params

    @staticmethod
    def api(url, params=dict()):
        return json.loads(requests.get(BiliBiliAPI.__api_url+url, params=BiliBiliAPI.__calc_params(params),
                          headers=BiliBiliAPI.__headers).text)

    @staticmethod
    def cid_api_url(cid):
        return requests.get(BiliBiliAPI.__cid_url, params=BiliBiliAPI.__calc_params({'cid': cid})).url

    @staticmethod
    def cid_api(cid):
        return minidom.parseString(requests.get(BiliBiliAPI.__cid_url,
                                                params=BiliBiliAPI.__calc_params({'cid': cid}),
                                                headers=BiliBiliAPI.__play_headers).text)

    @staticmethod
    def get_type_name(tid):
        return bilibili.BiliBiliList(BiliBiliAPI.api('list', {'tid': tid})).get_name()

    @staticmethod
    def get_index():
        return bilibili.BiliBiliIndex(BiliBiliAPI.api('index'))

    @staticmethod
    def get_list(tid):
        return bilibili.BiliBiliList(BiliBiliAPI.api('list', {'tid': tid}))

    @staticmethod
    def get_av_item(aid, page=1):
        return bilibili.BiliBiliAVItem(BiliBiliAPI.api('view', {'id': aid, 'page': page}))

    @staticmethod
    def get_url(cid):
        dom = BiliBiliAPI.cid_api(cid).getElementsByTagName('url')
        return 'stack://'+' , '.join([str(el.childNodes[0].data) for el in dom
                                      if el.parentNode.nodeName != 'backup_url'])

    @staticmethod
    def get_search(keyword):
        return bilibili.BiliBiliSearchList(BiliBiliAPI.api('search', {'keyword': keyword}))

    @staticmethod
    def get_partname(aid, p):
        time.sleep(1)
        return BiliBiliAPI.api('view', {'id': aid, 'page': p})['partname']
