#another
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/")
def hello_world1():
    return "<h1>Hello, World!</h1>"

@app.route("/test")
def test():
    a=5+6
    return "this is my function" ,a

@app.route('/', methods =['GET','POST'])
def home_page():
    return render_tempate('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")

# another
from flask import Flask

app1 = Flask(__name__)

@app1.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app1.run(host="0.0.0.0")
