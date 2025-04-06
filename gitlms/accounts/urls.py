from django.urls import path
from gitlms import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', welcome, name='welcome'),
    path('welcome/', welcome, name='welcome'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),  # Already included
    path('logout/', logout_view, name='logout'),
    path('viewprof/', view_prof, name='viewprof'),
    path('edit-prof/', edit_profile, name='edit-prof'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
