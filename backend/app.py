from flask import Flask,request,render_template, flash
from flask_mail import Mail,Message
import socket
import json
from Blockchain_ready_Gandolh import Blockchain,Block,Transaction
from GoodToUseScripts import keyFromHash,updatehash
WhiteList = []
EmailList = []

app = Flask(__name__)
app.config.update( DEBUG=True, MAIL_SERVER='smtp.gmail.com',
                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME = 'p1projectprogram@gmail.com',
                   MAIL_PASSWORD = "Project123")
mail=Mail(app)
IACoin = Blockchain()



@app.route('/')
def login3():
    return render_template('logareC.html')

@app.route("/inregistrare", methods=['POST','GET'])
def log():
    if request.method == 'POST':
        data = request.get_json()
        email = data['adresa']
        numarMatricol = data['numarMatricol']
        cuvantCheie = data['cuvantCheie']
        criptare = data['criptare']
        WhiteList.append( criptare )
        EmailList.append( email ) #criptez email in plus
        print(data)
        msg=Message("hi",sender="p1projectprogram@gmail.com",recipients=[email,])
        msg.html="<a style=\"background-color: #2d6cdf;color: white;padding: 10px;border-radius: 20px;\" href= windows.location.protocol + \"//\"+ windows.location.href +\"/confirmare?email={email}\"> Apasa-ma</a>"
        mail.send(msg)
        return json.dumps("ok")
    else: 
        return render_template("inregistrare.html")
  
@app.route("/",methods=['POST','GET'])
def autentificare():
    if request.method == 'POST':
        data = request.get_json()
        email = data['adresa']
        numarMatricol = data['numarMatricol']
        cuvantCheie = data['cuvantCheie']
        criptare = data['criptare']
        if criptare in WhiteList:
            return json.dumps("ok")
    #else:
        #return render_template("logareC.html")

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
    elif name=='verificaEmail':
        return render_template("verificaEmail.html")
    else:
        return render_template("error404.html")

if __name__=="__main__":
    app.run(debug=True)