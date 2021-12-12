from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')
def login3():
    return render_template('logare.html')


@app.route('/', methods=['POST'])
def login2():
    registerData = request.get_json()
    return registerData

@app.route('/<name>')
def login(name):
    if(name=="inregistrare"):
             return render_template('inregistrare.html')
    elif name=='detalii':
        return render_template('detalii.html')
    elif name=='confirmare':
        return render_template("confirmare.html")
    elif name=='index':
        return render_template("index.html")
    elif name=='rezultate':
        return render_template("rezultate.html")
    return render_template("error404.html")

if __name__=="__main__":
    app.run(debug=True)