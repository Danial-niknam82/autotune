from django.urls import path
from .views import (
    helloworld, about, login_user, logout_user, signup_user,
    product, category, add_advertisement, advertisement_detail
)

urlpatterns = [
    path('', helloworld, name='home'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_user, name='signup'),
    path('product/<int:pk>/', product, name='product'),
    path('category/<str:cat>/', category, name='category'),
    path('add_advertisement/', add_advertisement, name='add_advertisement'),
    path('advertisement/<int:pk>/', advertisement_detail, name='advertisement_detail'),
]