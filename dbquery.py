import sqlite3
conn = sqlite3.connect('fpl.db')
cursor = conn.cursor()
#create_query ='''CREATE TABLE valueteam(
  # team CHAR(100) NOT NULL,
 #  value CHAR(20)
#)'''
select_query = "select * from forval"
#insert_query = "insert into forval values(?,?,?)"
#delete_query = "delete from forval"
cursor.execute(select_query)
result = cursor.fetchall();
print(result)
conn.commit()
conn.close()
