#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'habeebq'
SITENAME = u'Bitsmashing'
SITEURL = ''
SITEDESCRIPTION = 'Randomizing the unknown...'
SITELOGO = u'https://habeebq.files.wordpress.com/2013/11/11412.jpg'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org'))

# Social widget
SOCIAL = (('linkedin', '#'),
          ('google', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']
LOAD_CONTENT_CACHE = False
MAIN_MENU = True
MENUITEMS = (('projects', '/projects.html'),
             ('whoami', '/about.html'))

THEME = '/home/habeeb/workspace/pelican_themes/pelican-bootstrap3'
USE_LESS = True
BOOTSTRAP_THEME = 'slate'
PYGMENTS_STYLE  = 'solarizeddark'
