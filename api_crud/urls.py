from django.contrib import admin
from django.conf.urls import include, url
from .views import RegisterView, CustomLoginView
from django.urls import include, path, re_path
from core.homepage.views import IndexView

#from core.login.views import *

# urls
urlpatterns = [
    url(r'^', include('validadores.urls')),
    path('login/', include('core.login.urls')),
    path('erp/', include('core.erp.urls')),
    path('reports/', include('core.reports.urls')),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registration/', RegisterView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
    
]