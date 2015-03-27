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

    def no_get_type_name(self):
        print BiliBiliAPI.get_type_name(129)

    def test_get_av_item(self):
        self.assertEqual(BiliBiliAPI.get_av_item(1845128).get_cid(), 2840169)
        self.assertEqual(BiliBiliAPI.api('view', {'id': 637684, 'page': 2})['partname'],
                         u'Episode 2~「赚著作权诉讼的钱？！」')
        #self.assertEqual(BiliBiliAPI.api('view', {'id': 2147573, 'page': 1}).keys(), [u'allow_feed', u'favorites', u'partname', u'pic', u'tag', u'title', u'review', u'coins', u'mid', u'tid', u'play', u'description', u'cid', u'video_review', u'spid', u'pages', u'src', u'created', u'allow_bp', u'created_at', u'author', u'offsite', u'typename', u'credit', u'instant_server'])

    def test_cid_api(self):
        self.assertEqual(BiliBiliAPI.cid_api(2840169).getElementsByTagName('url')[1].parentNode.nodeName,
                         'backup_url')

    def test_get_search(self):
        self.assertEquals(BiliBiliAPI.get_search(u'中文').get_list()[0].get_type(), 'special')


class BiliBiliListTestCase(unittest.TestCase):
    def setUp(self):
        self.__bilist = BiliBiliList(BiliBiliAPI.api('list', {'tid': 36, 'order': 'new'}))

    def test_bilibililist_get_name(self):
        self.assertEquals(self.__bilist.get_name(), u'科技')


class BiliBiliIndexTestCase(unittest.TestCase):
    def setUp(self):
        self.__bilindex = BiliBiliIndex(BiliBiliAPI.api('index'))

    def test_bilibiliindex(self):
        self.assertEqual(self.__bilindex.get_names()[0][0], u'动画')


class BiliBiliAVItemTestCase(unittest.TestCase):
    def test(self):
        pass

