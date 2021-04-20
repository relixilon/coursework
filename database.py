import mysql.connector , datetime

class Database():
  def __init__(self):
    self.config = {
      'user': 'mario',
      'password': 'mario',
      'host': '127.0.0.1',
      'database': 'travel', 
      'raise_on_warnings': True
    }

x = Database()

print(x.config)
