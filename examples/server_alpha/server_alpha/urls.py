from django.conf.urls import include, url
from django.contrib import admin
from server_alpha import views

urlpatterns = [
    url(r'^api/v1/$', views.api_root),
    url(r'^api/v1/', include('warehouse.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
