from django.urls import path
from .views import *

urlpatterns = [
    path('cookie/', cookie_count_view),
    path('session/', session_count_view),
]