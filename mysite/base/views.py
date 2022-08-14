from django.shortcuts import render
from . models import Students
from .serializer import studentserializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def student_deatails(request):
    stu = Students.objects.all()
    serializer = studentserializers(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
