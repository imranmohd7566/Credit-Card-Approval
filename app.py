# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 18:50:00 2022

@author: home
"""

from flask import Flask, render_template, request
import requests
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('Credit_Approval_RF_model_Smote.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['Gender']
        if(gender=='Male'):
            gender=1
        else:
            gender = 0
            
        car = request.form['Car']
        if(car=='Yes'):
            car=1
        else:
            car = 0
            
        realty = request.form['Realty']
        if(realty=='Yes'):
            realty=1
        else:
            realty = 0
            
        children = float(request.form['Children'])
        
        income=float(request.form['Income'])
        
        income_type = request.form['Income_type']
        if(income_type=='Pensioner'):
            income_type=1
        elif (income_type=='State servant'):
            income_type = 2
        elif (income_type=='Student'):
            income_type = 3
        elif (income_type=='Working'):
            income_type = 4
        else:
            income_type = 0
        
        education = request.form['Education']
        if(education=='Higher education'):
            education=1
        elif (education=='Incomplete higher'):
            education = 2
        elif (education=='Lower secondary'):
            education = 3
        elif (education=='Secondary / secondary special'):
            education = 4
        else:
            education = 0
        
        family_status = request.form['Family_Status']
        if(family_status=='Married'):
            family_status=1
        elif (family_status=='Separated'):
            family_status = 2
        elif (family_status=='Single / not married'):
            family_status = 3
        elif (family_status=='Widow'):
            family_status = 4
        else:
            family_status = 0
            
        housing = request.form['Housing']
        if(housing=='House / apartment'):
            housing=1
        elif (housing=='Municipal apartment'):
            housing = 2
        elif (housing=='Office apartment'):
            housing = 3
        elif (housing=='Rented apartment'):
            housing = 4
        elif (housing=='With parents'):
            housing = 5
        else:
            housing = 0
        
        mobile = request.form['Mobile']
        if(mobile=='Yes'):
            mobile=1
        else: mobile=0
        work_phone = request.form['Work_phone']
        if(work_phone=='Yes'):
            work_phone=1
        else: work_phone=0
        phone = request.form['Phone']
        if(phone=='Yes'):
            phone=1
        else: phone=0
        email = request.form['Email']
        if(email=='Yes'):
            email=1
        else: email=0
        
        occupation = request.form['Occupation']
        if(occupation=='Cleaning staff'): occupation=1
        elif (occupation=='Cooking staff'): occupation = 2
        elif (occupation=='Core staff'): occupation = 3
        elif (occupation=='Drivers'): occupation = 4
        elif (occupation=='HR staff'): occupation = 5
        elif (occupation=='High skill tech staff'): occupation = 6
        elif (occupation=='IT staff'): occupation = 7
        elif (occupation=='Laborers'): occupation = 8
        elif (occupation=='Low-skill Laborers'): occupation = 9
        elif (occupation=='Managers'): occupation = 10
        elif (occupation=='Medicine staff'): occupation = 11
        elif (occupation=='Private service staff'): occupation = 12
        elif (occupation=='Realty agents'): occupation = 13
        elif (occupation=='Sales staff'): occupation = 14
        elif (occupation=='Secretaries'): occupation = 15
        elif (occupation=='Security staff'): occupation = 16
        elif (occupation=='Waiters/barmen staff'): occupation = 17
        else: occupation = 0
        
        family_members=float(request.form['Family_members'])
        age=float(request.form['Age'])
        years_employed=float(request.form['Years_employed'])
        
        prediction=model.predict([[gender,car, realty, children, income, income_type, education, family_status, housing, mobile, work_phone, phone, email, occupation, family_members, age, years_employed]])
        output=prediction[0]
        if output == 1:
            return render_template('index.html',prediction_text="Your credit card can be approved.")

        else:
            return render_template('index.html',prediction_texts="Sorry, we cant issue you credit card at this time.")
    else:
        return render_template('index.html')

if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    #app.run(debug = True)