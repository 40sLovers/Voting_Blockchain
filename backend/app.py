from flask import Flask,request,render_template

WhiteList = []

app = Flask(__name__)
@app.route('/')
def login3():
    return render_template('logareC.html')


@app.route('/', methods=['POST'])
def login2():
    #registerData = request.get_json()
    criptare = request.json_get("criptare", None)
    email = request.json_get("adresa", None)
    numarMatricol = request.json_get("numarMatricol", None)
    cuvantCheie = request.json_get("cuvantCheie", None)
    WhiteList.append( criptare)
    return criptare

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
    else:
        return render_template("error404.html")

if __name__=="__main__":
    app.run(debug=True)