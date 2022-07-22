from rest_framework.viewsets import ModelViewSet
from stuapi.models import Student
from students.serializers import StudentModelSerializer
# Create your views here.

class StudentModelViewSet(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentModelSerializer

