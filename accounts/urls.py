from . import views
from django.urls import path

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('my_account/', views.account_manage, name='account-manage'),
    path('logout/', views.logout_user, name='logout'),

]
