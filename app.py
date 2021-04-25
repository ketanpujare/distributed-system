from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/post_link', methods=['POST'])
def post_link():
    weblink =  request.form['link']
    print(weblink)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)