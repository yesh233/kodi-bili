# -*- coding: utf-8 -*-

__author__ = 'yesh233'

import unittest
from bilibiliapi import BiliBiliAPI


class BilibiliTestCase(unittest.TestCase):
    def test_api_view(self):
        self.assertEquals(BiliBiliAPI.api('view', {'id': 312943})['title'], u'【BDRip720P】翼·年代记 第一季全【华盟】')

    def test_api_index(self):
        self.assertEquals(BiliBiliAPI.api('index').keys(),
                          [u'type36', u'type11', u'type119', u'type3', u'type5',
                           u'type4', u'type23', u'type1', u'type13', u'type129'])

    def test_api_search(self):
        print BiliBiliAPI.api('search', {'keyword': u'洛天依'})['result'][0].keys()

    def test_api_list(self):
        print BiliBiliAPI.api('list', {'tid': 3})['results']