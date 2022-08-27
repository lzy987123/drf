import json

from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
from mianshi.models import ClassMateModel





class ClassMetaView(View):
	def get(self,request):
		data = json.loads(request.body)
		meta_obj = [ClassMateModel(**i) for i in data]
		ClassMateModel.objects.bulk_create(meta_obj)
		return JsonResponse({"123": "456"})
	

class GetClassMateView(View):
	def get(self, request):
		# objs = ClassMateModel.objects.values_list("class_name").annotate(max_grade=Max('grade'))
		objs = ClassMateModel.objects.values_list("class_name").annotate(max_grade=Max("grade"))
		data_str = ""
		for obj in objs:
			print(obj.username)
			print(obj.class_name)
			print(obj.grade)
			# data_str = ",".join([obj.username, obj.class_name , obj.grade]))
		data_dict = {"info":data_str}
		return JsonResponse(data_dict)


class ClassMateListView(View):
	def get(self,request):
		class_mate = ClassMateModel.objects.all()
		class_mate_list = []
		for cm in class_mate:
			data_dict = {
				"id":cm.id,
				"class_name": cm.class_name,
				"username": cm.username,
				"grade": cm.grade if cm.grade else ""
			}
			class_mate_list.append(data_dict)
		return JsonResponse(class_mate_list, safe=False)
	
	def post(self, request):
		pass
		

class BookDetailView(View):
	def get(self, request):
		data = json.loads(request.body)
		id_only = data.get("id")
		try:
			class_mate = ClassMateModel.objects.get(id=id_only)
		except ClassMateModel.DoesNotExist:
			return JsonResponse({"message": "ID为%s获取失败, %s" % (id_only, e)})
		data_list = []
		data_dict = {
			"id": class_mate.id,
			"class_name": class_mate.class_name,
			"username": class_mate.username,
			"grade": class_mate.grade if class_mate.grade else ""
		}
		data_list.append(data_dict)
		return JsonResponse(data_list, safe=False)
	
	
	