from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from headeropening import views as headeropening_views

urlpatterns = [
    path('', headeropening_views.index, name='index'),
    path('elements', headeropening_views.elements, name='elements'),
    path('generic', headeropening_views.generic, name='generic'),
    #path('accounts/login', headeropening_views.index, name='index'),
    url('signup', headeropening_views.signup, name='signup'),
    url('login', auth_views.login, {'template_name': 'headeropening/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': 'login'}, name='logout'),
    #url('login', auth_views.login, {'template_name': 'headeropening/login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url('account_activation_sent', headeropening_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        headeropening_views.activate, name='activate'),
]
