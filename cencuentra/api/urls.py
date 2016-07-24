from django.conf.urls import url
from . import views as api_view
urlpatterns = [
    # User URL's
    url(r'user/register$', api_view.UserRegisterView.as_view(), name='user_api'),
    url(r'user/$', api_view.UserView.as_view(), name='myuser_api'),
    url(r'user/(?P<pk>[0-9]+)/$', api_view.UserDetailView.as_view(), name='myuser_api_detail'),
    # Admin URL's
    url(r'admin/register$', api_view.AdminRegisterView.as_view(), name='admin_api'),
    url(r'admin/$', api_view.AdminView.as_view(), name='myadmin_api'),
    url(r'admin/(?P<pk>[0-9]+)/$', api_view.AdminDetailView.as_view(), name='myadmin_api_detail'),

]
