from django.urls import path
from .views import *

urlpatterns = [
    path('additem/', add_view),
    path('display/', dispaly_view),
]