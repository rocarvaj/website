# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    "name": "Rodolfo Carvajal",  # your site name
    "url": "http://www2.isye.gatech.edu/~rcarvajal3/",  # your site url
    # "prefix": "blog",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    "source": "content",
    "output": "../public_html",
    "static": "deploy/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{filename}}",
    "relative_url": True,
    "perpage": 30,
    "feedcount": 20,
    "timezone": "-05:00",
}


author = {
    "default": "Rodolfo Carvajal",
    "vars": {}
}

#: active readers
reader = {
    "active": [
        "liquidluck.readers.markdown.MarkdownReader",
        # uncomment to active rst reader.
        # but you need to install docutils by yourself
        # "liquidluck.readers.restructuredtext.RestructuredTextReader",
    ],
    "vars": {}
}

#: active writers
writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        # "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        # "liquidluck.writers.core.TagCloudWriter",
    ],
    "vars": {
        # uncomment if you want to reset archive page
         "archive_output": "archive.html",
    }
}

#: theme variables
theme = {
    "name": "moment",

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    "vars": {
            "navigation": [
				{'title': "Log:Work", 'link': '/~rcarvajal3/work/'},
				{'title': "Log:Life", 'link': '/~rcarvajal3/life/'},
                    {'title': "About", 'link': '/~rcarvajal3/about.html'},
                    ],
        #"disqus": "rocarvaj",
        #"analytics": "UA-21475122-1",
        'elsewhere': [
			{'name': 'Google+', 'link': 'https://plus.google.com/u/0/105280383427274235902/about'},
                {'name': 'Twitter', 'link': 'http://twitter.com/rocarvaj'},
                ]
        }
}

#: template variables
template = {
    "vars": {},
    "filters": {},
}
