from django.urls import path
from .views import *
from .appoint import *
urlpatterns = []

pages=[path('', home, name='home'),
    path('courses', courses, name='courses'),
    path('students', students, name='students'),
    path('appoint', appoint, name='appoint'),]



functionalities=[ path('appoint_user/', appoint_user, name='appoint_user'),
                  path('get_courses_by_department/<int:department_id>/', get_courses_by_department, name='get_courses_by_department'),
                  path('get_departments/', get_departments, name='get_departments')
                 ]

urlpatterns+=pages
urlpatterns+=functionalities

