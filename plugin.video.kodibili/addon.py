# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin
from resources.lib.bilibiliapi import *
plugin = Plugin()
bilindex = BiliBiliAPI.get_index()

@plugin.route('/')
def index():
    items = [{'label': u'首页', 'path': plugin.url_for('show_index_subjects')}]
    items.extend([{'label': name, 'path': plugin.url_for('show_list', type_idx=idx)}
                  for (name, idx) in bilindex.get_names()])
    return items


@plugin.route('/subjects/')
def show_index_subjects():
    items = [{'label': name, 'path': plugin.url_for('show_index_subject', type_idx=idx)}
             for (name, idx) in bilindex.get_names()]
    return items


@plugin.route('/subject/<type_idx>/')
def show_index_subject(type_idx):
    items = [{'label': item.get_title()} for item in bilindex.get_subject_list(type_idx)]
    return items

@plugin.route('/list/<type_idx>/')
def show_list(type_idx):
    bilist = BiliBiliAPI.get_list(type_idx)
    items = [{'label': item.get_title()} for item in bilist.get_list()]
    return items