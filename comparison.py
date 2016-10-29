
import urllib2
import MySQLdb
from bs4 import BeautifulSoup

def insert_db(cursor,search_engine):
	query = """SELECT * FROM %s """ % search_engine
	cursor.execute(query)
	search_results = cursor.fetchall()
	for row in search_results:
		title = row[1]
		link_1 = row[2]
		description = row[3]
		#print row
		if link_1.find("http") == -1:
			link_2 = "https://"+link_1
			link_3 = "http://"+link_1
		else:
			if link_1.find("https") == -1:
				link_2 = link_1[7:]
				link_3 = link_2+"https://"
			else:
				link_3 = link_1[8:]	
				link_2 = "http://"+link_3	
		link_exists_query = "SELECT * FROM result WHERE link = %s OR link = %s OR link = %s"
		cursor.execute(link_exists_query,(link_1,link_2,link_3))
		link_exists = cursor.fetchall()
		print link_1
		get_rank = "SELECT id FROM %s WHERE link IN ('%s','%s','%s') " % (search_engine,link_1,link_2,link_3)
		print get_rank
		cursor.execute(get_rank)
		rank = cursor.fetchall()

		if len(link_exists) == 0:
			insert_query = "INSERT INTO result (title,link,description,ranky,rankb,rankaol,rankask) \
				        VALUES (%s,%s,%s,%s,%s,%s,%s)"
			if search_engine == "yahoo":
				insert_args = (title,link_1,description,rank[0][0],int(0),int(0),int(0))
			elif search_engine == "bing":
				insert_args = (title,link_1,description,int(0),rank[0][0],int(0),int(0))
			elif search_engine == "aol":
				insert_args = (title,link_1,description,int(0),int(0),rank[0][0],int(0))
			elif search_engine == "ask":
				insert_args = (title,link_1,description,int(0),int(0),int(0),rank[0][0])
			try:
				cursor.execute(insert_query,insert_args)
				db.commit()
				print "inserted!"
			except:
				print "failed"
				db.rollback()	
		else:
			if search_engine == "yahoo":
				arg_search = "ranky"
			elif search_engine == "bing":
				arg_search = "rankb"
			elif search_engine == "ask":
				arg_search = "rankask"
			elif search_engine == "aol":
				arg_search = "rankaol"

			update_query = "UPDATE result SET %s = %s WHERE link IN ('%s','%s','%s')" % \
					(arg_search,rank[0][0],link_1,link_2,link_3)
			
			try:
				cursor.execute(update_query)
				db.commit()
				print "updated!"
			except:
				print "failed"
				db.rollback()
	 

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
insert_db(cursor,"yahoo")
insert_db(cursor,"bing")
insert_db(cursor,"aol")
insert_db(cursor,"ask")
# disconnect from server
db.close()

