# from rest_framework.routers import DefaultRouter
from django.urls import path
from mianshi import views
# router = DefaultRouter()
# router.register(
#
# )




urlpatterns = [
	path("meta/",views.ClassMetaView.as_view()),
	path("get_class_mate_view/", views.GetClassMateView.as_view()),
	path("ClassMateListView/", views.ClassMateListView.as_view()),
	path("BookDetailView/", views.BookDetailView.as_view())
]