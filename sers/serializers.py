from rest_framework import serializers


class Student1Serializer(serializers.Serializer):
	"""学生信息序列化器"""
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	sex = serializers.BooleanField(default=True)
	age = serializers.IntegerField(max_value=100, min_value=0)
	classmate = serializers.CharField()
	description = serializers.CharField(allow_null=True, allow_blank=True)
	
	
	def validate(self, attrs):
		"""
			验证客户端传来的所有数据
		"""
		# 例307班只招女同学
		if attrs["classmate"] == "307" and attrs["sex"]:
			raise serializers.ValidationError(detail="307班只招女同学", code="validate")
		return attrs
	
	
	def validate_name(self, attrs):
		"""验证单个字段
			方法名的格式必须以 validate_<字段名> 为函数名称否则序列化器不识别
			validate开头的方法，会自动被is_valid调用
		"""
		if attrs in ["python","django"]:
			raise serializers.ValidationError(detail="name不合法", code="validate_name")
		print("name=%s"%(attrs))
		return attrs
	
	

	
