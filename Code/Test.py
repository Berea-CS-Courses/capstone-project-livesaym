# Just for tests
# Don't upload
import sqlite3  # MySQL doesn't want to work, so I'm switching to SQLite3
import time
import random
from google_trans_new import google_translator

text = ["Hello", "Greetings", "What", "is", "up", "dog"]
username = "Matthew"
finished_text = [':', ' ']
translator = google_translator()
for i in text:
    potential_languages = ['de', 'ko', 'ja', 'la']
    chosen_language = random.choice(potential_languages)
    print(i)
    translate_text = translator.translate(i, lang_tgt=chosen_language)
    print(translate_text)
    finished_text.append(translate_text)
    

conn = sqlite3.connect('database.db')

cur = conn.cursor()

# Three " means docstring, so multi-line commands can be made
# cur.execute("""CREATE TABLE messages
#             (id real, username text, message text, translation text, time real)""")
# ^ Makes table (Delete after first use I think)

# cur.execute("INSERT INTO messages VALUES ('Matthew', 'Hello world!')")
# ^ Inserts into the table the stated values, in column order specified above
# for row in cur.execute("SELECT * FROM messages "):
#     print(row)

# conn.commit() # Saves changes
#
# conn.close() # Closes connection
