# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin, xbmc
from resources.lib.bilibiliapi import BiliBiliAPI
import ChineseKeyboard as m
bilindex = BiliBiliAPI.get_index()
plugin = Plugin()


@plugin.route('/')
def index():
    item = [{'label': u'首页', 'path': plugin.url_for('show_index_subjects')},
            {'label': u'搜索', 'path': plugin.url_for('show_search')}]
    items = [{'label': name, 'path': plugin.url_for('show_list', type_idx=idx)}
             for (name, idx) in bilindex.get_names()]
    return item + items


@plugin.route('/search/')
def show_search():
    keyboard = m.Keyboard('', u'请输入关键字进行搜索')
    keyboard.doModal()
    if keyboard.isConfirmed():
        keyword = keyboard.getText()
        items = [{'label': item.get_title()} for item in BiliBiliAPI.get_search(keyword).get_list()]
        return items


@plugin.route('/subjects/')
def show_index_subjects():
    items = [{'label': name, 'path': plugin.url_for('show_index_subject', type_idx=idx)}
             for (name, idx) in bilindex.get_names()]
    return items


@plugin.route('/subject/<type_idx>/')
def show_index_subject(type_idx):
    items = [{'label': item.get_title(), 'path': plugin.url_for('show_play', aid=item.get_aid())}
             for item in bilindex.get_subject_list(type_idx)]
    return items


@plugin.route('/list/<type_idx>/')
def show_list(type_idx):
    bilist = BiliBiliAPI.get_list(type_idx)
    items = [{'label': item.get_title(), 'path': plugin.url_for('show_play', aid=item.get_aid())}
             for item in bilist.get_list()]
    return items


@plugin.route('/play/<aid>/')
def show_play(aid):
    avitem = BiliBiliAPI.get_av_item(aid)
    if avitem.get_pages() == 1:
        player = xbmc.Player()
        player.play(BiliBiliAPI.get_url(avitem.get_cid()))

if __name__ == '__main__':
    plugin.run()
