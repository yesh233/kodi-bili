# -*- coding: utf-8 -*-

__author__ = 'Yang'


class BiliBiliItem(object):
    def __init__(self, item):
        self.__title = item['title']
        self.__pic = item['pic']
        self.__description = item['description']

    def get_title(self):
        return self.__title

    def get_pic(self):
        return self.__pic

    def get_description(self):
        return self.__description


class BiliBiliAVItem(BiliBiliItem):
    def __init__(self, item):
        BiliBiliItem.__init__(self, item)
        self.__pages = item['pages']
        self.__cid = item['cid']

    def get_pages(self):
        return int(self.__pages)

    def get_cid(self):
        return self.__cid


class BiliBiliListItem(BiliBiliItem):
    def __init__(self, item):
        BiliBiliItem.__init__(self, item)
        self.__aid = item['aid']

    def get_aid(self):
        return self.__aid


class BiliBiliSearchItem(BiliBiliItem):
    def __init__(self, item):
        BiliBiliItem.__init__(self, item)
        self.__type = item['type']
        if self.__type == 'mylist':
            self.__id = item['lid']
        elif self.__type == 'video':
            self.__id = item['aid']
        elif self.__type == 'special':
            self.__id = item['spid']

    def get_type(self):
        return self.__type

    def get_id(self):
        return self.__id


class BiliBiliSearchList(object):
    def __init__(self, item):
        self.__pages = item['numPages']
        self.__search_list = [BiliBiliSearchItem(it) for it in item['result']]

    def get_list(self):
        return tuple(self.__search_list)

    def get_pages(self):
        return self.__pages


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

    def get_pages(self):
        return self.__pages


class BiliBiliIndex(object):
    __type_dict = {'type1': u'动画', 'type4': u'游戏', 'type5': u'娱乐', 'type11': u'电视剧', 'type13': u'番剧',
                   'type23': u'电影', 'type36': u'科技', 'type119': u'鬼畜', 'type3': u'音乐', 'type129' :u'舞蹈'}

    def __init__(self, biliindex):
        self.__index = dict([(name, [BiliBiliListItem(biliindex[name][idx])
                                     for idx in sorted(biliindex[name]) if idx != 'num'])
                             for name in biliindex])

    def __get_type_name(self, idx):
        return BiliBiliIndex.__type_dict[idx]

    def get_names(self):
        return tuple([(self.__get_type_name(name), name[4:]) for name in sorted(self.__index)])

    def get_subject_list(self, idx):
        return self.__index['type'+idx]