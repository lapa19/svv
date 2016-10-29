
import urllib2
import MySQLdb
from bs4 import BeautifulSoup
req = urllib2.Request("https://duckduckgo.com/?q=harry+potter&ia=news",headers={'User-Agent':"Google Chrome"})
con=urllib2.urlopen(req)
content = con.read()
soup = BeautifulSoup(content)

title=soup.find_all("a",{"class":"result__a"})
link=soup.find_all("a",{"class":"result__url"})
para=soup.find_all("div",{"class":"result__snippet"})

print title
titles=[]
links = []
paras = []
print "hi"
for t,l,p in zip(title,link,para):
	print "hello"
	titles.append(t.getText())
	links.append(l.getText())
	paras.append(p.getText())
	print t.getText()

'''

# Open database connection
db = MySQLdb.connect(db='svv', user='root', passwd='', unix_socket="/opt/lampp/var/mysql/mysql.sock")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS ddg")

# Create table as per requirement
sql = """CREATE TABLE ddg
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
	#sql = "INSERT INTO ddg \
	#	(TITLE, LINK, DESC) \
	#	VALUES ('%s', '%s', '%s')" % (t,l,p)
	query = "INSERT INTO ddg(title,link,description) " \
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
'''

f=open('linksddg.txt','w');
for t,l,p in zip(titles,links,paras):
	f.write(t.encode('utf8'))
	f.write("\n")
	f.write(l.encode('utf8'))
	f.write("\n")
	f.write(p.encode('utf8'))
	f.write("\n\n")
