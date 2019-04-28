#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cameron Cairns'
SITENAME = 'Home Page of Cameron Cairns'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('github', 'https://www.github.com/cameroncairns'),
    ('twitter', 'https://www.twitter.com/camerongcairns'),
    ('linkedin', 'https://www.linkedin.com/cameroncairns'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [('Home', '/'), ('About', '/pages/about.html'),]

DEFAULT_PAGINATION = 10

THEME = "brutalist"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'cartoon-headshot.jpeg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Collection of tech related musings'
## path to favicon
FAVICON = 'cartoon-headshot.jpeg'
## path to logo for nav menu (optional)
LOGO = 'cartoon-headshot.jpeg'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Cameron'
## google analytics (fake code commented out)
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@camerongcairns'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = True
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
TWITTER = 'https://twitter.com/camerongcairns'
GITHUB = 'https://github.com/cameroncairns'
LINKEDIN = 'https://linkedin.com/cameroncairns'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
## DISQUS_SITENAME = 'brutalistpelican'
## Gravatar
## Commenting mine out so you can see how the theme looks without one
## See https://mamcmanus.com to see what it looks like with a Gravatar
# GRAVATAR = 'https://www.gravatar.com/avatar/a5544bcae63c5d56c0b7a3fa0ab5b295?s=256'

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap',]

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}
