import sqlite3

#a db named jarvis will be created
conn = sqlite3.connect("jarvis.db")

#cursor to execute sql commands and fetch data from resukt sets in a database connection
cursor = conn.cursor()

#creating a table named user with columns id, name, path
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#insert values to the created table
#One note
#query = "INSERT INTO sys_command VALUES (null,'one note','C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
#cursor.execute(query)
#conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'chatgpt','https://chatgpt.com/?model=auto')"
cursor.execute(query)
conn.commit()