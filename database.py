import sqlite3
CREATE_EQUIPMENTS = '''CREATE TABLE IF NOT EXISTS equipments (
    id INTEGER PRIMARY KEY,
    is_mred BOOLEAN DEFAULT FALSE,
    name VARCHAR(60) NOT NULL,
    category VARCHAR(60) NOT NULL
    )'''

def select(command, *args):
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    return cursor.execute(command, args).fetchall()

def get_items(is_all, mred, category=None):
    if is_all:
        if mred == 'all':
            command = '''SELECT * FROM equipments ORDER BY name'''
        elif mred == 'MR\'ed':
            command = '''SELECT * FROM equipments WHERE is_mred=TRUE ORDER BY name'''
        else:
            command = '''SELECT * FROM equipments WHERE is_mred=FALSE ORDER BY name'''
        return select(command)
    else:
        if mred == 'all':
            command = '''SELECT * FROM equipments WHERE category=? ORDER BY name'''
        elif mred == 'MR\'ed':
            command = '''SELECT * FROM equipments WHERE is_mred=TRUE AND category=? is_mred=TRUE ORDER BY name'''
        else:
            command = '''SELECT * FROM equipments WHERE is_mred=FALSE AND category=? ORDER BY name'''
        return select(command,category)


def insertItem(name, category):
    command = '''INSERT INTO equipments(name, category) VALUES(?,?)'''
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(command, (name,category))
    conn.commit()

def update_mred(item):
    command = '''UPDATE equipments SET is_mred=? WHERE id=?'''
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(command, item)
    conn.commit()


def start():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(CREATE_EQUIPMENTS)
    conn.commit()


