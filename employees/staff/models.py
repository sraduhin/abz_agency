from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

def get_head_of_supervisor():
    return Staff.objects.first()

class Staff(MPTTModel):
    ROLES = (
        ('CEO', 'CEO'),
        ('LEAD', 'Lead'),
        ('SENIOR', 'Senior'),
        ('MIDDLE', 'Middle'),
        ('JUNIOR', 'Junior'),
    )
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, null=False, blank=False, choices=ROLES)
    date_joined = models.DateField()
    salary = models.DecimalField(max_digits=9, decimal_places=2, default=50000.00)
    boss = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET(get_head_of_supervisor), related_name='subordinates')

    class MPTTMeta:
        order_insertion_by = ['full_name']
        parent_attr = 'boss'

    def __str__(self):
        return self.full_name
