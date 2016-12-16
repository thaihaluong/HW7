from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("w3_About me.html")
@app.route('/zai')
def man():
    return render_template("w3_Manly Actors.html")

if __name__ == '__main__':
    app.run()
