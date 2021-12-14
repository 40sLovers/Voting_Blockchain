from flask import Flask,request,render_template, flash
from flask_mail import Mail,Message
import socket
import json
socket.getaddrinfo('127.0.0.1', 8080)
WhiteList = []


app = Flask(__name__)
app.config.update( DEBUG=True, MAIL_SERVER='smtp.gmail.com',
                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME = 'p1projectprogram@gmail.com',
                   MAIL_PASSWORD = "Project123")
mail=Mail(app)

@app.route('/')
def login3():
    return render_template('logareC.html')

@app.route("/inregistrare", methods=['POST','GET'])
def log():
    if request.method == 'POST':
        #registerData = request.json_get()
        #email = request.json_get("adresa", None)
        #numarMatricol = request.json_get("numarMatricol", None)
        #cuvantCheie = request.json_get("cuvantCheie", None)
        #WhiteList.append( criptare)
        data = request.get_json()
        email=data['adresa']
        numarMatricol=data['numarMatricol']
        print(data)
        msg=Message("hi",sender="p1projectprogram@gmail.com",recipients=[email,])
        msg.body="buna ce mai faci Onisim<3?"
        mail.send(msg)
        return json.dumps("ok")
    else: 
        return render_template("inregistrare.html")

@app.route('/<name>')
def login(name):
    if(name=="inregistrare"):
        return render_template('inregistrare.html')
    elif name=='Despre':
        return render_template('Despre.html')
    elif name=='confirmare':
        return render_template("confirmare.html")
    elif name=='index':
        return render_template("index.html")
    elif name=='rezultate':
        return render_template("rezultate.html")
    elif name=='votPoll':
        return render_template("votPoll.html")
    elif name=='newPoll':
        return render_template("newPoll.html")
    else:
        return render_template("error404.html")

if __name__=="__main__":
    app.run(debug=True)