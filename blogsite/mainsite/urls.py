from django.urls import path

from .views import *

app_name = 'mainsite'

urlpatterns = [
    path('', Home, name='Home'),
    path('blogUpload', uploadContent, name='blogUpload'),
    path('editContent/<int:id>', editContent, name='editContent'),
    path('delPost/<int:id>', delPost, name='delPost'),

]
