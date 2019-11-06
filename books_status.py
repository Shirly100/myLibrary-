# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:25:41 2019

@author: Shirly
"""
import sqlite3
import datetime
from collections import deque
def connect_db():
    return sqlite3.connect('myLibrary.db')

from enum import Enum
class Status(Enum):
   available = "available"
   borrowed= "borrowed"



if __name__== "__main__":
    now = datetime.date.today()
    info={}
    book_request={}#who ordered the book
    db = connect_db()
    cursor = db.execute('SELECT book_name FROM book;')
    for row in cursor.fetchall():
        info[row[0]]={"status":Status.available.value, "reader ID":0, "borrowed date":now, "due date":now}
        book_request[row[0]]=deque()
    
    
  

