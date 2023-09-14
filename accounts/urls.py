from . import views
from django.urls import path

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('my_account/', views.account_manage, name='account-manage'),
    path('my_account/account', views.account_option, name='account-option'),
    path('my_account/account/orders', views.account_orders, name='account-orders'),
    path('logout/', views.logout_user, name='logout'),

]
