from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    # Sign up Log{in, out}
    url(r'signup/$', views.SignupView.as_view(), name='signup'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),

    # main app
    url('nearby_shops/$', views.ShopsListView.as_view(), name='shops_list'),
]
