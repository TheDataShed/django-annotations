import uuid
from django.db import models

class Engine(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name =  models.CharField(max_length=4096, blank=False, null=True)

class Attribute(models.Model):
	engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
	name = models.CharField(max_length=4096, blank=False, null=True)
	value = models.CharField(max_length=4096, blank=False, null=True)