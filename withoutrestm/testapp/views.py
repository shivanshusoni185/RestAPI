from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.core.serializers import serialize

class EmployeeDetailCBV(View):
    def get(self, request, id, *args, **kwargs):
        try:
                 qs = Employee.objects.all()
                 json_data = serialize('json', qs)
                 return HttpResponse(json_data, content_type='application/json')
        except Employee.DoesNotExist:
            return HttpResponse(status=404)  # Return a 404 response if the employee is not found
