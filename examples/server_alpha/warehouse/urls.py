from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from warehouse import views

urlpatterns = patterns('',
    url(r'^customers$', views.CustomerList.as_view(), name='customers-list'),
    url(r'^customers/(?P<pk>[0-9]+)$', views.CustomerDetail.as_view(), name='customers-detail'),

    url(r'^products$', views.ProductList.as_view(), name='products-list'),
    url(r'^products/(?P<pk>[0-9]+)$', views.ProductDetail.as_view(), name='products-detail'),

    url(r'^orders$', views.OrderList.as_view(), name='orders-list'),
    url(r'^orders/(?P<pk>[0-9]+)$', views.OrderDetail.as_view(), name='orders-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
