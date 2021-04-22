# Just for tests
# Don't upload
import mysql.connector
import sqlite3 # MySQL doesn't want to work, so I'm switching to SQLite3
import goslate
import time


# text = "Hello world!"
#
# gs = goslate.Goslate()
# time.sleep(3)
# translatedText = gs.translate(text,'fr')
#
# print(translatedText)

# TestVar = input("Saomething for the database")

conn = sqlite3.connect('database.db')

cur = conn.cursor()

# Three " means docstring, so multi-line commands can be made
# cur.execute("""CREATE TABLE messages
#             (username text, message text)""") #Makes table (Delete after first use I think)

# cur.execute("INSERT INTO messages VALUES ('Matthew', 'Hello world!')") # Inserts into the table the stated values,
                                                                         # in column order specified above
for row in cur.execute("SELECT * FROM messages "):
    print(row)

# conn.commit() # Saves changes
#
# conn.close() # Closes connection
