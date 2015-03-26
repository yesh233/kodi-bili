# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin
from resources.lib.bilibiliapi import *
plugin = Plugin()


@plugin.route('/')
def index():
    bilindex = BiliBiliAPI.get_index()
    items = [{'label': u'首页', 'path': plugin.url_for('show_index_subjects', bilindex=bilindex)}]
    items.extend([{'label': name, 'path': plugin.url_for('show_list', type_idx=idx, name=name)}
                  for (name, idx), _ in bilindex])
    return items


@plugin.route('/subjects/')
def show_index_subjects(bilindex):
    items = [{'label': name, 'path': plugin.url_for('show_index_subject', name=name, subject_list=subject_list)}
             for (name, idx), subject_list in bilindex]
    return items


@plugin.route('/subjects/<name>/')
def show_index_subject(name, subject_list):
    pass


@plugin.route('/list/<name>/')
def show_list(type_idx, name):
    pass