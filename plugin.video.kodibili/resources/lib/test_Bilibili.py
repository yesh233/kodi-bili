# -*- coding: utf-8 -*-

__author__ = 'yesh233'

import unittest
import bilibili


class BilibiliTestCase(unittest.TestCase):
    def setUp(self):
        self.__bilibili = bilibili.Bilibili()
    #
    # def test_api_view(self):
    #     self.assertEquals(self.__bilibili.api('view', {'id': 312943})['title'], u'【BDRip720P】翼·年代记 第一季全【华盟】')
    #
    # def test_api_index(self):
    #     self.assertEquals(self.__bilibili.api('index').keys(),
    #                       [u'type36', u'type11', u'type119', u'type3', u'type5',
    #                        u'type4', u'type23', u'type1', u'type13', u'type129'])

    def test_api_search(self):
        print self.__bilibili.api('search', {'keyword': u'中文'})

    def test_api_list(self):
        print self.__bilibili.api('list', {'tid': 33})