from django.urls import path
from . import views


urlpatterns = [
    # path('new', views.newblog, name='new-blog'),
    # path('404', views.error, name='404'),
    path('', views.predict, name='predict'),
    path('result', views.predict_results, name='result'),




]
