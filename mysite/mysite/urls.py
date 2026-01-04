from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login', ),
    path('register/', views.login, name='register', ),
]
