from django.contrib import admin
from django.urls import path
from shop.views import helloworld



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', helloworld)
]
