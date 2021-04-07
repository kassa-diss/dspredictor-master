from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),


    path('profile', views.PatientCreateView, name='edit-profile'),
    path('profile/<pk>/edit', views.PatientUpdateView.as_view(), name='edit-profiledata'),
    path('patient/<int:user_id>', views.PatientProfileView.as_view() , name='patient'),
    path('instructor/<int:user_id>', views.InstructorProfileView.as_view() , name='instructor'),

    path('patients', views.Patients, name='Patients'),
    path('instructors', views.Instructors, name='Instructors'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
