from flask import Flask,request,render_template, flash
from flask_mail import Mail,Message
import socket
import json
from Blockchain_ready_Gandolh import Blockchain,Block,Transaction
from GoodToUseScripts import *
WhiteList = []
EmailList = []
CoduriList = []
ListaOp = []
app = Flask(__name__)

################################ configurare server smtp pentru trimitere emailuri
app.config.update( DEBUG=True, MAIL_SERVER='smtp.gmail.com',
                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME = 'p1projectprogram@gmail.com',
                   MAIL_PASSWORD = "Project123")
mail=Mail(app)

################################ initializare blockchain
#
IACoin = Blockchain()
initializareLantDeBlocuri(IACoin)


################################ routes
@app.route('/')
def login3():
    return render_template('index.html')

@app.route("/inregistrare", methods=['POST','GET'])
def log():
    if request.method == 'POST':
        data = request.get_json()
        email = data['adresa']
        criptare = data['criptare']
        emailCriptat = data['adresaCriptata']
        WhiteList.append( criptare )
        if emailCriptat not in EmailList:
            EmailList.append( emailCriptat ) 
            print(data)
            msg=Message("hi",sender="p1projectprogram@gmail.com",recipients=[email,])
            msg.html="<a style=\"background-color: #2d6cdf;color: white;padding: 10px;border-radius: 20px;\" href= windows.location.protocol + \"//\"+ windows.location.href +\"/confirmare?email={email}\"> Apasa-ma</a>"
            mail.send(msg)
            return json.dumps("ok")
        else:
            return json.dumps("EmailFolosit")    
    else: 
        return render_template("inregistrare.html")
  
@app.route("/",methods=['POST', 'GET'])
def autentificare():
    data = request.get_json()
    criptare = data['criptare']
    if criptare in WhiteList:
        return json.dumps("ok")
    else:
        return json.dumps("notok")

@app.route("/newPoll", methods = ['GET'])

def codConectare():
    return render_template("newPoll.html")

@app.route("/newPoll", methods = ['POST'])

def codConectarePOST():
    data = request.get_json()
    if data != None:
        cod = data['cod']
        listaOp = data['listaOp']
        numePoll = data['numePoll']
        CoduriList.append(cod)
        return json.dumps("{\"succes\": true}")
    return json.dumps("{\"succes\": false}")

@app.route("/newPollVerificare", methods = ['POST', 'GET'])

def verificaCod():
    data = request.get_json()
    if data != None:
        CodConectare = data['CodConectare']
        if CodConectare in CoduriList:
                return json.dumps("ok")
    return render_template("newPoll.html")


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
    elif name=='Votare':
        return render_template("Votare.html")
    elif name=='newPoll':
        return render_template("newPoll.html")
    elif name=='verificaEmail':
        return render_template("verificaEmail.html")
    elif name == 'confirmarevot':
        return render_template("confirmarevot.html")
    else:
        return render_template("error404.html")

if __name__=="__main__":
    app.run(debug=True)
