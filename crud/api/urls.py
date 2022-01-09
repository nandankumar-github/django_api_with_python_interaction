from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.student_api),
    path('student/<int:pk>',views.student_api),
    ]