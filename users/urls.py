from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("field-student/", views.field_student, name="field_student"),
    path("activity/", views.activity, name="activity"),
    path("profile/", views.profile, name="profile"),
    path("teacher/", views.teacher, name="teacher"),
]