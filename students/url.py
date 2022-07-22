from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("stu2", views.StudentModelViewSet, basename="stu2")

urlpatterns = [

] + router.urls