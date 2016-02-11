import django_rq
import json
import re
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from . import models
from annotation.models import Annotation

class Row:
	name = ""
	attribute_values = []

def dummy_method(json_string):
	js_dcode = json_string.decode('utf-8')
	rows = json.loads(js_dcode)["myrows"]

	engines = []

	for row in rows[0]:
		pattern = re.compile(u'(?<=>).*?(?=<)', re.UNICODE)
		engine_name = pattern.search(row)
		if engine_name:
			engine = models.Engine.objects.create(name=engine_name.group())
			engine.save()
			engines.append(engine)

	x = 0
	table_rows = [] 
	while x <= len(rows) - 1:
		row = Row()
		row.attribute_values = []
		for row_value in rows[x].values():
			if ">" in row_value:
				annotation_id = row_value[47:83]
				row.name = Annotation.objects.get(pk=annotation_id).quote
			if ">" not in row_value and row_value != "":
				row.attribute_values.append(row_value)				
		table_rows.append(row)
		x+=1

	i = 0
	for row in table_rows:
		if row.name == "":
			row.name = "untagged attribute"
		for x in range(len(engines)):
			engine_attribute = models.Engine_Attribute.objects.create(engine=engines[x], name=row.name)
			engine_attribute.save()
		for attribute in row.attribute_values:
		 	engine_value = models.Attribute_Value.objects.create(engine_attribute=engine_attribute, value=attribute)
		 	engine_value.save()
		i+=0





	# x = 0
	# while x <= len(rows) - 1:
	# 	filtered_values = []

	# 	for value in rows[x].values(): 
	# 		if ">" in value:
	# 			print(value[48:]) 
	# 		if value != "" and ">" not in value:
	# 			filtered_values.append(value)

	# 	i = 0
	# 	while i <= 3:	
	# 		print(rows[x].values()[0])	
	# 		#attribute_name = Annotation.objects.get(pk=1)
	# 		#print("attrib name: " + attribute_name.quote)		
	# 		#attribute = models.Attribute.objects.create(engine=engines[i], name="attribute_name", value=filtered_values[0])
	# 		#attribute.save()
	# 		i+=1
	# 	x+=1


@csrf_exempt
def enqueue(request):
	if request.method == "POST":
		# TODO: Correct method.
		django_rq.enqueue(dummy_method, request.body)
		return HttpResponse(status=204)
	else:
		return HttpResponseForbidden()
