from django import forms
from .models import Instructor,Patient,MyWorks
from django.forms import formset_factory




# #employee forms
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['qualification',
#                   'phone',
#                   'email',
#                   'address',
#                   'birth_date',
#                   'profile_picture',
#                   'guardian',
#                   'bio',
#                   'is_instuctor']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
                  'phone',
                  'email',
                  'address',
                  'birth_date',
                  'profile_picture',
                  'guardian',
                  'bio',
                  ]

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['qualification',
                  'phone',
                  'email',
                  'address',
                  'birth_date',
                  'profile_picture',
                  'bio',
                  ]

class MyWorksForm(forms.ModelForm):
    


    class Meta:
        model = MyWorks
        fields = [
                          'title',
                          'description',
                          'picture_1',
                          'picture_2',
                          'picture_3',
                          'video',
                  ]
