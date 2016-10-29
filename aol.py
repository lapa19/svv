
import urllib2
import MySQLdb
from bs4 import BeautifulSoup
req = urllib2.Request("http://www.aolsearch.com/search?q=harry%20potter",headers={'User-Agent':"Google Chrome"})
con=urllib2.urlopen(req)
content = con.read()
soup = BeautifulSoup(content)
title=soup.find_all("h3",{"class":"hac"})
link=soup.find_all("p",{"class":"durl find"})
para=soup.find_all("p",{"property":"f:desc"})
titles=[]
links = []
paras = []
for t,l,p in zip(title,link,para):
	titles.append(t.find('a').getText())
	links.append(l.find('span').getText())
	paras.append(p.getText())

# Open database connection
db = MySQLdb.connect(db='svv', user='root', passwd='', unix_socket="/opt/lampp/var/mysql/mysql.sock")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS aol")

# Create table as per requirement
sql = """CREATE TABLE aol
(
ID int NOT NULL AUTO_INCREMENT,
title text NOT NULL,
link text,
description text,
PRIMARY KEY (ID)
)"""

cursor.execute(sql)

for t,l,p in zip(titles,links,paras):	
	# Prepare SQL query to INSERT a record into the database.
	#sql = "INSERT INTO aol \
	#	(TITLE, LINK, DESC) \
	#	VALUES ('%s', '%s', '%s')" % (t,l,p)
	query = "INSERT INTO aol(title,link,description) " \
            "VALUES(%s,%s,%s)"
	args = (t.encode('utf8'), l.encode('utf8'), p.encode('utf8'))
	try:
	   # Execute the SQL command
	   cursor.execute(query, args)
	   # Commit your changes in the database
	   print "inserted a row!"
	   db.commit()
	except:
	   # Rollback in case there is any error
	   print "failed"
	   db.rollback()

# disconnect from server
db.close()

f=open('linksaol.txt','w');
for t,l,p in zip(titles,links,paras):
	f.write(t.encode('utf8'))
	f.write("\n")
	f.write(l.encode('utf8'))
	f.write("\n")
	f.write(p.encode('utf8'))
	f.write("\n\n")
