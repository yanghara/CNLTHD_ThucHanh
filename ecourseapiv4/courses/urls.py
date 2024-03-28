from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from courses import views

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, 'categories')
r.register('courses', views.CourseViewSet, 'courses')


urlpatterns = [
    path('', include(r.urls))
]