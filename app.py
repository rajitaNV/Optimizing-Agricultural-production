# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 18:41:53 2021

@author: Rajita
"""

from flask import Flask,render_template,request
import pickle
#import numpy as np
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')

standard_to = StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        n=int(request.form['Nitrogen'])
        p=int(request.form['Phosphorus'])
        k=int(request.form['Potassium'])
        t=float(request.form['temp'])
        h=float(request.form['humd'])
        ph=float(request.form['ph'])
        r=float(request.form['rain'])
        
        prediction=model.predict([[n,p,k,t,h,ph,r]])
        return render_template('index1.html', prediction_text='The Crop you can grow is : {}'.format(prediction)) 

    else:
        return render_template('index1.html')
    
if __name__=="__main__":
    app.run(debug=True)
