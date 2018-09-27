#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Daniel Roseman"
SITENAME = u"rosemanblog"
SITEURL = 'https://blog.roseman.org.uk'

TIMEZONE = 'Europe/London'

DEFAULT_LANG='en'

# Blogroll
#LINKS =  (
          #('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          #('Python.org', 'http://python.org'),
          #('Jinja2', 'http://jinja.pocoo.org'),
          #('You can modify those links in your config file', '#')
         #)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/danielroseman'),
    ('github', 'https://github.com/danielroseman'),
    ('stackoverflow', 'http://stackoverflow.com/users/104349/daniel-roseman', 'stack-overflow'),
    ('rss', '/feeds/all.atom.xml')
)

RELATIVE_URLS = False
DEFAULT_PAGINATION = 10
#CREATE_CLEAN_URLS = False
#LINK_CLEAN_URLS = True
REVERSE_CATEGORY_ORDER = True
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
TWITTER_USERNAME = 'danielroseman'
DISQUS_SITENAME = 'rosemanblog'
#DISQUS_NO_ID = True
#DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNTS = True
THEME = 'pelican-themes/pelican-bootstrap3'
#THEME = 'notmyidea'
BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'solarizeddark'
CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['static']
THEME_TEMPLATE_OVERRIDES = ['templates']
# Tell Pelican to change the path to 'static/custom.css' in the output dir
#EXTRA_PATH_METADATA = {
    #'extras/custom.css': {'path': 'static/custom.css'}
#}
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10
SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'category/']
}
SHOW_ARTICLE_CATEGORY = True
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud', 'sitemap']
FEED_RSS = 'feeds/all.xml'
TAG_FEED_ATOM = 'feeds/tags/%s.xml'
AUTHOR_URL = 'author/{slug}.html'
GOOGLE_ANALYTICS = 'UA-11944054-1'
