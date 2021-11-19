#!/usr/bin/python3

import pymysql

conn = pymysql.connect(host='localhost', 
                    user='admin', 
                    passwd='admin', 
                    db='moonpark')

with conn:
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM market")  #сам SQL код

    rows = cursor.fetchall() # Получаем данные.
    
    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))

    #conn.close() # Разрываем подключение. Но если тут закрыть, будет выбрасывать исключение: Already closed.

