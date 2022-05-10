
from quicksurveycodeihop import quick_survey_ihop
from quicksurveycodemc import quick_survey_mcdonalds
from unicodedata import name
from urllib import request
from flask import Flask, render_template, request
from pydoc import cli
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib, ssl

#mcdonalds code 04016032205251812490002610
app = Flask(__name__)


@app.route("/") # directs to home page 
def home():        # defining function as home 
    return render_template('index.html') # on home page 'return' enter this 

@app.route("/sent", methods = ['POST'])
def sent():
    if request.method=='POST':
        company = request.form["company_name"]
        email = request.form["email_name"]
        survey_code = request.form["survey_name"]
        check_number = request.form["check#_name"]
        print(company)
        # if company == 'ihop' or 'Ihop' or 'IHOP':
        #     quick_survey_ihop(survey_code,check_number, email)
        #     return render_template("sent.html")
        # if company == "McDonald's":
        #     quick_survey_mcdonalds(survey_code, email)
        #     return render_template("sent.html")
        if company == "McDonald's":
            print('mcdonalds')
            quick_survey_mcdonalds(survey_code, email)
            
        elif company == 'IHOP':
            print('ihop')
            quick_survey_ihop(survey_code, check_number, email)
        return render_template("sent.html")



    


if __name__ == '__main__':
    app.debug = True
    app.run()