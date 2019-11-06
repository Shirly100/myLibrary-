# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:47:50 2019

@author: sohanonx

project: my library
"""

import sqlite3
conn=sqlite3.connect('myLibrary.db')
c=conn.cursor()


def create_table_book():
    c.execute('drop table if exists book')
    c.execute('create table book ( book_name text primary key, author text  )')


def data_entry_book():
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Lord of the Rings\', \'J. R. R. Tolkien\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Little Prince\', \'Antoine de Saint-Exupery\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Harry Potter\', \'J. K. Rowling\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Hobbit\', \'J. R. R. Tolkien\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Lion, the Witch and the Wardrobe\', \'C. S. Lewis\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Adventures of Pinocchio\', \'Carlo Collodi\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Da Vinci Code\', \'Dan Brown\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Anne of Green Gables\', \'Lucy Maud Montgomery\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Gone with the Wind\', \'Margaret Mitchell\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Hunger Games\', \'Suzanne Collins\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Wind in the Willows\', \'Kenneth Grahame\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Fault in Our Stars\', \'John Green\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Gone Girl\', \'Gillian Flynn\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Animal Farm\', \'George Orwell\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Winnie-the-Pooh\', \'A. A. Milne\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Little House on the Prairie\', \'Laura Ingalls Wilder\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Tarzan\', \'Edgar Rice Burroughs\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Rainbow Magic\', \'Daisy Meadows\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'house rules\', \'Jodi Picoult\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'change of heart\', \'Jodi Picoult\')')
    c.execute('INSERT INTO book (book_name, author) VALUES ("my sister\'s keeper", \'Jodi Picoult\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'a walk to remember\', \'nicholas sparks\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'dear John\', \'nicholas sparks\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'the best of me\', \'nicholas sparks\')')
    c.execute('INSERT INTO book (book_name, author) VALUES ("What to Expect When You\'re Expecting", \'Arlene Eisenberg\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Charlie and the Chocolate Factory\', \'Roald Dahl\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Tuesdays with Morrie\', \'Mitch Albom\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'A Wrinkle in Time\', "Madeleine L\'Engle")')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Old Man and the Sea\', \'Ernest Hemingway\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Me Before You\', \'Jojo Moyes\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Cat in the Hat\', \'Dr. Seuss\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'The Help\', \'Kathryn Stockett\')')
    c.execute('INSERT INTO book (book_name, author) VALUES (\'Star Wars\', \'Various authors\')')
    
    	
    	

create_table_book()
data_entry_book()


conn.commit()
c.close()
conn.close()
