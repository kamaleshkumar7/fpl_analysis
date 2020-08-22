import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def execute():
  conn = sqlite3.connect('fpl.db')
  cursor = conn.cursor()
  sql = "select * from valueteam"
  cursor.execute(sql)
  teamval = cursor.fetchall();
  conn.commit()
  sql = "select * from roiteam"
  cursor.execute(sql)
  roiteam = cursor.fetchall();
  conn.commit()
  sql = "select * from teamrot"
  cursor.execute(sql)
  teamrot = cursor.fetchall();
  conn.commit()
  sql = "select * from gkval"
  cursor.execute(sql)
  gkval = cursor.fetchall();
  conn.commit()
  sql = "select * from defval"
  cursor.execute(sql)
  defval = cursor.fetchall();
  conn.commit()
  sql = "select * from midval"
  cursor.execute(sql)
  midval = cursor.fetchall();
  conn.commit()
  sql = "select * from forval"
  cursor.execute(sql)
  forval = cursor.fetchall();
  conn.commit()
  return render_template('fpl.html',teamval=teamval,roiteam=roiteam,teamrot=teamrot,gkval=gkval,defval=defval,midval=midval,forval=forval)
  
if __name__ == '__main__':
    app.run(debug=True)