from django.views import View

from django.http import JsonResponse
from .serializers import Student1Serializer
from stuapi.models import Student

# Create your views here.

class StudentView(View):
	# def get(self,request):
	# 	student_list = Student.objects.all()
	#
	# 	serializer = Student1Serializer(instance=student_list)
	# 	data = serializer.data
	#
	# 	return JsonResponse(data=data, status=200, safe=False)
	# def get2(self, request):
	# 	student_list = Student.objects.all()
	#
	# 	serializer = Student1Serializer(instance=student_list, many=True)
	#
	# 	data = serializer.data
	# 	return JsonResponse(data=data, status=200, safe=False)
	
	# def get(self, request):
	#   """序列化器"""
	# 	stu_list = Student.objects.all()
	# 	s = Student1Serializer(instance=stu_list)
	# 	data = s.data
	# 	return JsonResponse(data, safe=False)
	
	def get(self, request):
		"""继承django.view的反序列化器"""
		data = {
			"name": "xiaoming",
			"age": 11,
			"sex": True,
			"classmate": "307",
			"description": "什么都没有~"
		}
		print(123)
		serializer = Student1Serializer(data=data)
		ret = serializer.is_valid()
		if ret:
			return JsonResponse(dict(serializer.validated_data))
		else:
			return JsonResponse(dict(serializer.errors))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	