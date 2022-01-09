from flask import Flask,request,render_template, flash, jsonify,make_response
from flask_mail import Mail,Message
import socket,json,uuid
from src.Classes import *

WhiteList = []
EmailList = []
randTokens={}

app = Flask(__name__)
rootDomain= "http://127.0.0.1:5000/"

GVoteEntryStore = VoteEntryStore()
#Michelle e cea mai misto fata 

# Gia e net superioara pentru ca asculta IAN!!!

#Dupa ce terminam proiectul, votam!!!!

#Hahahah daca merge....

# :(((
    
#  cf?

# Hello hello

################################ configurare server smtp pentru trimitere emailuri
app.config.update( DEBUG=True, MAIL_SERVER='smtp.gmail.com',
                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME = 'proiectvoteboat@gmail.com',
                   MAIL_PASSWORD = "Celmaimistosite0")
mail=Mail(app)
 
################################ initializare blockchain
#
IACoin = Blockchain()
BlockchainHelpers.initializareLantDeBlocuri(IACoin)

################################ routes
@app.route('/')
def login3():
    return render_template('index.html')
 
@app.route("/inregistrare", methods=['POST','GET'])
def log():
    if request.method == 'POST':
        data = request.get_json()
        privateKey=data['cheiePrivata']
        emailCriptat=data['adresaCriptata']
        email= data['email']
        randToken=  uuid.uuid4().hex
        #Emailist va fi un csv
        if not CSVHelpers.isInCSVFile('database/EmailList.csv',emailCriptat):
            print(email)
            msg=Message("hi",sender="proiectvoteboat@gmail.com",recipients=[email,])
            msg.html=f"<div><p>Cineva a incercat sa creeze un cont pe adresa dumneavoastra de email, ati fost dumneavoastra?</p><a href=\"http://127.0.0.1:5000/confirmare?token={randToken}\" type=\"button\" style=\"background-color: #007bff;border-color: #007bff;padding: .375rem .75rem;border-radius: .25rem;color: white;text-decoration: none;\">Confirma</a></div>"
            mail.send(msg)
            randTokens[randToken]={
                'email':data['adresaCriptata'],
                'privateKey':privateKey
            }
            resp = make_response(json.dumps("ok"))
            resp.set_cookie('randToken',randToken)
            return resp
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
 
@app.route("/doVote", methods = ['GET'])
def votareGET2():
    cod = request.args.get('cod')
    entry=None
    CurrentPool = [p for p in IACoin.openedPools if p.poolId== cod]
    if(len(CurrentPool)!=0):
        entry = CurrentPool[0]
    return render_template("Votare.html", entry=entry)
 
@app.route("/doVote", methods = ['POST'])
def votareGET():
    data = request.get_json()
    if data != None:
        cod = data['cod']
        voteOption = data['voteOption']
        entry = GVoteEntryStore.GetVoteEntry(cod)
        if entry != None:
            result = entry.bHasVoted
            if result == False:
                entry.bHasVoted = True
                entry.voteOption = voteOption
            return jsonify(
                    succes = result == False
                   )
    return jsonify(
            succes = False,
            )
    
@app.route("/Votare", methods = ['POST'])
def yourVote():
    data = request.get_json()
    if data != None:
        VotedOption = data['selectedOption']
        cod = data['cod']
        #CurrentPool.Vote(codConectare, privatKey, VotedOption) #privatekey trebuie generat
        return jsonify(
            succes = True,
            cod = cod
        )
    return jsonify(
        succes = False
    )

@app.route("/newPoll", methods = ['POST'])
def codConectarePOST():
        try:
            data = request.get_json()
            print(data)
            if data != None:
                    cod = uuid.uuid4().hex
                    listaOp = data['listaOp']
                    numePoll = data['numePoll']
                    poolOptions= {}
                    for option in listaOp:
                        poolOptions[option]=GenerateHelper.getRandomPublicKey(option,cod)
                    PoolVote= Pool(cod,poolOptions,IACoin,numePoll)
                    return jsonify(
                        succes = True,
                        cod = cod,
                       # CoduriList = CoduriList
                    )
            return jsonify(
                    succes = False,
                )
        except Exception as e:
            return str(e)
 
@app.route("/newPollVerificare", methods = ['POST', 'GET'])
 
def verificaCod():
    data = request.get_json()
    if data != None:
        CodConectare = data['CodConectare']
        CurrentPool = [p for p in IACoin.openedPools if p.poolId== CodConectare]
        #CurrentPool.Vote(codConectare,privateKey, VotedOption) privatekey trebuie generat
        if(len(CurrentPool)!=0):
                return jsonify(
                    succes = True,
                    cod = CodConectare
                )
        return jsonify(
                succes = False,
            )
    return render_template("newPoll.html")
 
 
@app.route('/<name>')
def login(name):
    if(name=="inregistrare"):
        return render_template('inregistrare.html')
    elif name=='Despre':
        return render_template('Despre.html')
    elif name=='confirmare':
        randToken=request.cookies.get('randToken')
        email=randTokens[randToken]['email']
        privateKeyHex=randTokens[randToken]['privateKey']
        privateKey= keyFromHash( privateKeyHex)
        SaveHelper.saveEmailList("database/EmailList.csv",email)
        SaveHelper.saveWhitelist("database/Whitelist.csv",privateKey.get_public_key())
        resp = make_response(render_template("confirmare.html"))
        resp.set_cookie('privateKey', privateKeyHex )
        return resp
    elif name=='index':
        return render_template("index.html")
    elif name=='rezultate':
        pool_id=request.args.get("pool_id")
        entry=None
        #CurrentPool = [p for p in IACoin.openedPools if p.poolId==pool_id]
        #if(len(CurrentPool)!=0):
            #entry = CurrentPool[0]
        entry=Pool("-", {}, IACoin, "Pool Title")
        return render_template("rezultate.html", entry=entry)
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
 

@app.route('/getPoolResults',methods =['GET'])
def getPoolResults():
    #http://127.0.0.1:5000/getPoolResults?pool_id=1234&order_by=nume --example
    pool_id=request.args.get('pool_id')
    order_by=request.args.get('order_by') #nume sau altceva
    return GenerateHelper.getRandomOptions(order_by) #temporar, pana rezolvam cu poolurile


if __name__=="__main__":
    app.run(debug=True)
