import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.connection = None
    def __enter__(self):
         return sqlite3.connect('data.db')
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()