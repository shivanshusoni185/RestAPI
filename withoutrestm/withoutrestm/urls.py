from django.urls import path
from django.contrib import admin
from testapp.views import EmployeeDetailCBV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:id>/', EmployeeDetailCBV.as_view(), name='employee-detail'),

]
