from flask import Flask, render_template, request
from model.modellstm import sepsis
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("/index.html")

@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method=="POST":
        hr= request.form["hr"]
        o2sat=request.form["o2sat"]
        temp=request.form["temp"]
        sbp=request.form["sbp"]
        map1=request.form["map1"]
        resp=request.form["resp"]
        gender=request.form["gender"]
        age=request.form["age"]
        hospadmtime=request.form["hospadmtime"]
        iculos=request.form["iculos"]
        #arr=np.array([[hr,o2sat,temp,sbp,map1,resp,gender,age,hospadmtime,iculos]])
        pred=sepsis(hr,o2sat,temp,sbp,map1,resp,gender,age,hospadmtime,iculos)
        print(hr,o2sat,temp,sbp,map1,resp,gender,age,hospadmtime,iculos)
        print(pred)
    return render_template("/inner-page.html",data=pred)
    #return render_template("/inner-page.html",data=0)
"""
@app.route('/nw')
def nw():
    return render_template("/index.html")

@app.route('/nw1')
def nw1():
    return render_template("/inner-page.html")
"""

if __name__=='__main__' :
    app.run(debug=True)
