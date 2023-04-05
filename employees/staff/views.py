from django.views.generic.list import ListView
from employees.staff.models import Staff

class StaffView(ListView):
    model = Staff

    template_name = 'tree.html'