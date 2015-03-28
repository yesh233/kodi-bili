# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin, xbmc, xbmcgui
from resources.lib.bilibiliapi import BiliBiliAPI
import ChineseKeyboard as m
import time


bilindex = BiliBiliAPI.get_index()
plugin = Plugin()


@plugin.route('/')
def index():
    item = [{'label': u'首页', 'path': plugin.url_for('show_index_subjects')},
            {'label': u'搜索', 'path': plugin.url_for('show_search')}]
    items = [{'label': name, 'path': plugin.url_for('show_list_firstpage', type_idx=idx)}
             for (name, idx) in bilindex.get_names()]
    return item + items


@plugin.route('/search/')
def show_search():
    keyboard = m.Keyboard('', u'请输入关键字进行搜索')
    keyboard.doModal()
    if keyboard.isConfirmed():
        keyword = unicode(keyboard.getText(), 'utf-8')
        return show_search_list(keyword)

@plugin.route('/search/keyword/<keyword>/<page>')
def show_search_list(keyword, page=1):
    search_list = BiliBiliAPI.get_search(keyword, page)
    items = [{'label': item.get_title(),
              'path': plugin.url_for('show_search_item', idx=item.get_id(), stype=item.get_type())}
             for item in search_list.get_list()]
    if int(page) != 1:
        items.append({'label': u'上一页('+str(int(page)-1)+'/'+str(search_list.get_pages())+')',
                      'path': plugin.url_for('show_search_list',
                                             keyword=unicode(keyword).encode('utf-8'),
                                             page=int(page)-1)})
    if int(page) != int(search_list.get_pages()):
        items.append({'label': u'下一页('+str(int(page)+1)+'/'+str(search_list.get_pages())+')',
                      'path': plugin.url_for('show_search_list',
                                             keyword=unicode(keyword).encode('utf-8'),
                                             page=int(page)+1)})
    return items


@plugin.route('/search/item/<stype>/<idx>/')
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

@plugin.route('/list/<type_idx>/<page>')
@plugin.route('/list/<type_idx>/', name='show_list_firstpage')
def show_list(type_idx, page=1):
    bilist = BiliBiliAPI.get_list(type_idx, page)
    items = [{'label': item.get_title(), 'path': plugin.url_for('show_play', aid=item.get_aid())}
             for item in bilist.get_list()]
    if int(page) != 1:
        items.append({'label': u'上一页('+str(int(page)-1)+'/'+str(bilist.get_pages())+')',
                      'path': plugin.url_for('show_list', type_idx=type_idx, page=int(page)-1)})
    if int(page) != int(bilist.get_pages()):
        items.append({'label': u'下一页('+str(int(page)+1)+'/'+str(bilist.get_pages())+')',
                      'path': plugin.url_for('show_list', type_idx=type_idx, page=int(page)+1)})
    return items


def __play(av_item):
    player = xbmc.Player()
    list_item = xbmcgui.ListItem(av_item.get_title(), thumbnailImage=av_item.get_pic())
    list_item.setInfo('video', {'Title': av_item.get_title()})
    player.play(BiliBiliAPI.get_url(av_item.get_cid()), list_item)


@plugin.route('/play/<aid>/')
def show_play(aid):
    av_item = BiliBiliAPI.get_av_item(aid)
    if av_item.get_pages() == 1:
        __play(av_item)
    else:
        items = []
        for p in range(1, av_item.get_pages()+1):
            items.append({'label': BiliBiliAPI.get_partname(aid, p),
                      'path': plugin.url_for('show_play_part', aid=aid, p=p)})
            if p % 5 == 0:
                time.sleep(1)
        return items


@plugin.route('/play/<aid>/p/<p>/')
def show_play_part(aid, p):
    av_item = BiliBiliAPI.get_av_item(aid, p)
    __play(av_item)


if __name__ == '__main__':
    plugin.run()
