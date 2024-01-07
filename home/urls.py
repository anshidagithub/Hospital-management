from django.urls import path,include
from . import views



urlpatterns = [
   
    path('signup', views.signup,name= 'signup'),
    path('', views.loginn,name= 'login'),
    path('logout', views.logout,name= 'logout'),
    

    path('home', views.index,name= 'home'),
    path('about/', views.about,name= 'about'),
    path('booking/', views.booking,name= 'booking'),
    path('doctors', views.docters,name= 'doctors'),
    path('contact', views.condact,name= 'contact'),
    path('department', views.department,name= 'department'),
    
]
