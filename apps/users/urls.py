from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index, name="index"),
    #url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^success$', views.success, name="success"),
    url(r'^logout$', views.logout, name="logout"),  
    url(r'^users/(?P<user_id>\d+)$', views.account, name="account")  
]                            
