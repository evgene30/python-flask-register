import pymysql.cursors

con = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password='12345678',
                      db='expenses',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

init = int(input('Введите значение: 2 - сделать запись, 1 - просмотр базы: '))

if init == 1:
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM staff")

        rows = cur.fetchall()

        for row in rows:
            print(row)
    con.close()

elif init == 2:
    cur = con.cursor()
    b = str(input('Введите Фамилию: ')).strip()
    a = str(input('Введите Имя: ')).strip()
    c = str(input('Введите Отчество: ')).strip()
    d = str(input('Введите размер зарплаты: ')).strip()

    # Ввод значений полей в базу данных
    cur.execute(
        """INSERT INTO staff (Name, Family, FatherFamily, sum) 
        VALUES ('%(Name)s', '%(Family)s', '%(FatherFamily)s','%(sum)s')
        """ % {"Name": a, "Family": b, "FatherFamily": c, "sum": d}
    )

    # Сохранение внесенных изменений
    con.commit()

    # Просмотр измененных данных
    cur.execute("SELECT * FROM staff")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Вывод информации о изменениях
    base = "'expenses'".upper()
    print('\n''Изменения в базу ' + base + ' внесены!' + '\n')
    # Закрыть соединение
    con.close()

else:
    print('Соединение завершено')
    con.close()
