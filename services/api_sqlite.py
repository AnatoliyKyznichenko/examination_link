# import sqlite3
# import os
#
#
# class UserLink:
#     def __init__(self):
#         self.database = sqlite3.connect(os.path.join('data', 'database.db'))
#         self.cursor = self.database.cursor()
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(
#                             chat_id INTEGER
#         )''')
#         self.database.commit()
#
#
#     def get_id_user(self):
#         return self.cursor.execute("SELECT chat_id FROM user").fetchall()

