# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:52:04 2018

@author: YHF
"""

import web.py

urls = (
'/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
app.run()