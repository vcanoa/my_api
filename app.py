import os
from flask import Flask, render_template, request, redirect ,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import validators,IntegerField,SubmitField
import numpy as np
from scipy.stats import lognorm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', 'testing')
Bootstrap(app)

from services.longevity_form import Ale_form

#here I import my fitted longevity model to be use for predict
import joblib
# Load the model from the file 
model_predict = joblib.load('model_predict_file.pkl')  

#here I am getting my index
@app.route('/',methods=['GET','POST'])
def index_m():
    if request.method == 'GET':
         return render_template('main.html')
    else:
        return redirect('/main_m')


#longevity form
@app.route('/aleform',methods=['GET','POST'])
def aleform():
    form=Ale_form()
    if request.method == "POST" and form.validate_on_submit():
        #obesity
        weight=float(form.weight.data)
        height=float(form.height.data)
        bmi=float(weight/height**2)
        #bmi distribution
        percentilbmi=lognorm.cdf([bmi], 0.1955,-10,25.71)
        #value in the obesity county distr
        val_obse = lognorm.ppf([percentilbmi], 0.0099,-449.9,474.25)
        #diabetes
        diabetes=float(form.diabetes.data)
        val_dia=lognorm.ppf([diabetes],0.164 ,-7.143 ,14.58)
        #smokers
        smoke=float(form.smoke.data)
        #number of cigarretes distribution
        percentilcigars=lognorm.cdf([smoke],0.506 ,0,2.29)
        #value in the smoker county distribution
        val_smoke = lognorm.ppf([percentilcigars],0.062 ,-65.19 ,88.55)
        #exercise
        exercise=float(form.exercise.data)
        val_exer=lognorm.ppf([exercise],0.105 ,-36.41 ,62.65)
        #hsdiploma 
        hsdiploma=float(form.hsdiploma.data)
        val_dip=lognorm.ppf([hsdiploma],0.208 ,-11.3 ,24.59)
        #poverty
        poverty=float(form.poverty.data)
        val_pov=lognorm.ppf([poverty],0.279 ,-3.594,15.76)
        out_person=[val_exer,val_obse,val_smoke,val_dia,val_pov,val_dip]
       # out_person=[35.41,39,42,17,33.7,35.4]   #lo mas bajo
        #out_person=[8,10,7.9,1.64,3.0,1.6]    #lo mas alto
        #out_person=[35,15,25.5,30.5,45.5,45.5]#example,building the web
        x_predict=np.array(out_person).reshape(1,-1)
        result=model_predict.predict(x_predict)
        result=str(result)
        #return result
        return render_template('predict_ale.html',result=result)
       # return redirect(url_for('predict_ale',out_person=out_person))
    return render_template('longevityform.html',title='LONGEVITY',form=form)


#here is information about the web page
@app.route('/about')
def about():
     return render_template('about.html')
 
#here I have my map_plots
@app.route('/longevity_m')
def func1_m():
    return render_template('ale_plot.html')

@app.route('/depresion_m')
def func2_m():
    return render_template('Major_Depression_plot.html')

@app.route('/obesity_m')
def func3_m():
    return render_template('obesity_plot.html')

@app.route('/diabetes_m')
def func10_m():
    return render_template('diabetes_plot.html')

@app.route('/noexer_m')
def func4_m():
    return render_template('no_exercise_plot.html')

@app.route('/no_hs_m')
def func5_m():
    return render_template('no_hs_diplo_plot.html')

@app.route('/poverty_m')
def func6_m():
    return render_template('poverty_plot.html')

@app.route('/unemployed_m')
def func7_m():
    return render_template('unemployed_plot.html')

@app.route('/uninsured_m')
def func8_m():
    return render_template('Uninsured_plot.html')

@app.route('/drug_m')
def func9_m():
    return render_template('Recent_Drug_Use_plot.html')

#   return html
          #   return render_template('end.html'), show(p)
     # else:
     #     return redirect('/next_m')


if __name__ == '__main__':
# app.run(port=33507)
 app.run(debug=True)
