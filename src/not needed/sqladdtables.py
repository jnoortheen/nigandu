import sqlite3

con = sqlite3.connect("nofts.sqlite")
cur = con.cursor()
con.set_authorizer()

#cur.execute("CREATE TABLE SETTINGS (field text, setting text)")
#cur.execute("CREATE TABLE HISTORY (history text)")
#cur.execute("CREATE TABLE BOOKMARKS (bkm text)")

#for i, j in [("fontsize", 11),("clipauto", "True"),("histdock", "True"),("savehist", "True"),("bkmdock", "True"),("delhist", "False"),("delbkm", "False")]:
#	cur.execute("insert into SETTINGS values(?, ?)", (i, j, ))
#	print(i, j)

#con.commit()

cur.execute("select * from SETTINGS")
cuf = cur.fetchall()
print(cuf)

def printf(self):
	for i, j in cuf:
		self.i = j
		print(self.i)

printf("self")

con.close()