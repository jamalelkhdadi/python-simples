# import sqlite3
import sqlite3

# create database and connect
db = sqlite3.connect("database.db")

# setting cursor
cr = db.cursor()

# create table and fields
cr.execute("create table if not exists users (user_id integer, name text)")

# create table and fields
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# insertting data
cr.execute("insert into users(user_id, name) values(1, 'html')")
cr.execute("insert into users(user_id, name) values(2, 'css')")
cr.execute("insert into users(user_id, name) values(3, 'js')")
cr.execute("insert into users(user_id, name) values(4, 'py')")

# save commit changes
db.commit()

# close database
db.close()