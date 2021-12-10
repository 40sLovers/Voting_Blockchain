from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('logare.html')


if __name__=="__main__":
    app.run(debug=True)