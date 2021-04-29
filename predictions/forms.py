from django.forms import ModelForm
from django import forms



class PredictForm(forms.Form):
    name = forms.CharField(label='Enter your name')
    age = forms.IntegerField(label='Enter age')
    head_Circumference_Inches = forms.FloatField(label='Head circumference in inches')
    lines_across_the_palm = forms.IntegerField(label='Lines across the palm')
    protruding_tongue = forms.IntegerField(label='Protruding tongue')
    height_in_Inches = forms.FloatField(label='Height in inches')
    sysBP  = forms.IntegerField(label='Systolic blood pressure')
    diaBP  = forms.IntegerField(label='Diastolic blood pressure')
