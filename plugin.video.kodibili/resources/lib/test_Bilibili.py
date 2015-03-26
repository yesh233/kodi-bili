# -*- coding: utf-8 -*-

__author__ = 'yesh233'

import unittest
from bilibiliapi import *
from bilibili import *


class BiliBiliAPITestCase(unittest.TestCase):
    def test_api_view(self):
        self.assertEquals(BiliBiliAPI.api('view', {'id': 312943})['title'], u'【BDRip720P】翼·年代记 第一季全【华盟】')

    def test_api_index(self):
        self.assertEquals(BiliBiliAPI.api('index').keys(),
                          [u'type36', u'type11', u'type119', u'type3', u'type5',
                           u'type4', u'type23', u'type1', u'type13', u'type129'])

    def test_get_type_name(self):
        self.assertEqual(BiliBiliAPI.get_type_name(33), u'连载动画')


class BiliBiliListTestCase(unittest.TestCase):
    def setUp(self):
        self.__bilist = BiliBiliList(BiliBiliAPI.api('list', {'tid': 36, 'order': 'new'}))

    def test_bilibililist_get_name(self):
        self.assertEquals(self.__bilist.get_name(), u'科技')


class BiliBiliIndexTestCase(unittest.TestCase):
    def setUp(self):
        self.__bilindex = BiliBiliIndex(BiliBiliAPI.api('index'))

    def test_bilibiliindex(self):
        self.assertEqual(BiliBiliAPI.get_type_name(self.__bilindex.get_index()[0][0]), u'动画')
