from django import forms
from django.forms import ModelForm
from . import models
from administrative.models import Employee, Teaching_Period

class classForm(forms.ModelForm):
    class Meta:
        fields = ['unit_id', 't_period', 'time_commi', 'code']
        model = models.Class

    def __init__(self, user, *args, **kwargs):
        super(classForm, self).__init__(*args, **kwargs)
        emp = Employee.objects.filter(user=user).first()
        self.fields['unit_id'].queryset  = emp.units.all()



