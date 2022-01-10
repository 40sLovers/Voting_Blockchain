from threading import current_thread
from flask import Flask,request,render_template, flash, jsonify,make_response
from flask_mail import Mail,Message
import socket,json,uuid,os
from src.Classes import *
from dotenv import load_dotenv
load_dotenv()
MAIL_USERNAME=os.getenv('MAIL_USERNAME')
MAIL_PASSWORD= os.getenv('MAIL_PASSWORD')
SERVER_TYPE=os.getenv('SERVER_TYPE')
WhiteList = []
EmailList = []
randTokens={}

app = Flask(__name__)
if SERVER_TYPE=="PRODUCTION":
    rootDomain = "http://40s.negro.systems"
else:
	rootDomain = "http://127.0.0.1:5000"

GVoteEntryStore = VoteEntryStore()
#Scuze Michelle te-am confundat cand am facut commit-ul :/

#Michelle e cea mai misto fata 

# Gia e net superioara pentru ca asculta IAN!!!

#Dupa ce terminam proiectul, votam!!!!

#Hahahah daca merge....

# :(((
    
#  cf?

# Hello hello

# Man im so lonely, despite i'm surrounded by people

# :')

#:"(
################################ configurare server smtp pentru trimitere emailuri
app.config.update( DEBUG=True, MAIL_SERVER='smtp.gmail.com',
                   MAIL_PORT=587, MAIL_USE_SSL=False, MAIL_USE_TLS=True, MAIL_USERNAME = MAIL_USERNAME,
                   MAIL_PASSWORD = MAIL_PASSWORD)
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
            # print(email)
            msg=Message("hi",sender=MAIL_USERNAME,recipients=[email,])
            msg.html=f"<div><p>Cineva a incercat sa creeze un cont pe adresa dumneavoastra de email, ati fost dumneavoastra?</p><a href=\"{rootDomain}/confirmare?token={randToken}\" type=\"button\" style=\"background-color: #007bff;border-color: #007bff;padding: .375rem .75rem;border-radius: .25rem;color: white;text-decoration: none;\">Confirma</a></div>"
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
    prv_key=keyFromHash(criptare)
    pub_key = prv_key.get_public_key()
    if CSVHelpers.isInCSVFile("database/Whitelist.csv",str(pub_key.W.x)) and \
    CSVHelpers.isInCSVFile("database/Whitelist.csv",str(pub_key.W.y)):
        resp = make_response(json.dumps("ok"))
        resp.set_cookie('privateKey', criptare )
        return resp
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
    succes=False
    if data != None:
        cod = data['cod']
        voteOption = data['selectedOption']
        CurrentPool = [p for p in IACoin.openedPools if p.poolId== cod]
        # print(CurrentPool)
        if(len(CurrentPool)!=0):
            CurrentPool=CurrentPool[0]
            privateKey= keyFromHash(request.cookies.get('privateKey'))
            succes=CurrentPool.Vote(privateKey,voteOption)
            # print(CurrentPool.pendingTransactions)
    return jsonify(succes = succes, cod=CurrentPool.poolId)

    
@app.route("/Votare", methods = ['POST'])
def yourVote():
    #asta e a buna acum
    data = request.get_json()
    succes=False
    if data != None:
        cod = data['cod']
        voteOption = data['selectedOption']
        CurrentPool = [p for p in IACoin.openedPools if p.poolId== cod]
        # print(CurrentPool)
        if(len(CurrentPool)!=0):
            CurrentPool=CurrentPool[0]
            privateKey= keyFromHash(request.cookies.get('privateKey'))
            pub_key = privateKey.get_public_key()
            if CSVHelpers.isInCSVFile("database/Whitelist.csv",str(pub_key.W.x)) and \
            CSVHelpers.isInCSVFile("database/Whitelist.csv",str(pub_key.W.y)):
                succes=CurrentPool.Vote(privateKey,voteOption)
            # print(CurrentPool.pendingTransactions)
    return jsonify(succes = succes, cod=CurrentPool.poolId)

@app.route("/newPoll", methods = ['POST'])
def codConectarePOST():
        try:
            data = request.get_json()
            # print(data)
            if data != None:
                    cod = uuid.uuid4().hex
                    listaOp = data['listaOp']
                    numePoll = data['numePoll']
                    poolCreator= request.cookies.get('privateKey')
                    poolOptions= {}
                    for option in listaOp:
                        poolOptions[option]=GenerateHelper.getRandomPublicKey(option,cod)
                    PoolVote= Pool(cod,poolOptions,IACoin,numePoll,poolCreator)
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
        pool_id=request.args.get("cod")
        entry=None
        # print(IACoin.openedPools[0].poolId,pool_id)
        CurrentPool = [p for p in IACoin.openedPools if p.poolId==pool_id]
        if(len(CurrentPool)!=0):
            entry = CurrentPool[0]
        # print("entry======",entry)
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
 
#pentru randomGenerari
# @app.route('/getPoolResults',methods =['GET'])
# def getPoolResults():
#     #http://127.0.0.1:5000/getPoolResults?pool_id=1234&order_by=nume --example
#     pool_id=request.args.get('pool_id')
#     order_by=request.args.get('order_by') #nume sau altceva
#     return GenerateHelper.getRandomOptions(order_by) #temporar, pana rezolvam cu poolurile

@app.route('/getPoolResults',methods =['GET'])
def getPoolResults():
    #http://127.0.0.1:5000/getPoolResults?pool_id=1234&order_by=nume --example
    pool_id=request.args.get('pool_id')
    CurrentPool = [p for p in IACoin.openedPools if p.poolId==pool_id]
    print(pool_id)
    if(len(CurrentPool)!=0):
        CurrentPool=CurrentPool[0]
        results= CurrentPool.getResults()
        return jsonify(results)
    return jsonify([])

if __name__=="__main__":
    app.run(debug=True)
