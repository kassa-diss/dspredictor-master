from django.forms import ModelForm
from django import forms

Choices= [
    (0, 'No'),
    (1, 'Yes'),
    ]

class PredictForm(forms.Form):
    name = forms.CharField(label='Enter your name')
    age = forms.IntegerField(label='Enter age')
    

    muscle_weakness = forms.IntegerField(label = "Do you have Muscle weakness",widget=forms.Select(choices=Choices))
    Nausea = forms.IntegerField(label ="Do you have nausea",widget=forms.Select(choices=Choices))
    vomiting = forms.IntegerField(label ="Do you have vomiting",widget=forms.Select(choices=Choices))
    Postural_dizziness = forms.IntegerField(label ="Do you have postural_dizziness",widget=forms.Select(choices=Choices))
    diarrhea  = forms.IntegerField(label ="Do you have diarrhea",widget=forms.Select(choices=Choices))
    body_temp_cel  = forms.FloatField(label ="Enter body temperature")
    cortisol_level = forms.IntegerField(label ="Enter blood cortisol_level")
    aldosterone_level = forms.IntegerField(label ="Enter aldosterone_level")
    sysBP  = forms.IntegerField(label='Systolic blood pressure')
    diaBP  = forms.IntegerField(label='Diastolic blood pressure')
    Blood_S_low = forms.IntegerField(label ="Enter blood suger low")
    Blood_S_high = forms.IntegerField(label ="Enter blood sugar high")
