import pymysql as mysql

mysql_conn = mysql.connect(host='127.0.0.1',user='root',passwd='passme@sql',database='sys')

cursor = mysql_conn.cursor()

create_query="CREATE TABLE USERS(name VARCHAR(45), username VARCHAR(45) UNIQUE, password VARCHAR(45))"
cursor.execute(create_query)
