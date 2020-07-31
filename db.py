import pymysql.cursors

con = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password='12345678',
                      db='expenses',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()
b = str(input('Введите число: ')).strip()
a = str(input('Введите главный номер: ')).strip()
c = str(input('Введите годовую зарплату: ')).strip()
d = str(input('Введите размер зарплаты: ')).strip()
e = str(input('Введите размер имя: ')).strip()

    # Ввод значений полей в базу данных
cur.execute(
        """INSERT INTO receivers3 (num, receiver, value, comment, name) 
        VALUES ('%(num)s', '%(receiver)s', '%(value)s', '%(comment)s', '%(name)s')
        """ % {"num": a, "receiver": b, "value": c, "comment": d, "name": e}
    )

    # Сохранение внесенных изменений
con.commit()

    # Просмотр измененных данных
cur.execute("SELECT * FROM receivers3")
rows = cur.fetchall()
for row in rows:
    print(row)

    # Вывод информации о изменениях
base = "'receivers3'".upper()
print('\n''Изменения в базу ' + base + ' внесены!' + '\n')
    # Закрыть соединение
con.close()
