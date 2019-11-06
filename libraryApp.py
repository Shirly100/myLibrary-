# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:11:51 2019

@author: Shirly
project: my library
"""

import sqlite3
from flask import Flask, g, render_template, request
from collections import deque
app = Flask(__name__)
from datetime import date, timedelta

def connect_db():
    return sqlite3.connect('myLibrary.db')
from enum import Enum
class Status(Enum):
   available = "available"
   borrowed= "borrowed"
   
def func():
    g.db = connect_db()
    global info
    info=dict()
    global book_request
    book_request=dict()
    cursor = g.db.execute('SELECT author,book_name FROM book;')
    now = date.today().isoformat()
    for row in cursor.fetchall():
        info[row[1]]={'picture':"booksCover/{}_{}.jpg".format(row[1], row[0]),"status":Status.available.value}
        book_request[row[1]]=deque()
    
@app.before_request
def before_request():
    g.db = connect_db()
    






@app.route('/')
def hello_world():
    cursor = g.db.execute('SELECT author, book_name FROM book;')
    books = [dict(author=row[0], name=row[1], picture="static/booksCover/{}_{}.jpg".format(row[1], row[0])) for row in cursor.fetchall()]
    return render_template('database/booksList.html', books=books)


@app.route('/book/<book_name>', methods=['POST','GET'])
def book_info(book_name):
    if request.method == 'POST' :
        if "Reader_ID" in request.form :
            Reader_ID=request.form["Reader_ID"]
            if info[book_name]["status"]==Status.available.value:
                info[book_name]["status"]=Status.borrowed.value
                info[book_name]["reader_ID"]=Reader_ID
                now = date.today().isoformat()
                info[book_name]["borrowed_date"]=now
                info[book_name]["due_date"]=(date.today()+timedelta(days=30)).isoformat()
            else:
                book_request[book_name].append("Reader "+ Reader_ID)
            return render_template('database/book_info.html', book_name=book_name, info=info[book_name], book_request=book_request[book_name])
        
        elif "return_Reader_ID" in  request.form:
            if book_request[book_name]:
                info[book_name]["status"]=Status.borrowed.value
                info[book_name]["reader_ID"]=book_request[book_name].popleft()
                
            else:
                info[book_name]["status"]=Status.available.value
                return render_template('database/book_info.html', book_name=book_name, info=info[book_name], book_request=book_request[book_name])

        
    elif request.method == 'GET' :
        return render_template('database/book_info.html', book_name=book_name, info=info[book_name], book_request=book_request[book_name])
    

       
             

        
   
    
    return render_template('database/book_info.html', book_name=book_name, info=info[book_name], book_request=book_request[book_name])

@app.route('/order_book/<book_name>')
def order_book(book_name):
    return render_template('database/orderBook.html', book_name=book_name)

@app.route('/return_book/<book_name>')
def return_book(book_name):
    reading_now=(info[book_name]["reader_ID"]).replace('Reader ',"")
    return render_template('database/returnBook.html', book_name=book_name, reading_now=reading_now)


    

    
 	
    