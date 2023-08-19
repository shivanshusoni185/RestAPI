from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeCRUDCBV.as_view()),
    # path('api/', views.EmployeeListCBV.as_view()),
]
