# -*- coding: utf-8 -*-

__author__ = 'Yang'


class BiliBiliListItem(object):
    def __init__(self, item):
        self.__aid = item['aid']
        self.__title = item['title']
        self.__pic = item['pic']
        self.__description = item['description']

    def get_title(self):
        return self.__title

    def get_aid(self):
        return self.__aid

    def get_title(self):
        return self.__title

    def get_pic(self):
        return self.__pic

    def get_description(self):
        return self.__description


class BiliBiliList(object):
    def __init__(self, bilist):
        self.__name = bilist['name']
        self.__pages = int(bilist['pages'])
        self.__num = int(bilist['num'])
        self.__list = [BiliBiliListItem(item) for idx, item
                       in sorted(bilist['list'].iteritems()) if idx != 'num']

    def get_name(self):
        return self.__name

    def get_list(self):
        return tuple(self.__list)


class BiliBiliIndex(object):
    def __init__(self, biliindex):
        self.__index = [BiliBiliList(biliindex[name]) for name in biliindex]

    def get_lists(self):
        return tuple(self.__index)