from flask import Flask,render_template,request
import pickle
model=pickle.load(open('concrete.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/predict',methods=["POST"])
def func2():
    cement=request.form['cement']
    slag=request.form['slag']
    ash=request.form['ash']
    water=request.form['water']
    plasticizer=request.form['plasticizer']
    coarse_aggregate=request.form['coarse_aggregate']
    fine_aggregate=request.form['fine_aggregate']
    age=request.form['age']
    data=[[float(cement),float(slag),float(ash),float(water),float(plasticizer),float(coarse_aggregate),float(fine_aggregate),int(age)]]
    pred=model.predict(data)
    print(pred)
    return render_template("index.html",y=str(pred))
   
if __name__=='__main__':

    app.run(debug= True)#wsgi local server url