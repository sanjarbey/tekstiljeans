from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from order.views import *

urlpatterns = [
     path('', home_site, name="home_site"),
     path('order/', home_order, name="home_order"),
]