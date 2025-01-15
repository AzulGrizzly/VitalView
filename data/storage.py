import sqlite3


try:
  #connect to the DB
  conn = sqlite3.connect('vital_view.db')
  cursor = conn.cursor()

  #Create Users Table
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL, 
      password TEXT NOT NULL
    );
  ''')
  
  
  #Create Base Symptoms Table
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS symptoms (
      entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      symptom_name TEXT NOT NULL,
      symptom_description TEXT,
      datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
      severity INTEGER CHECK(severity >= 1 AND severity <= 10),
      FOREIGN KEY(user_id) REFERENCES users(user_id)
    );
   ''')

  # Commit the changes 
  conn.commit()
  print('tables updated successfully')
  
except Exception as e:
  print('An error occured:', e)

finally:
  #close connection
  conn.close()



