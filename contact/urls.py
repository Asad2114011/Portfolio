from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contact_msg/',contact_view,name='contact'),
]
