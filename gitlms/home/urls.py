from django.urls import path
from .views import *

urlpatterns = [
    path('', departments, name='departments'),
    path('courses', courses, name='courses'),
    path('students', students, name='students'),
    path('appoint', appoint, name='appoint'),
    path('changerole/<int:userid>/<str:role>/', changerole, name='changerole')
    
]
