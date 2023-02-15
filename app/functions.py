import mysql.connector

dbhost = "localhost" # os.getenv('dbhost')
dbuser = "root"# os.getenv('dbuser')
dbpass = ""# os.getenv('dbpass')
dbname = "hadada"# os.getenv('dbname')

def db(sql, query='select', data=None):
    conn = mysql.connector.connect(host=dbhost,user=dbuser,port=3306, password=dbpass,database=dbname)
    cursor = conn.cursor(dictionary=True,buffered=True)
    ret = []
    # sql = conn.converter.escape(sql)
    if query == 'insert':
        cursor.execute(sql,data)
    else:
        cursor.execute(sql)
    if query == 'select':
        ret = cursor.fetchone()
    elif query == 'many':
        ret = cursor.fetchall()
    elif query == 'insert':
        ret = cursor.lastrowid
        conn.commit()
    elif query == 'update':
        conn.commit()
        ret = True
    cursor.close()
    return ret