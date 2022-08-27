from django.db import models


class ClassMateModel(models.Model):
	class_name = models.CharField(verbose_name="科目名称", max_length=30)
	username = models.CharField(verbose_name="学生姓名", max_length=50)
	grade = models.IntegerField(verbose_name="分数")
	
	
	
