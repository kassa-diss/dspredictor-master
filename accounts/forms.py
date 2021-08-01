from django import forms
from .models import Instructor,Patient,MyWorks,Event
from django.forms import formset_factory
from django.forms import ModelForm, DateInput



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




class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
