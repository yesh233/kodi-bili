from xbmcswift2 import Plugin
from resources.lib.bilibiliapi import *
plugin = Plugin()


@plugin.route('/')
def index():
    bilindex = BiliBiliAPI.get_index()
    items = [{'label': name} for name, list in bilindex.get_index()]
    return items

