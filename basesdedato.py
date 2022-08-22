import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor =conn.cursor()

rows = cursor.execute('select * from users where nombre="emma"')
for row in rows:
    print(row)


rows = cursor.execute('select * from users')
for row in rows:
    print(row)

cursor.close()
conn.close()

------------------------------
/usr/bin/python3.9 /home/emma/Escritorio/py/basesdedato.py 
(1, 'emma', 'albarran')
(1, 'emma', 'albarran')
(2, 'eugenio', 'soto')
(3, 'elsa', 'villasmil')
(4, 'demi', 'rincon')
(5, 'valeria', 'garcia')
(6, 'paola', 'garcia')
(7, 'jorge', 'albarran')
(8, 'eleana', 'villasmil')
