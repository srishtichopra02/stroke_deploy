from flask import Flask, render_template, request
import pickle
import numpy as np


app=Flask("app")
loaded_model=pickle.load(open("Model.pkl","rb"))

@app.route("/")
def home():
    return render_template("html of app.html")

@app.route("/prediction", methods=["POST"])
def predict():
    glucose= request.form["glucose"]
    bmi= request.form["bmi"]
    age= request.form["age"]
    prediction = loaded_model.predict([[glucose,bmi,age]])[0]
    probability=loaded_model.predict_proba([[glucose,bmi,age]])
    probability=np.round((np.max(probability)*100),2)
    output=" "
    probability= f"{probability}%"


    if prediction==0:
        output="NOT A stroke"
    else:
        output="IT'S A STROKE"

    print(prediction,probability)
    return render_template("html of app.html", output_prediction=output,output_proba=probability)

if __name__=="__main__" :
    app.run(debug=True)
