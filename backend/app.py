from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('logare.html')


@app.route('/login', methods=['POST'])
def login2():
    registerData = request.get_json()
    registerData.adresa
    return "A mers"


if __name__=="__main__":
    app.run(debug=True)