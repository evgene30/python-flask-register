from flask import Flask, render_template, request
import pymysql.cursors

# Создаем экземпляр Flask App
app = Flask(__name__)

# Соединяемся с базой данных
con = pymysql.connect(host='127.0.0.1',
                      user='root',
                      password='12345678',
                      db='kontakt',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=["POST", "GET"])
@app.route('/home', methods=["POST", "GET"])
def index():
    # Проверяем использование метода отправки данных
    if request.method == "POST":
        cur = con.cursor()

        b = request.form['inputFamily'].strip()
        a = request.form['inputName'].strip()
        c = request.form['inputLastName'].strip()
        d = request.form['inputPhone'].strip()
        e = request.form['inputDateBirthsday'].strip()
        f = request.form['inputShool'].strip()
        g = request.form['inputNumberShool'].strip()
        h = request.form['inputClass'].strip()
        j = request.form['inputCity'].strip()
        k = request.form['inputRaion'].strip()
        l = request.form['inputTupeStreet'].strip()
        m = request.form['imputNameStreet'].strip()
        u = request.form['inputHome'].strip()
        r = request.form['inputCorpus'].strip()
        mr = request.form['inputRoom'].strip()


        # Ввод значений полей в базу данных
        cur.execute(
            """INSERT INTO user_kontakt (inputFamily, inputName, inputLastName, inputPhone, inputDateBirthsday, inputShool, inputNumberShool, inputClass, inputCity, inputRaion, inputTupeStreet, imputNameStreet, inputHome, inputCorpus, inputRoom) 
            VALUES ('%(inputFamily)s', '%(inputName)s', '%(inputLastName)s', '%(inputPhone)s', '%(inputDateBirthsday)s', '%(inputShool)s','%(inputNumberShool)s', '%(inputClass)s', '%(inputCity)s', '%(inputRaion)s', '%(inputTupeStreet)s','%(imputNameStreet)s','%(inputHome)s','%(inputCorpus)s', '%(inputRoom)s')"""
                % {"inputFamily": a, "inputName": b, "inputLastName": c, "inputPhone": d, "inputDateBirthsday": e,
                   "inputShool": f, "inputNumberShool": g, "inputClass": h, "inputCity": j, "inputRaion": k,
                   "inputTupeStreet": l, "imputNameStreet": m, "inputHome": u, "inputCorpus": r, "inputRoom": mr}
        )
        # Сохранение внесенных изменений
        con.commit()

        # Просмотр измененных данных
        cur.execute("SELECT * FROM user_kontakt")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # Вывод информации о изменениях
        base = "'user_kontakt'".upper()
        print('\n''Изменения в базу ' + base + ' внесены!' + '\n')
        # Закрыть соединение
        # con.close()
        # Выести страницу успешного запроса
        return render_template('Success!.html')
    else:
        return render_template('index.html')

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
