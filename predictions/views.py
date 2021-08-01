from django.shortcuts import render
from .forms import PredictForm
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import joblib
import numpy as np
import pandas as pd

def predict(request):
    if request.method == 'GET':
     return render(request,"predictions/predict.html",{'form' : PredictForm()})
    else:
        form= PredictForm(request.POST or None)
        #import model file
        model = joblib.load('Addisons_Disease_Prediction_Model.sav')
        #validating user entered 18 features inputs
        if form.is_valid():
            age= form.cleaned_data.get("age")
            name= form.cleaned_data.get("name")
            muscle_weakness = form.cleaned_data.get("muscle_weakness")
            Nausea = form.cleaned_data.get("Nausea")
            vomiting = form.cleaned_data.get("vomiting")
            Postural_dizziness = form.cleaned_data.get("Postural_dizziness")
            diarrhea  = form.cleaned_data.get("diarrhea")
            body_temp_cel  = form.cleaned_data.get("body_temp_cel")
            cortisol_level = form.cleaned_data.get("cortisol_level")
            aldosterone_level = form.cleaned_data.get("aldosterone_level")
            sysBP  = form.cleaned_data.get("sysBP")
            diaBP  = form.cleaned_data.get("diaBP")
            Blood_S_low = form.cleaned_data.get("Blood_S_low")
            Blood_S_high = form.cleaned_data.get("Blood_S_high")


            #adding validated user inputs to model
            answer = model.predict([[
                                    muscle_weakness,
                                    Nausea ,
                                    vomiting ,
                                    Postural_dizziness ,
                                    diarrhea ,
                                    body_temp_cel  ,
                                    cortisol_level ,
                                    aldosterone_level,
                                    sysBP  ,
                                    diaBP  ,
                                    Blood_S_low ,
                                    Blood_S_high ,


            ]])
            #extracting predicted value
            formatted_string = "{:.2f}".format(answer[0])
            predict_value_f = (float(formatted_string)*100)
            predict_value = int(predict_value_f)

            if (predict_value <= 30 ):
                risk ="Low"
            if (predict_value > 30 and predict_value < 70  ):
                risk ="Intermediate"
            if (predict_value >= 70 and predict_value <= 100  ):
                risk ="High"

            context = {
            'age':age,
            'name':name,
            'muscle_weakness':muscle_weakness,
            'Nausea' :Nausea,
            'vomiting' :vomiting,
            'Postural_dizziness' :Postural_dizziness,
            'diarrhea' :diarrhea,
            'body_temp_cel'  :body_temp_cel,
            'cortisol_level' :cortisol_level,
            'aldosterone_level' :aldosterone_level,
            'sysBP'  :sysBP,
            'diaBP'  :diaBP,
            'Blood_S_low' :Blood_S_low,
            'Blood_S_high': Blood_S_high,
            'risk' : risk,
            'predict_value':predict_value,
            }

            lgb_predict = model.predict([[1,1,1,1,1,38.6,2,6,120,80,70,100]])


            print(lgb_predict[0])
            print(answer[0])
            return render(request,"predictions/result.html",context)

def predict_results(request):
    if request.method == 'GET':
     return render(request,"predictions/result.html")
