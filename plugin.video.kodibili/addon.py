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
        keyword = unicode(keyboard.getText(), 'utf-8')
        items = [{'label': item.get_title(),
                  'path': plugin.url_for('show_search_item', idx=item.get_id(), stype=item.get_type())}
                 for item in BiliBiliAPI.get_search(keyword).get_list()]
        return items

@plugin.route('/search/<stype>/<idx>/')
def show_search_item(idx, stype):
    if stype == 'video':
        return show_play(idx)
    elif stype == 'special':
    # TODO stype == special
        print 'special'

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
    av_item = BiliBiliAPI.get_av_item(aid)
    if av_item.get_pages() == 1:
        player = xbmc.Player()
        player.play(BiliBiliAPI.get_url(av_item.get_cid()))
    else:
        items = [{'label': BiliBiliAPI.get_partname(aid, p),
                  'path': plugin.url_for('show_play_part', aid=aid, p=p)}
                 for p in range(1, av_item.get_pages()+1)]
        return items


@plugin.route('/play/<aid>/p/<p>/')
def show_play_part(aid, p):
    av_item = BiliBiliAPI.get_av_item(aid, p)
    player = xbmc.Player()
    player.play(BiliBiliAPI.get_url(av_item.get_cid()))


if __name__ == '__main__':
    plugin.run()
