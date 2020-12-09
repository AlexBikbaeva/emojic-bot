import sqlite3

def sqlite_database():
    try:
        conn = sqlite3.connect("emojic_database.db")
        cur = conn.cursor()
        print("Connected to SQLite")
        cur.executescript("\
                   PRAGMA foreign_keys=on;\
                   CREATE TABLE IF NOT EXISTS messages(\
                   mes_id INT PRIMARY KEY,\
                   mes_time,\
                   ses_id INT NOT NULL,\
                   mes_text TEXT,\
                   user_id INT NOT NULL,\
                   FOREIGN KEY (ses_id) REFERENCES sessions(ses_id));\
                    \
                   CREATE TABLE IF NOT EXISTS sessions(\
                   ses_id INT PRIMARY KEY,\
                   start_time,\
                   end_time)")
        conn.commit()
        print("Database made successfully \n")
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")

def database_insert(info):
    conn = sqlite3.connect("emojic_database.db")
    cur = conn.cursor()
    cur.executemany("INSERT INTO messages (mes_id, mes_time, ses_id, mes_text, user_id)\
                    VALUES (?,?,?,?,?)", (info)) #mess_id, mess_date.strftime("%H:%M:%S %d.%m.%Y"), ses_id, mess_text, user_id
    conn.commit()
    cur.close()

def database_insert_session(info):
    conn = sqlite3.connect("emojic_database.db")
    cur = conn.cursor()
    for item in info:
        cur.execute("INSERT INTO sessions (ses_id, start_time, end_time)\
                        VALUES (?,?,?)", (item)) #ses_id, start_time, end_time
    conn.commit()
    cur.close()