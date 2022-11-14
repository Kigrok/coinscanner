import sqlite3

# Create database's file
def create_db():
	db = open('users.db', 'w+')
	db.close()

# Create table 'Users' in database
def create_users():
	with sqlite3.connect('users.db') as db:
		cursor = db.cursor()
		query = """ 
CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,\
user_id INTEGER NOT NULL UNIQUE,\
active INTEGER NOT NULL DEFAULT (1),\
join_date DATETIME NOT NULL DEFAULT ( (DATETIME('now')))); """
		cursor.execute(query)
	cursor.connection.close()

def main():
	create_db()
	create_users()

if __name__ == '__main__':
	main()