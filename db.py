import sqlite3

class BotDB:


    def __init__(self, db_file):
        self.conn=sqlite3.connect(db_file)
        self.cursor=self.conn.cursor()


    def user_exists(self, user_id):
        """ Is there a user in base? """
        result=self.cursor.execute("SELECT * FROM `users` WHERE `user_id`=?", (user_id,)).fetchmany(1)
        return bool(len(result))


    def add_user(self, user_id):
        """ Add user to base """
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()


    def set_active(self, user_id, active):
        """ Update user's status """
        self.cursor.execute("UPDATE 'users' SET active=? WHERE user_id=?", (active, user_id,))
        return self.conn.commit()


    def get_users(self):
        """ Getting users and activities """
        result=self.cursor.execute("SELECT user_id, active FROM `users`").fetchall()
        return result


    def all_users(self):
        """ Getting all users"""
        result=self.cursor.execute("SELECT * FROM `users`").fetchall()
        return len(result)


    def all_active(self):
        """ Getting all active users """
        result=self.cursor.execute("SELECT * FROM `users` WHERE active=?", (1,)).fetchall()
        return len(result)


    def close(self):
        """ Close connection to DB """
        self.connection.close()