from flask import Flask,request,render_template
from flask_mail import Mail,Message

WhiteList = []


app = Flask(__name__)
mail=Mail(app)
app.config["MAIL_SERVER"]="smpt.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]="p1projectprogram@gmail.com"
app.config["MAIL_PASSWORD"]="Project123"
app.config['MAIL_USE_SSL'] = True



mail=Mail(app)
@app.route('/')
def login3():
    return render_template('inregistrare.html')


@app.route('/', methods=['POST'])
def login2():
    #registerData = request.get_json()
    validareemail=request.json_get("validareemail",None)
    criptare = request.json_get("criptare", None)
    email = request.json_get("adresa", None)
    numarMatricol = request.json_get("numarMatricol", None)
    cuvantCheie = request.json_get("cuvantCheie", None)
    WhiteList.append( criptare)
    return criptare
@app.route("/inregistrare", methods=['POST','GET'])
def log():
   validareemail=request.json_get("validareemail",None)
   if request.method == 'POST' and validareemail==True:
     email = request.json_get("adresa", None)
     msg=Message(request.form.get("hi"),sender="p1project@gmail.com",recipients=email)
     msg.body="buna ce mai faci Onisim<3?"
     mail.send(msg)
     return render_template("confirmare.html")

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