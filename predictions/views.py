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
        model = joblib.load('DS_Predictor_Model.sav')
        #validating user entered 18 features inputs
        if form.is_valid():
            age= form.cleaned_data.get("age")
            name= form.cleaned_data.get("name")
            head_Circumference_Inches = form.cleaned_data.get("head_Circumference_Inches")
            lines_across_the_palm = form.cleaned_data.get("lines_across_the_palm")
            protruding_tongue = form.cleaned_data.get("protruding_tongue")
            height_in_Inches = form.cleaned_data.get("height_in_Inches")
            sysBP  = form.cleaned_data.get("sysBP")
            diaBP  = form.cleaned_data.get("diaBP")


            #adding validated user inputs to model
            answer = model.predict([[
                                    head_Circumference_Inches,
                                    lines_across_the_palm,
                                    protruding_tongue,
                                    height_in_Inches,
                                    sysBP,
                                    diaBP,


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
            'predict_value':predict_value,
            'head_Circumference_Inches' : head_Circumference_Inches,
            'lines_across_the_palm' : lines_across_the_palm,
            'protruding_tongue' : protruding_tongue,
            'height_in_Inches' : height_in_Inches,
            'sysBP' : sysBP,
            'diaBP' : diaBP,
            'risk' : risk,

            }
            lgb_predict = model.predict([[11.0,5,0,19.5,70,40]])


            print(lgb_predict[0])
            print(answer[0])
            return render(request,"predictions/result.html",context)

def predict_results(request):
    if request.method == 'GET':
     return render(request,"predictions/result.html")
