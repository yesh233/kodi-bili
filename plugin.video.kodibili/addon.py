# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin
from resources.lib.bilibiliapi import *
plugin = Plugin()


@plugin.route('/')
def index():
    bilindex = BiliBiliAPI.get_index()
    items = [{'label': u'a', 'path': plugin.url_for('show_index_subjects')}]
    items.extend([{'label': name, 'path': plugin.url_for('show_list', type_idx=idx, name=name)}
                  for (name, idx) in bilindex])
    return items


@plugin.route('/subjects/')
def show_index_subjects():
    bilindex = BiliBiliAPI.get_index()
    items = [{'label': name, 'path': plugin.url_for('show_index_subject', type_idx=idx, name=name)}
             for (name, idx) in bilindex]
    return items


@plugin.route('/subject/<name>/')
def show_index_subject(type_idx, name):
    pass


@plugin.route('/list/<name>/')
def show_list(type_idx, name):
    pass