from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://feeds.soundcloud.com/users/soundcloud:users:310830713/sounds.rss"
url2 = "http://feeds.soundcloud.com/users/soundcloud:users:286452905/sounds.rss"
url3 = "http://feeds.soundcloud.com/users/soundcloud:users:310425469/sounds.rss"
url4 = "http://feeds.soundcloud.com/users/soundcloud:users:477620601/sounds.rss"
url5 = "https://podcasts.apple.com/us/podcast/wbai-news-with-paul-derienzo/id1245761118"
url6 = "http://feeds.soundcloud.com/users/soundcloud:users:640704198/sounds.rss"
url7 = "http://feeds.soundcloud.com/users/soundcloud:users:310622696/sounds.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000),
            'path': "https://streams.pacifica.org:9000/wbai_128",
            'thumbnail': "https://www.wbai.org/podcast/src/images/podcast-logo.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts127/v4/8d/f6/e1/8df6e1f2-3334-1004-c378-3d1ec887600e/mza_7885962605268436256.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://www.wbai.org/images/TrumpWatchJesseLent300.png"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://www.wbai.org/images/mansion_backend.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://www.wbai.org/images/leonard.png"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://www.wbai.org/images/Pauldraw.png"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://www.wbai.org/images/wfb300.png"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://www.wbai.org/images/how-to-make-it-_backend.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

if __name__ == '__main__':
    plugin.run()
