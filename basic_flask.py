from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/search/<searchterm>")
def search(searchterm):
    print(request.args.get('test', ''))
    return render_template('search.html', searchvar=searchterm)

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    return render_template('signin.html', name=request.form['name'])

if __name__ == "__main__":
    app.run()
