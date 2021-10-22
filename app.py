from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os
currentdirectory = os.path.dirname(os.path.abspath(__file__))



app = Flask("__name__")
model = pickle.load(open('random_forest_classifier_model.pkl', 'rb'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class CustomerDf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(120), unique=True, nullable=False)
    LastName = db.Column(db.String(120), unique=True, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Education = db.Column(db.String(120), unique=True, nullable=False)
    Age = db.Column(db.Integer, unique=True, nullable=False)
    SSN = db.Column(db.Integer, unique=True, nullable=False)
    PhoneNumber = db.Column(db.Integer, unique=True, nullable=False)
    Gender = db.Column(db.String(120), unique=True, nullable=False)
    MaritalStatus = db.Column(db.String(120), unique=True, nullable=False)
    CreditAmount = db.Column(db.Integer, unique=True, nullable=False)
    Rpay_Status_1 = db.Column(db.Integer, unique=True, nullable=False)
    Rpay_Status_2 = db.Column(db.Integer, unique=True, nullable=False)
    Rpay_Status_3 = db.Column(db.Integer, unique=True, nullable=False)
    Rpay_Status_4 = db.Column(db.Integer, unique=True, nullable=False)
    Rpay_Status_5 = db.Column(db.Integer, unique=True, nullable=False)
    Rpay_Status_6 = db.Column(db.Integer, unique=True, nullable=False)
    Statement_1 = db.Column(db.Integer, unique=True, nullable=False)
    Statement_2 = db.Column(db.Integer, unique=True, nullable=False)
    Statement_3 = db.Column(db.Integer, unique=True, nullable=False)
    Statement_4 = db.Column(db.Integer, unique=True, nullable=False)
    Statement_5 = db.Column(db.Integer, unique=True, nullable=False)
    Statement_6 = db.Column(db.Integer, unique=True, nullable=False)
    Payment_1 = db.Column(db.Integer, unique=True, nullable=False)
    Payment_2 = db.Column(db.Integer, unique=True, nullable=False)
    Payment_3 = db.Column(db.Integer, unique=True, nullable=False)
    Payment_4 = db.Column(db.Integer, unique=True, nullable=False)
    Payment_5 = db.Column(db.Integer, unique=True, nullable=False)
    Payment_6 = db.Column(db.Integer, unique=True, nullable=False) 
    Default_pay = db.Column(db.Integer, unique=True, nullable=False)
    Default_Status = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,FirstName,LastName,Email,Education,Age,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay,Default_Status):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Education = Education
        self.Age = Age
        self.SSN = SSN
        self.PhoneNumber = PhoneNumber
        self.Gender = Gender
        self.MaritalStatus = MaritalStatus
        self.CreditAmount = CreditAmount
        self.Rpay_Status_1 = Rpay_Status_1
        self.Rpay_Status_2 = Rpay_Status_2
        self.Rpay_Status_3 = Rpay_Status_3
        self.Rpay_Status_4 = Rpay_Status_4
        self.Rpay_Status_5 = Rpay_Status_5
        self.Rpay_Status_6 = Rpay_Status_6
        self.Statement_1 = Statement_1
        self.Statement_2 = Statement_2
        self.Statement_3 = Statement_3
        self.Statement_4 = Statement_4
        self.Statement_5 = Statement_5
        self.Statement_6 = Statement_6
        self.Payment_1 = Payment_1
        self.Payment_2 = Payment_2
        self.Payment_3 = Payment_3
        self.Payment_4 = Payment_4
        self.Payment_5 = Payment_5
        self.Payment_6 = Payment_6
        self.Default_pay = Default_pay
        self.Default_Status = Default_Status

        def __repr__(self):
            return 'User %r' % self.FirstName




@app.route('/',methods=['GET'])
def Home():
    return render_template('webpageupdated.html')
standard_to = StandardScaler()
@app.route("/", methods = ['GET','POST'])
def main():
    alert_message = False
    success_message = False
    try:
        if request.method == 'POST':

            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            Email = request.form['Email']
            Education = request.form['Education']
            if (Education == 'Graduate'):
                Education_Graduate = 1
                Education_University = 0
                Education_HighSchool = 0
                Education_Others = 0
            elif (Education == 'University'):
                Education_Graduate = 0
                Education_University = 1
                Education_HighSchool = 0
                Education_Others = 0
            elif (Education == 'Highschool'):
                Education_Graduate = 0
                Education_University = 0
                Education_HighSchool = 1
                Education_Others = 0
            else:
                Education_Graduate = 0
                Education_University = 0
                Education_HighSchool = 0
                Education_Others = 1

            Age = int(request.form['Age'])
            SSN = int(request.form['SSN'])
            PhoneNumber = int(request.form['PhoneNumber'])
            Gender = request.form['Gender']
            if (Gender == 'Male'):
                Gender_Male = 1
                Gender_Female =0
            else:
                Gender_Female = 1
                Gender_Male = 0
            MaritalStatus = request.form['MaritalStatus']
            if (MaritalStatus == 'Married'):
                MaritalStatus_Married = 1
                MaritalStatus_Single = 0
                MaritalStatus_Others = 0
            elif (MaritalStatus == 'Single'):
                MaritalStatus_Married = 0
                MaritalStatus_Single = 1
                MaritalStatus_Others = 0
            else:
                MaritalStatus_Married = 0
                MaritalStatus_Single = 0
                MaritalStatus_Others = 1
            CreditAmount = int(request.form['CreditAmount'])
            Rpay_Status_1 = int(request.form['Rpay_Status_1'])
            Rpay_Status_2 = int(request.form['Rpay_Status_2'])
            Rpay_Status_3 = int(request.form['Rpay_Status_3'])
            Rpay_Status_4 = int(request.form['Rpay_Status_4'])
            Rpay_Status_5 = int(request.form['Rpay_Status_5'])
            Rpay_Status_6 = int(request.form['Rpay_Status_6'])
            Statement_1 = int(request.form['Statement_1'])
            Statement_2 = int(request.form['Statement_2'])
            Statement_3 = int(request.form['Statement_3'])
            Statement_4 = int(request.form['Statement_4'])
            Statement_5 = int(request.form['Statement_5'])
            Statement_6 = int(request.form['Statement_6'])
            Payment_1 = int(request.form['Payment_1'])
            Payment_2 = int(request.form['Payment_2'])
            Payment_3 = int(request.form['Payment_3'])
            Payment_4 = int(request.form['Payment_4'])
            Payment_5 = int(request.form['Payment_5'])
            Payment_6 = int(request.form['Payment_6'])
            
            prediction=model.predict([[CreditAmount,Age,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Gender_Male,Gender_Female,Education_Graduate,Education_University,Education_HighSchool,Education_Others,MaritalStatus_Married,MaritalStatus_Single,MaritalStatus_Others]])
            if prediction[0] == 1:
                alert_message = "This account will be defaulted"
            else:
                success_message = "This account will not be defaulted"

            Default_pay = int(prediction[0])
            if Default_pay == 1:
                Default_Status = 'Defaulter'
            else:
                Default_Status = 'Non-Defaulter'
        
            entry = CustomerDf(FirstName,LastName,Email,Education,Age,SSN,PhoneNumber,Gender,MaritalStatus,CreditAmount,Rpay_Status_1,Rpay_Status_2,Rpay_Status_3,Rpay_Status_4,Rpay_Status_5,Rpay_Status_6,Statement_1,Statement_2,Statement_3,Statement_4,Statement_5,Statement_6,Payment_1,Payment_2,Payment_3,Payment_4,Payment_5,Payment_6,Default_pay,Default_Status)
            db.session.add(entry)
            db.session.commit()
    except:
        alert_message = "Please enter relevant information."
    return render_template('webpageupdated.html',alert_message = alert_message, success_message = success_message)
        

if __name__ == "__main__":
    app.run(debug=True)
