import json

from django.views import View
from django.http import JsonResponse

from .models import Student


# Create your views here.


class StudentView(View):
	def post(self, request):
		name = request.POST.get("name")
		sex = request.POST.get("sex")
		age = request.POST.get("age")
		classmate = request.POST.get("classmate")
		description = request.POST.get("description")
		
		isntance = Student.objects.create(
			name=name,
			sex=sex,
			age=age,
			classmate=classmate,
			description=description
		)
		return JsonResponse(
			data={
				"name": isntance.name,
				"sex": isntance.sex,
				"age": isntance.age,
				"classmate": isntance.classmate,
				"description": isntance.description
			}
		)
	
	def get(self, request):
		values = list(Student.objects.values())
		return JsonResponse(data=values, safe=False)


class StudentInfoView(View):
	def get(self, request, pk):
		try:
			values = Student.objects.get(pk=pk)
			return JsonResponse(data=
			{
				"id": values.id,
				"name": values.name,
				"sex": values.sex,
				"age": values.age,
				"classmate": values.classmate,
				"description": values.description
			},
				safe=False)
		except Student.DoesNotExist:
			return JsonResponse(data={}, safe=False)

	def put(self, request, pk):
		data = json.loads(request.body)
		name = data.get("name")
		sex = data.get("sex")
		age = data.get("age")
		classmate = data.get("classmate")
		description = data.get("description")

		try:
			inst = Student.objects.get(pk=pk)
			inst.name = name
			inst.sex = sex
			inst.age = age
			inst.classmate = classmate
			inst.description = description
			inst.save()
		except Student.DoesNotExist:
			return JsonResponse(data={}, safe=False)
		return JsonResponse(
			data={
				"name": inst.name,
				"sex": inst.sex,
				"age": inst.age,
				"classmate": inst.classmate,
				"description": inst.description
			}
		)
	
	def delete(self, request, pk):
		try:
			Student.objects.filter(pk=pk).delete()
		except:
			pass
		return JsonResponse(data={}, status=204)