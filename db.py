import pymysql
import pymysql.cursors

con = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password='12345678',
                      db='expenses',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

init = int(input('Введите значение: 1 - сделать запись, 2 - просмотр: '))
if init == 2:
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM staff")

        rows = cur.fetchall()

        for row in rows:
            print(row)
    con.close()
elif init == 1:
    cur = con.cursor()
    b = str(input('Введите Фамилию: '))
    a = str(input('Введите Имя: '))
    c = str(input('Введите Отчество: '))
    d = str(input('Введите размер зарплаты: '))

    # Ввод значений полей в базу данных
    cur.execute(
        """INSERT INTO staff (Name, Family, FatherFamily, sum) 
         VALUES ('%(Name)s', '%(Family)s', '%(FatherFamily)s','%(sum)s')
         """ % {"Name": a, "Family": b, "FatherFamily": c, "sum": d}
    )
    # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
    con.commit()
    # Вывод информации о изменениях
    base = "'expenses'".upper()
    print('\n''Изменения в базу ' + base + ' внесены!' + '\n')
    # Просмотр измененных данных
    cur.execute("SELECT * FROM staff")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    con.close()

else:
    print('Соединение завершено')
    con.close()
