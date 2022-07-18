from django.urls import path
from . import views
from chat import views as v
# URL конфигуратор
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logOutUser, name='logout'),

    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]