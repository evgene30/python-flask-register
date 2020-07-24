from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def index():
    q = request.args.get('q')
    if q:
        return render_template('search.html')
    else:
        return render_template('index.html')


@app.route('/about', methods=['POST', 'GET'])
def about():
    q = request.args.get('q')
    if q:
        return render_template('search.html')

    else:
        return render_template('about.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)
