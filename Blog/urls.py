from django.urls import path
from . import views

urlpatterns = [
    path('blogs/',views.Blogs,name="blos"),
    path('blog_details/<int:pk>/',views.BlogDetail,name="blog_detail"),
]
