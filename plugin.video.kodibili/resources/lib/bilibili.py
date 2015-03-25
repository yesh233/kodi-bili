# -*- coding: utf-8 -*-

__author__ = 'yesh233'

import requests
import hashlib
import json


class Bilibili(object):
    __app_key = '85eb6835b0a1034e'
    __secret_key = '2ad42749773c441109bdc0191257a664'
    __ver = '0.98.72'
    __ua = 'Biligrab / ' + __ver + ' (cnbeining@gmail.com)'
    __headers = {'User-Agent': __ua}
    __api_url = 'http://api.bilibili.com/'

    @staticmethod
    def __string_sign(string):
        # print string
        return unicode(hashlib.md5(unicode(string).encode('utf8')).hexdigest())

    @staticmethod
    def __calc_sign(params):
        return Bilibili.__string_sign('&'.join([unicode(name)+'='+unicode(params[name]) for name in sorted(params)]) +
                                      Bilibili.__secret_key)

    @staticmethod
    def __calc_params(params):
        params['appkey'] = Bilibili.__app_key
        params['sign'] = Bilibili.__calc_sign(params)
        return params

    @staticmethod
    def api(url, params=dict()):
        # print Bilibili.__api_url+url+Bilibili.__calc_params(params)
        print requests.get(Bilibili.__api_url + url, params=Bilibili.__calc_params(params),
                           headers=Bilibili.__headers).url
        # return json.loads(requests.get(Bilibili.__api_url+url+Bilibili.__calc_params(params),
        #                   headers=Bilibili.__headers).text)

