from flask import Flask,render_template,request,flash,redirect,url_for
from database import validUser,addUser,addLink,getLongLink
import random
from hashids import Hashids
app=Flask(__name__)
app.config['SECRET_KEY'] = 'Amir Secret key'

@app.route("/", methods=['GET','POST'])
def signUp():
    if request.method=='GET':
        return render_template('signUp.html')
    elif request.method=="POST":
        name=request.form['Name']
        email=request.form['Email']
        password=request.form['Password']
        if((name!="") and (email !="") and (password !="")):
            addUser(name,email,password)
            return redirect(url_for('home'))
        else:
            return render_template('signUp.html')

@app.route("/signIn",methods=['GET','POST'])
def signIn():
    if request.method=='GET':
        return render_template("sign in.html")
    else:
        email=request.form['SignInEmail']
        password=request.form['SignInPassword']
        ifExist=validUser(email,password)
        if(ifExist):
            return redirect(url_for('home'))
        else:
            flash("You Don't Have an Acount Please Sign Up!!!!")
            return render_template('sign in.html')


@app.route("/home",methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template("home.html")
    else:
        longLink=request.form['homeLongLink']
        num1 = random.randint(0,10000)
        hashids = Hashids(longLink,5)
        shortLink= hashids.encode(num1)
        addLink(longLink,shortLink)
        return render_template('home.html',short=f'http://127.0.0.1:5000/home/{shortLink}')


@app.route("/home/<string:shortLink>")
def getLong(shortLink):
    print(shortLink)
    long=getLongLink(shortLink)
    return redirect(long)

 

