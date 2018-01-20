from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login_page$', views.LoginMockView.as_view(), name='login'),
    url(r'^products$', views.ProductsMockView.as_view(), name='products'),
]
