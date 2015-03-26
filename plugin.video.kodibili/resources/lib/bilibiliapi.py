# -*- coding: utf-8 -*-

__author__ = 'yesh233'

import requests
import hashlib
import json
import urllib
import bilibili


class BiliBiliAPI(object):
    __app_key = '85eb6835b0a1034e'
    __secret_key = '2ad42749773c441109bdc0191257a664'
    __ver = '0.98.72'
    __ua = 'Biligrab / ' + __ver + ' (cnbeining@gmail.com)'
    __headers = {'User-Agent': __ua}
    __api_url = 'http://api.bilibili.com/'

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
    def get_type_name(tid):
        return bilibili.BiliBiliList(BiliBiliAPI.api('list', {'tid':tid})).get_name()