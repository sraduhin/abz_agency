from django.urls import path
from employees.staff.views import StaffView

urlpatterns = [
    path('', StaffView.as_view(), name='staff_index'),
]
