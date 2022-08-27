from django.urls import path, re_path

import test
from . import views, tests

urlpatterns = [
	path('students/',views.StudentView.as_view()),
	re_path('^students/(?P<pk>\d+)/?', views.StudentInfoView.as_view()),
	path("test/",tests.test)
]