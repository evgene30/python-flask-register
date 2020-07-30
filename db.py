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
    con.close(CREATE TABLE `user_kontakt` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`inputFamily` CHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`inputName` CHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`inputLastName` CHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`inputPhone` INT(9) UNSIGNED ZEROFILL NOT NULL,
	`inputDateBirthsday` DATE NULL DEFAULT NULL,
	`inputShool` CHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`inputNumberShool` INT(10) UNSIGNED NOT NULL,
	`inputClass` CHAR(8) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`inputCity` CHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8_general_ci',
	`inputRaion` CHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`inputTupeStreet` CHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`imputNameStreet` CHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`inputHome` INT(10) NULL DEFAULT NULL,
	`inputCorpus` INT(10) NOT NULL,
	`inputRoom` INT(10) NOT NULL,
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=8
;)

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
