from flask import Flask, render_template

app = Flask(__name__)


# Основная страница сайта-визитки
@app.route('/')
def index():
    return render_template('index.html')


# Страница с предыдущем опытом работы
@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
