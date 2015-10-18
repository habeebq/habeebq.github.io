#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'habeebq'
SITENAME = u'BITSMASHING'
SITEURL = ''
SITEDESCRIPTION = 'Randomizing the unknown...'

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
          ('google-plus', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']
LOAD_CONTENT_CACHE = False
MAIN_MENU = True
MENUITEMS = (('projects', '/projects.html'),
             ('whoami', '/about.html'))

THEME = '/home/habeeb/workspace/habeebq.github.io/blog/pelican-bootstrap3'
#BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'cosmo'
PYGMENTS_STYLE  = 'monokai'
ABOUT_ME = 'Writing something about the author'
# Header
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

# Fixing the tables formatting
PLUGIN_PATHS = ['/home/habeeb/workspace/pelican_plugins/pelican-bootstrapify']
PLUGINS = ['bootstrapify']
# Bootstrap extra css
CUSTOM_CSS = 'theme/css/custom.css'
GOOGLEFONT = 'https://fonts.googleapis.com/css?family=Source+Sans+Pro'
