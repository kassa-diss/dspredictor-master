from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),


    # path('profile', views.PatientCreateView, name='edit-profile'),
    # path('profile/<pk>/edit', views.PatientUpdateView.as_view(), name='edit-profiledata'),
    # path('patient/<int:user_id>', views.PatientProfileView.as_view() , name='patient'),
    # path('instructor/<int:user_id>', views.InstructorProfileView.as_view() , name='instructor'),

    path('patient/new', views.PatientCreateView, name='edit-profile'),
    path('patient/<pk>/edit', views.PatientUpdateView.as_view(), name='edit-profiledata'),
    path('patient/<pk>', views.PatientProfileView.as_view() , name='patient'),
    path('instructor/<pk>', views.InstructorProfileView.as_view() , name='instructor'),



    path('patients', views.Patients, name='Patients'),
    path('instructors', views.Instructors, name='Instructors'),

    path('patient-my', views.PatientMyProfile, name='myprofile-patient'),
    path('instructor-my', views.InstructorMyProfile, name='myprofile-instructor'),

    path('addmyworks', views.MyWorksCreateView , name='addmyworks'),
    path('talent', views.talent , name='talent'),

    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('event/new', views.event, name='event_new'),
	path('event/edit/<event_id>/', views.event, name='event_edit'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
