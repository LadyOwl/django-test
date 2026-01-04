from django.contrib import admin
from django.urls import path
from users import views as uviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', uviews.login, name='login', ),
    path('register/', uviews.login, name='register', ),
]
