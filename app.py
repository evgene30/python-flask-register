from flask import Flask, render_template, request
import pymysql.cursors

# Создаем экземпляр Flask App
app = Flask(__name__)


# Соединяемся с базой данных
con = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password='12345678',
                      db='expenses',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=["POST", "GET"])
@app.route('/home', methods=["POST", "GET"])
def index():
    # Проверяем использование метода отправки данных
    if request.method == "POST":
        cur = con.cursor()
        print(request.form)
        b = request.form['inputFamily'].strip()
        a = request.form['inputName'].strip()
        c = request.form['inputLastName'].strip()
        d = request.form['inputPhone'].strip()

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
        #con.close()
        # Выести страницу успешного запроса
        return render_template('Success!.html')





    q = request.args.get('q')
    if q:
        return render_template('search.html')
    else:
        return render_template('index.html')


@app.route('/about', methods=["POST", "GET"])
def about():
    q = request.args.get('q')
    if q:
        return render_template('search.html')

    else:
        return render_template('about.html')


@app.route('/search', methods=["POST", "GET"])
def search():
    return render_template('search.html')



if __name__ == "__main__":
    app.run(debug=True)
