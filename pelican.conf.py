#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Daniel Roseman"
SITENAME = u"rosemanblog"
SITEURL = 'http://blog.roseman.org.uk'

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
SOCIAL = (('twitter', 'http://twitter.com/danielroseman'),
          ('github', 'http://github.com/danielroseman'),)

RELATIVE_URLS = False
DEFAULT_PAGINATION = 10
CREATE_CLEAN_URLS = False
LINK_CLEAN_URLS = True
REVERSE_CATEGORY_ORDER = True
#ARTICLE_PERMALINK_STRUCTURE = '%Y/%m/%d/'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
TWITTER_USERNAME = 'danielroseman'
DISQUS_SITENAME = 'rosemanblog'
THEME = 'notmyidea'
FEED_RSS = 'feeds/all.xml'
TAG_FEED = 'feeds/tags/%s.xml'
AUTHOR_URL = 'author/{slug}.html'
GOOGLE_ANALYTICS = 'UA-11944054-1'
