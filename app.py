from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    q = request.args.get('q')
    if q:
        return render_template('search.html')

    else:
        return render_template('index.html')


@app.route('/about')
def about():
    q = request.args.get('q')
    if q:
        return render_template('search.html')

    else:
        return render_template('about.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)
