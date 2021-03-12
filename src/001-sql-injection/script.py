#!/bin/python

import pymysql

def run(name):
    db = pymysql.connect("localhost","root","root","mydb" )
    cur = db.cursor()
    cur.execute("SELECT * FROM USER WHERE NAME = '%s'" % name)
    db.close()
