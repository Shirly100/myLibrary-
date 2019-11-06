# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:52:10 2019

@author: Shirly
project: my library
"""


from libraryApp import app
from libraryApp import func



if __name__ == '__main__':
    app.before_first_request(func)
    app.run()
   

