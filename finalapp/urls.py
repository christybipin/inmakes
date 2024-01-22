
from . import views
from django.urls import path

urlpatterns = [

    path('', views.store, name="store"),
    path('register/', views.register, name="register"),
    path('loginView', views.loginView, name="loginView"),
    path('login', views.login, name="login"),
    path('add_form/', views.personcreateview, name="add_form"),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities', views.load_cities, name='ajax_load_cities'),
]
