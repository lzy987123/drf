from django.http import JsonResponse
from django.test import TestCase

# Create your tests here.
from stuapi.models import Student


def test(reqeust):
	values = Student.objects.get(sex=1)
	
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
