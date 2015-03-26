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
        self.__list = [BiliBiliListItem(bilist['list'][idx]) for idx
                       in sorted(bilist['list']) if idx != 'num']

    def get_name(self):
        return self.__name

    def get_list(self):
        return tuple(self.__list)


class BiliBiliIndex(object):
    __type_dict = {'type1': u'动画', 'type4': u'游戏', 'type5': u'娱乐', 'type11': u'电视剧', 'type13': u'番剧',
                   'type23': u'电影', 'type36': u'科技', 'type119': u'鬼畜', 'type3': u'音乐', 'type129' :u'舞蹈'}

    def __init__(self, biliindex):
        self.__index = dict([(name, [BiliBiliListItem(biliindex[name][idx])
                                     for idx in sorted(biliindex[name]) if idx != 'num'])
                             for name in biliindex])

    def __get_type_name(self, idx):
        return BiliBiliIndex.__type_dict[idx]

    def get_index(self):
        return tuple([(self.__get_type_name(name), self.__index[name]) for name in sorted(self.__index)])