import django_rq
import json
import re
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models


def dummy_method(json_string):
	js_dcode = json_string.decode('utf-8')
	rows = json.loads(js_dcode)["myrows"]
	engines = []

	for row in rows[0]:
		engine_name = re.search('(?<=>).*?(?=<)', row)
		if engine_name:
			engine = models.Engine.objects.create(name=engine_name)
			engine.save()
			engines.append(engine)

	x = 0
	while x <= len(rows) - 1:
		filtered_values = []

		for value in rows[x].values(): 
			if value != "" and ">" not in value:
				filtered_values.append(value)

		i = 0
		while i <= 3:
			# engines[i]["attributes"].append({"attribute_name": filtered_values[i]})
			attribute = models.Attribute.objects.create(engine=engines[i], name="attribute_name", value=filtered_values[i])
			attribute.save()
			i+=1
		x+=1


@csrf_exempt
def enqueue(request):
	if request.method == "POST":
		# TODO: Correct method.
		django_rq.enqueue(dummy_method, request.body)
		return HttpResponse(status=204)
	else:
		return HttpResponseForbidden()
