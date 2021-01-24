from django.urls import include, path, re_path
from . import views
from core.homepage.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), #HY1
    path('process_email/', views.spam_ham_predict.as_view(), name = 'predict'),
    path('history/<N_EMAILS>/', views.history, name='history'),
]