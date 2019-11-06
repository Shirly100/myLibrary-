# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:11:51 2019

@author: Shirly
project: my library
"""

import sqlite3
import datetime
from flask import Flask, g, render_template, request
from collections import deque
app = Flask(__name__)



def connect_db():
    return sqlite3.connect('myLibrary.db')
from enum import Enum
class Status(Enum):
   available = "available"
   borrowed= "borrowed"

@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def hello_world():
    cursor = g.db.execute('SELECT author, book_name FROM book;')
    books = [dict(author=row[0], name=row[1], picture="static/booksCover/{}_{}.jpg".format(row[1], row[0])) for row in cursor.fetchall()]
    print(books)
    return render_template('database/booksList.html', books=books)


@app.route('/book/<book_name>')
def book_info(book_name):
    cursor = g.db.execute('SELECT author,book_name FROM book;')
    now = datetime.date.today()
    info={}
    book_request={}#who ordered the book
    for row in cursor.fetchall():
        info[row[1]]={'picture':"booksCover/{}_{}.jpg".format(row[1], row[0]),"status":Status.available.value, "reader_ID":0, "borrowed_date":now, "due_date":now}
        book_request[row[1]]=deque()
    info["Harry Potter"]["status"]=Status.borrowed.value
    book_request["Harry Potter"].append("Reader 34")
    book_request["Harry Potter"].append("Reader 12")
    return render_template('database/book_info.html', book_name=book_name, info=info[book_name], book_request=book_request[book_name])

@app.route('/order_book/<book_name>')
def order_book(book_name):
    return render_template('database/orderBook.html', book_name=book_name)

@app.route('/handle_data/<book_name>', methods=['POST'])
def handle_data(book_name):
    Reader_ID = request.form['Reader_ID']
    
    cursor = g.db.execute('SELECT author,book_name FROM book;')
    now = datetime.date.today()
    info={}
    book_request={}#who ordered the book
    for row in cursor.fetchall():
        info[row[1]]={'picture':"booksCover/{}_{}.jpg".format(row[1], row[0]),"status":Status.available.value, "reader_ID":0, "borrowed_date":now, "due_date":now}
        book_request[row[1]]=deque()
    
    info[book_name]["status"]=Status.borrowed.value
    book_request[book_name].append("Reader "+ Reader_ID)
    print(book_name, book_request)
    return render_template('database/book_info.html', book_name=book_name, info=info[book_name], book_request=book_request[book_name])

    

    
 	
    