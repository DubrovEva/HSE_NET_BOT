import sqlite3
con = sqlite3.connect('../database/info.db')

con.execute('''CREATE TABLE users
               (
               UserID text,
               Name text, 
               Surname text, 
               University text, 
               Faculty text, 
               Info text)''')

# con.execute("INSERT INTO users VALUES ('Илья','Коннов','ВШЭ',19)")

con.commit()