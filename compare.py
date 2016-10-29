
import urllib2
import MySQLdb
from bs4 import BeautifulSoup

# Open database connection
db = MySQLdb.connect(db='svv', user='root', passwd='', unix_socket="/opt/lampp/var/mysql/mysql.sock")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS result")

# Create table as per requirement
sql = """CREATE TABLE result
(
ID int NOT NULL AUTO_INCREMENT,
title text NOT NULL,
link text,
description text,
ranky INTEGER,
rankb INTEGER,
rankaol INTEGER,
rankask INTEGER,
PRIMARY KEY (ID)
)"""

cursor.execute(sql)

sqly = """SELECT * FROM yahoo"""
sqlbing = """SELECT * FROM bing"""
sqlaol = """SELECT * FROM aol"""
sqlask = """SELECT * FROM ask"""


cursor.execute(sqly)
results = cursor.fetchall()
print len(results)
for row in results:
	title = row[1]
	link = row[2]
	description = row[3]
	print link
	q = "SELECT * FROM result WHERE link = %s"
	qr = "SELECT id FROM yahoo WHERE link = %s"
	if link.find("https://") == -1:
		args2 = "https://"+link
	else:
		args2 = link[8:]
	args = (link.encode('utf8'))
	rank = cursor.execute(qr,args)
	rank = cursor.fetchall()
	
	r = cursor.execute(q,args)
	c = cursor.fetchall()
	r2 = cursor.execute(q,args2)
	c2 = cursor.fetchall()
	print rank[0][0]
	if len(c) == 0 and len(c2) == 0:
		sqlr = "INSERT INTO result (title,link,description,ranky,rankb,rankaol,rankask) \
			 VALUES (%s,%s,%s,%s,%s,%s,%s)"
		args = (title,link,description,rank[0][0],int(0),int(0),int(0))
		try:
			cursor.execute(sqlr,args)
			db.commit()
			print "inserted!"
		except:
			print "failed"
			db.rollback()	
	
      
cursor.execute(sqlbing)
results = cursor.fetchall()
for row in results:
	title = row[1]
	link = row[2]
	description = row[3]
	q = "SELECT * FROM result WHERE link = %s"
	qr = "SELECT id FROM bing WHERE link = %s"
	if link.find("https://") == -1:
		args2 = "https://"+link
	else:
		args2 = link[8:]
	args = (link.encode('utf8'))
	rank = cursor.execute(qr,args)
	rank = cursor.fetchall()
	r = cursor.execute(q,args)
	c = cursor.fetchall()
	r2 = cursor.execute(q,args2)
	c2 = cursor.fetchall()
	if len(c) == 0 and len(c2) == 0:
		sqlr = "INSERT INTO result(title,link,description,ranky,rankb,rankaol,rankask) \
			VALUES(%s,%s,%s,%s,%s,%s,%s)"
		args = (title,link,description,int(0),int(rank[0][0]),int(0),int(0))
		try:
			cursor.execute(sqlr,args)
			db.commit()
		except:
			db.rollback()	
	else:
		update = "UPDATE result SET rankb = %s WHERE link = %s OR link = %s"
		cursor.execute(update,(int(rank[0][0]),args,args2))

cursor.execute(sqlaol)
results = cursor.fetchall()
for row in results:
	title = row[1]
	link = row[2]
	description = row[3]
	q = "SELECT * FROM result WHERE link = %s"
	qr = "SELECT id FROM aol WHERE link = %s"
	if link.find("https://") == -1:
		args2 = "https://"+link
	else:
		args2 = link[8:]
	args = (link.encode('utf8'))
	cursor.execute(qr,args)
	rank = cursor.fetchall()
	r = cursor.execute(q,args)
	c = cursor.fetchall()
	r2 = cursor.execute(q,args2)
	c2 = cursor.fetchall()
	if len(c) == 0 and len(c2) == 0:
		sqlr = "INSERT INTO result(title,link,description,ranky,rankb,rankaol,rankask)\
			VALUES(%s,%s,%s,%s,%s,%s,%s)"
		args = (title,link,description,int(0),int(0),int(rank[0][0]),int(0))
		try:
			cursor.execute(sqlr,args)
			db.commit()
		except:
			db.rollback()
	else:
		update = "UPDATE result SET rankaol = %s WHERE link = %s OR link = %s"
		cursor.execute(update,(int(rank[0][0]),args,args2))

cursor.execute(sqlask)
results = cursor.fetchall()
for row in results:
	title = row[1]
	link = row[2]
	description = row[3]
	q = "SELECT * FROM result WHERE link = %s"
	qr = "SELECT id FROM ask WHERE link = %s"
	if link.find("https://") == -1:
		args2 = "https://"+link
	else:
		args2 = link[8:]
	args = (link.encode('utf8'))
	rank = cursor.execute(qr,args)
	rank = cursor.fetchall()
	r = cursor.execute(q,args)
	c = cursor.fetchall()
	r2 = cursor.execute(q,args2)
	c2 = cursor.fetchall()
	if len(c) == 0 and len(c2) == 0:
		sqlr = "INSERT INTO result(title,link,description,ranky,rankb,rankaol,rankask)\
			VALUES(%s,%s,%s,%s,%s,%s,%s)"
		args = (title,link,description,int(0),int(0),int(0),int(rank[0][0]))
		try:
			cursor.execute(sqlr,args)
			db.commit()
		except:
			db.rollback()
	else:
		update = "UPDATE result SET rankask = %s WHERE link = %s OR link = %s"
		cursor.execute(update,(int(rank[0][0]),args,args2))	


# disconnect from server
db.close()

