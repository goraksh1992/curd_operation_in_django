from django import forms
from .models import EmployeeRegister


class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model = EmployeeRegister
        fields = ['fullname', 'mobile', 'emp_no', 'emp_pos']
        labels = {
            "fullname": "Full name",
            "mobile": "Mobile",
            "emp_no": "Emp.No",
            "emp_pos": "Emp.Position"
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeRegisterForm, self).__init__(*args, **kwargs)
        self.fields['emp_pos'].empty_label = "Select Position"
