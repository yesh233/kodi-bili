from xbmcswift2 import Plugin


plugin = Plugin()


@plugin.route('/')
def index():
    items = [
        {'label': 'Hola XBMC!', 'path': plugin.url_for('show_label', label='spanish')},
        {'label': 'Bonjour XBMC!', 'path': plugin.url_for('show_label', label='french')},
    ]
    return items


@plugin.route('/labels/<label>/')
def show_label(label):
    # Normally we would use label to parse a specific web page, in this case we are just
    # using it for a new list item label to show how URL parsing works.
    items = [
        {'label': label, 'path': plugin.url_for('show_videos')},
    ]
    return items


@plugin.route('/videos/')
def show_videos():
    items = [
        {'label': 'Calculus: Derivatives 1',
         'path': 'http://s3.amazonaws.com/KA-youtube-converted/ANyVpMS3HL4.mp4/ANyVpMS3HL4.mp4',
         'is_playable': True,
         }
    ]
    return plugin.finish(items)


