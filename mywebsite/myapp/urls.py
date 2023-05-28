from django.urls import path
from .views import Homepage, About, Products, Services, Contact

urlpatterns = [
    path("", Homepage, name='home'), # localhost:8000 -> Homepage
    path("about/", About, name='about'),
    path("product/", Products, name='product'),
    path("service/", Services, name='service'),
    path("contact/", Contact, name='contact'),
]