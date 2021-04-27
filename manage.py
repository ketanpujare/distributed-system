from typing import Collection
from flask import Flask, render_template, request
from db   import get_connection

app = Flask(__name__, template_folder='templates')

mongo = get_connection()
db = mongo['webdata']['weblink']

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def post_link():
    weblink =  request.form['link']
    db.insert({'link':str(weblink)})
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)